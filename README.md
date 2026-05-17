# Fashion ETL Pipeline

Proyek ini merupakan implementasi sederhana proses **ETL (Extract, Transform, Load)** menggunakan Python.  
Pipeline ini melakukan scraping data produk fashion dari website, membersihkan data, lalu menyimpannya ke beberapa target seperti CSV, PostgreSQL, dan Google Sheets.

---

## Features

- Web Scraping 50 halaman website
- Data Cleaning & Transformation
- Export ke CSV
- Load ke PostgreSQL
- Load ke Google Sheets
- Unit Testing menggunakan Pytest
- Mock Testing API Request
- Error Handling pada setiap tahapan ETL
- Test Coverage 100%

---

## Tech Stack

- Python
- Pandas
- BeautifulSoup4
- Requests
- PostgreSQL
- SQLAlchemy
- Google Sheets API
- Pytest

---

## Project Structure

```bash
fashion-etl-pipeline/
│
├── utils/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ETL Process

### 1. Extract
Melakukan web scraping dari website target sebanyak 50 halaman menggunakan `requests` dan `BeautifulSoup`.

### 2. Transform
Melakukan pembersihan data:
- Menghapus invalid data
- Menghapus duplicate data
- Konversi harga USD ke Rupiah
- Konversi tipe data
- Menambahkan timestamp

### 3. Load
Menyimpan data hasil transformasi ke:
- CSV
- PostgreSQL
- Google Sheets

---

## Installation

Clone repository:

```bash
git clone https://github.com/username/fashion-etl-pipeline.git
cd fashion-etl-pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
python main.py
```

---

## Run Testing

```bash
pytest tests/
```

Coverage testing:

```bash
pytest --cov=utils tests/
```

---

## Output

Dataset hasil ETL memiliki:
- 1000 raw data hasil scraping
- 867 clean data setelah transformasi

---

## Notes

Sebelum menjalankan Google Sheets integration, tambahkan file credential:

```bash
google-sheets-api.json
```

dan sesuaikan:
- Spreadsheet ID
- PostgreSQL connection string

pada file `main.py`.

---

## Author

Satrio Budi Pratama