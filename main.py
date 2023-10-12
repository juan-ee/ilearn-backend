from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
import sqlite3
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from utilities import *
import shutil


class Report(BaseModel):
    id: Optional[str] = None
    company_name: str
    industry: str
    logo_path: Optional[str] = None
    pdf_path: Optional[str] = None
    pptx_path: Optional[str] = None
    rating_ecovadis: str
    rating_cdp: str
    rating_sp_dow_jones: str
    rating_msci: str
    rating_sustainalitycs: str


app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/logos", StaticFiles(directory="logos"), name="logos")
app.mount("/pdfs", StaticFiles(directory="pdfs"), name="pdfs")
app.mount("/pptxs", StaticFiles(directory="pptxs"), name="pptxs")


@app.get("/reports")
def get_all_reports():
    conn = sqlite3.connect('db/app_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, company_name, industry, logo_path, pdf_path, pptx_path, rating_ecovadis, rating_cdp, rating_sp_dow_jones, rating_msci, rating_sustainalitycs FROM reports')
    reports_data = cursor.fetchall()
    conn.close()

    items = [Report(id=id,
                    company_name=company_name,
                    industry=industry,
                    logo_path=logo_path,
                    pdf_path=pdf_path,
                    pptx_path=pptx_path,
                    rating_ecovadis=rating_ecovadis,
                    rating_cdp=rating_cdp,
                    rating_sp_dow_jones=rating_sp_dow_jones,
                    rating_msci=rating_msci,
                    rating_sustainalitycs=rating_sustainalitycs) for id, company_name, industry, logo_path, pdf_path, pptx_path, rating_ecovadis, rating_cdp, rating_sp_dow_jones, rating_msci, rating_sustainalitycs in reports_data]
    return items


# TODO: next week
@app.get("/reports/{report_id}")
def get_report_by_id(report_id: int):
    conn = sqlite3.connect('db/app_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, company_name, industry FROM reports WHERE id = ?', (report_id,))
    report = cursor.fetchone()
    conn.close()

    if report is None:
        raise HTTPException(status_code=404, detail="Item not found")

    id, company_name, industry = report

    return {"id": id, "company_name": company_name, "industry": industry}


# TODO: process the pdf
@app.post("/reports")
def insert_report(company_name: str = Form(...),
                  pdf: UploadFile = File(...),
                  image: UploadFile = File(...)):
    if pdf.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File is not a PDF")

        # Ensure the image is of correct type. For example, checking if it's a PNG:
    if image.content_type not in ["image/png", "image/jpeg", "image/jpg"]:
        raise HTTPException(status_code=400, detail="Image is not valid")

    report_id = get_timestamp()

    pdf_path = f"pdfs/{report_id}.pdf"
    # Handle saving files to storage (for now, saving to the local disk)
    with open(pdf_path, "wb") as buffer:
        buffer.write(pdf.file.read())

    # save logo
    logo_path = f"logos/{report_id}.{image.filename.split('.')[-1]}"
    with open(logo_path, "wb") as buffer:
        buffer.write(image.file.read())

    # process pdf
    pptx_path = f'pptxs/{report_id}.pptx'
    shutil.copy('template.pptx', pptx_path)

    conn = sqlite3.connect('db/app_database.db')

    industry = get_industry_auto(company_name)
    rating_ecovadis = get_ratings_ecovadis()
    rating_cdp = get_ratings_cdp()
    rating_sp_dow_jones = get_ratings_dowjones()
    rating_msci = get_ratings_msci()
    rating_sustainalitycs = get_ratings_sustainalytics()

    data = (report_id, company_name, industry, logo_path, pdf_path, pptx_path, rating_ecovadis, rating_cdp, rating_sp_dow_jones, rating_msci, rating_sustainalitycs)

    cursor = conn.cursor()
    cursor.execute('INSERT into reports (id, company_name, industry, logo_path, pdf_path, pptx_path, rating_ecovadis, rating_cdp, rating_sp_dow_jones, rating_msci, rating_sustainalitycs)'
                   'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', data)
    conn.commit()
    conn.close()

    return {"inserted": "ok"}


@app.get("/last-4-reports")
def get_all_reports():
    conn = sqlite3.connect('db/app_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reports ORDER BY id DESC LIMIT 4')
    reports_data = cursor.fetchall()
    conn.close()

    items = [Report(id=data[0],
                    company_name=data[1],
                    industry=data[2],
                    logo_path=data[3],
                    pdf_path=data[4],
                    pptx_path=data[5],
                    ratings_ecovadis=data[6],
                    ratings_cdp=data[7],
                    ratings_dowjones=data[8],
                    ratings_msci=data[9],
                    rating_sustainalitycs=data[10]) for data in reports_data]
    return items
