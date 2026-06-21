# 🎬 Netflix Airflow ETL Project

## 📌 Overview
This project is an end-to-end data engineering pipeline that processes Netflix dataset using Apache Airflow, PostgreSQL, Python, and SQL. It automates data validation, cleaning, and aggregation into analytics-ready tables.

---

## 🏗️ Architecture

Netflix Dataset (PostgreSQL)
        ↓
Apache Airflow (Orchestration)
        ↓
Python (psycopg2)
        ↓
SQL Transformations
        ↓
Analytics Tables

---

## ⚙️ Tech Stack
- Apache Airflow
- Python
- PostgreSQL
- SQL
- psycopg2
- Git & GitHub

---

## 🔄 Pipeline Steps

1. Data Validation (row count check)
2. Data Cleaning (remove null titles)
3. Yearly Aggregation (titles per year)
4. Country Aggregation (titles per country)

---

## 📊 Output Tables
- netflix_clean
- netflix_yearly_summary
- netflix_country_summary

---

## 🚀 How to Run

1. Start PostgreSQL
2. Set environment variable:
```bash
export POSTGRES_PASSWORD="your_password"
Start Airflow:
airflow webserver
airflow scheduler
Trigger DAG:
netflix_etl
👨‍💻 Author

Achintya Vamshi Nudurupati
