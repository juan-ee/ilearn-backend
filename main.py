from fastapi import FastAPI, HTTPException
import sqlite3
from uuid import uuid4
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware


class Report(BaseModel):
    id: Optional[str] = None
    company_name: str
    industry: str


app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/reports")
def get_all_reports():
    conn = sqlite3.connect('db/app_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reports')
    reports_data = cursor.fetchall()
    conn.close()

    items = [Report(id=id, company_name=company_name, industry=industry) for id, company_name, industry in reports_data]
    return items


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


@app.post("/reports")
def insert_report(report: Report):
    conn = sqlite3.connect('db/app_database.db')
    report.id = str(uuid4())

    data = (report.id, report.company_name, report.industry)

    cursor = conn.cursor()
    cursor.execute('INSERT into reports VALUES (?, ?, ?)', data)
    conn.commit()
    conn.close()

    return {"inserted": "ok"}

