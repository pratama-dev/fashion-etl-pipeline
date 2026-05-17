import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sqlalchemy import create_engine
import logging

def load_to_csv(df, filename):
    try:
        df.to_csv(filename, index=False)
        logging.info(f"Data disimpan ke {filename}")
    except Exception as e:
        logging.error(f"Gagal simpan CSV: {e}")

def load_to_gsheets(df, spreadsheet_id, range_name):
    try:
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            'google-sheets-api.json',
            scope
        )

        client = gspread.authorize(creds)
        sheet = client.open_by_key(spreadsheet_id).sheet1
        sheet.clear()
        data = [df.columns.values.tolist()] + df.values.tolist()
        sheet.update(range_name, data)
        logging.info("Data berhasil dikirim ke Google Sheets")
    except Exception as e:
        logging.error(f"Gagal ke Google Sheets: {e}")

def load_to_postgres(df, db_string):
    try:
        engine = create_engine(db_string)
        df.to_sql('fashion_products', engine, if_exists='replace', index=False)
        logging.info("Data berhasil disimpan ke PostgreSQL")
    except Exception as e:
        logging.error(f"Gagal ke PostgreSQL: {e}")