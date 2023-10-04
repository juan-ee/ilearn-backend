# script to create the db

import sqlite3

conn = sqlite3.connect('app_database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reports (
        id TEXT PRIMARY KEY,
        company_name TEXT NOT NULL,
        industry TEXT NOT NULL,
        logo_path TEXT NOT NULL,
        pdf_path TEXT NOT NULL,
        pptx_path TEXT,
        rating_ecovadis TEXT,
        rating_cdp TEXT,
        rating_sustainalitycs TEXT,
        rating_msci TEXT,
        rating_sp_dow_jones TEXT,
        base_of_operations TEXT,
        employees_number INT,
        risks TEXT,
        opportunities TEXT,
        env_general TEXT,
        env_emission_management TEXT,
        env_resources_management TEXT,
        env_waste_management TEXT,
        social TEXT,
        governance_economics TEXT
    )
''')

# cursor.execute('''
#     INSERT INTO reports (
#     id, company_name, industry, logo_path, pdf, pptx, rating_ecovadis, rating_cdp, rating_sustainalitycs, rating_msci, rating_sp_dow_jones,
#     base_of_operations, employees_number, risks, opportunities, env_general, env_emission_management, env_resources_management, env_waste_management,
#     social, governance_economics
# ) VALUES (
#     '1', 'ABC Company', 'Technology', '/logos/abc_logo.png', '/reports/abc_report.pdf', '/reports/abc_report.pptx', 'A', 'B', 'C', 'D', 'E',
#     'New York', 500, 'Environmental risks', 'Market expansion', 'Green initiatives', 'Reduced emissions', 'Resource efficiency', 'Waste reduction',
#     'Community engagement', 'Strong governance'
# )
# ''')

conn.commit()
conn.close()
