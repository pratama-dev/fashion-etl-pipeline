from utils.extract import extract_all
from utils.transform import transform_data
from utils.load import load_to_csv, load_to_postgres, load_to_gsheets
import logging

def main():
    logging.info("Memulai ETL Pipeline...")
    
    # Ekstraksi
    raw_df = extract_all(total_pages=50)
    
    # Transformasi
    clean_df = transform_data(raw_df)
    
    # Load
    if not clean_df.empty:
        # 1. Flat File
        load_to_csv(clean_df, 'products.csv')
        
        # 2. PostgreSQL (Ganti kredensial Anda)
        db_string = "postgresql://username:password@localhost:5432/dbname"
        load_to_postgres(clean_df, db_string)
        
        # 3. Google Sheets (Ganti SPREADSHEET_ID dengan ID di URL sheet Anda)
        SHEET_ID = 'YOUR_SPREADSHEET_ID'
        load_to_gsheets(clean_df, SHEET_ID, 'A1')
    else:
        logging.warning("Dataframe kosong. Tidak ada data yang diload.")

if __name__ == "__main__":
    main()