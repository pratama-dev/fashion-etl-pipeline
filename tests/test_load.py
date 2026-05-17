import os
import pandas as pd
from unittest.mock import patch, MagicMock
from utils.load import (
    load_to_csv,
    load_to_postgres,
    load_to_gsheets
)


# =========================
# TEST LOAD CSV
# =========================
def test_load_to_csv():
    df = pd.DataFrame({
        'Title': ['T-shirt'],
        'Price': [1600000]
    })

    filename = 'test_products.csv'

    # Jalankan fungsi
    load_to_csv(df, filename)

    # Cek file berhasil dibuat
    assert os.path.exists(filename)

    # Cek isi file tidak kosong
    loaded_df = pd.read_csv(filename)
    assert not loaded_df.empty
    assert loaded_df.iloc[0]['Title'] == 'T-shirt'

    # Cleanup
    os.remove(filename)


# =========================
# TEST LOAD POSTGRES
# =========================
@patch('utils.load.create_engine')
def test_load_to_postgres(mock_create_engine):
    df = pd.DataFrame({
        'Title': ['Hoodie'],
        'Price': [320000]
    })

    mock_engine = MagicMock()
    mock_create_engine.return_value = mock_engine

    # Mock to_sql agar tidak benar-benar konek DB
    with patch.object(df, 'to_sql') as mock_to_sql:
        load_to_postgres(
            df,
            "postgresql://user:password@localhost:5432/testdb"
        )

        # Pastikan create_engine dipanggil
        mock_create_engine.assert_called_once()

        # Pastikan to_sql dipanggil
        mock_to_sql.assert_called_once_with(
            'fashion_products',
            mock_engine,
            if_exists='replace',
            index=False
        )


# =========================
# TEST LOAD GOOGLE SHEETS
# =========================
@patch('utils.load.gspread.authorize')
@patch('utils.load.ServiceAccountCredentials.from_json_keyfile_name')
def test_load_to_gsheets(mock_creds, mock_authorize):
    df = pd.DataFrame({
        'Title': ['Jacket'],
        'Price': [500000]
    })

    # Mock credentials
    mock_credentials = MagicMock()
    mock_creds.return_value = mock_credentials

    # Mock service sheets
    mock_service = MagicMock()
    mock_authorize.return_value = mock_service

    # Mock API chain
    mock_update = (
        mock_service.spreadsheets()
        .values()
        .update()
    )

    mock_update.execute.return_value = {}

    # Jalankan fungsi
    load_to_gsheets(
        df,
        spreadsheet_id='dummy_sheet_id',
        range_name='Sheet1!A1'
    )

    # Validasi credential dipanggil
    mock_creds.assert_called_once()

    # Validasi update dipanggil
    mock_service.spreadsheets().values().update.assert_called_once()


# =========================
# TEST ERROR HANDLING CSV
# =========================
@patch('pandas.DataFrame.to_csv')
def test_load_to_csv_exception(mock_to_csv):
    df = pd.DataFrame({
        'Title': ['Error Test']
    })

    # Paksa error
    mock_to_csv.side_effect = Exception("CSV Error")

    # Fungsi tidak boleh crash
    load_to_csv(df, 'error.csv')


# =========================
# TEST ERROR HANDLING POSTGRES
# =========================
@patch('utils.load.create_engine')
def test_load_to_postgres_exception(mock_create_engine):
    df = pd.DataFrame({
        'Title': ['Error DB']
    })

    # Paksa error
    mock_create_engine.side_effect = Exception("DB Error")

    # Fungsi tidak boleh crash
    load_to_postgres(
        df,
        "postgresql://invalid"
    )


# =========================
# TEST ERROR HANDLING GSHEETS
# =========================
@patch('utils.load.ServiceAccountCredentials.from_json_keyfile_name')
def test_load_to_gsheets_exception(mock_creds):
    df = pd.DataFrame({
        'Title': ['Error Sheets']
    })

    # Paksa error
    mock_creds.side_effect = Exception("Google Sheets Error")

    # Fungsi tidak boleh crash
    load_to_gsheets(
        df,
        spreadsheet_id='dummy',
        range_name='Sheet1!A1'
    )