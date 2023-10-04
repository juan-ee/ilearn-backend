# script to create the db

import sqlite3

conn = sqlite3.connect('app_database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reports (
        id TEXT PRIMARY KEY,
        company_name TEXT NOT NULL,
        industry TEXT NOT NULL,
        logo_path TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
