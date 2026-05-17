# ✨ Fashion ETL Pipeline

<div align="center">

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data-purple?logo=pandas)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-DB-blue?logo=postgresql)
![Pytest](https://img.shields.io/badge/Pytest-Testing-green?logo=pytest)
![Coverage](https://img.shields.io/badge/Coverage-100%25-success)

Simple ETL pipeline project for scraping, cleaning, and storing fashion product data.

</div>

---

## 📌 Overview

This project implements an end-to-end **ETL (Extract, Transform, Load)** pipeline using Python.

### Workflow

```text
Extract → Transform → Load
```

* Scrape data from 50 pages
* Clean and validate data
* Convert USD to IDR
* Store data into CSV, PostgreSQL, and Google Sheets
* Test using Pytest + Mock Testing

---

## ⚙️ Tech Stack

| Tools             | Purpose                 |
| ----------------- | ----------------------- |
| Python            | Main language           |
| Pandas            | Data processing         |
| BeautifulSoup     | Web scraping            |
| PostgreSQL        | Database                |
| SQLAlchemy        | Database connector      |
| Google Sheets API | Spreadsheet integration |
| Pytest            | Unit testing            |

---

## 📂 Structure

```bash
fashion-etl-pipeline/
├── utils/
├── tests/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ Run Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run ETL:

```bash
python main.py
```

Run testing:

```bash
pytest --cov=utils tests/
```

---

## 📊 Result

| Stage      | Total |
| ---------- | ----- |
| Raw Data   | 1000  |
| Clean Data | 867   |

---

## 🧠 Key Features

✅ Web Scraping
✅ Data Cleaning
✅ Error Handling
✅ Currency Conversion
✅ Timestamp Column
✅ PostgreSQL Integration
✅ Google Sheets Integration
✅ Mock Testing
✅ 100% Coverage

---

## 👨‍💻 Author

**Satrio Budi Pratama**

Currently exploring:

* Data Engineering
* Data Science
* Machine Learning
* AI Engineering

---

<div align="center">

⭐ Building projects > only watching tutorials

</div>
