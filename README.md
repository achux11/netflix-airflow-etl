# 🎬 Netflix Data Engineering Pipeline (Airflow + PostgreSQL)

## 🚀 Overview
This project implements a production-style data engineering pipeline using Apache Airflow, PostgreSQL, Python, and SQL to process and transform a Netflix dataset into analytics-ready tables.

The pipeline simulates a real-world ETL workflow used in modern data platforms for batch processing and reporting systems.

---

## 🏗️ System Architecture

```text
Raw Data Layer: netflix_data in PostgreSQL
        ↓
Orchestration Layer: Apache Airflow DAG
        ↓
Processing Layer: Python + psycopg2
        ↓
Transformation Layer: SQL cleaning and aggregation
        ↓
Analytics Layer: PostgreSQL summary tables
🔄 End-to-End Data Flow
netflix_data
        ↓
validate_data
        ↓
netflix_clean
        ↓
netflix_yearly_summary
        ↓
netflix_country_summary
⚙️ Tech Stack
Apache Airflow
PostgreSQL
Python
SQL
psycopg2
Git & GitHub
🧠 Key Engineering Concepts
Airflow DAG orchestration
ETL pipeline design
SQL-based transformations
Modular Python functions
Environment-based secret handling
Analytics-ready data modeling
🧪 Airflow DAG Structure
validate_data
      ↓
create_clean_table
      ↓
create_year_summary
      ↓
create_country_summary
📊 Output Tables
netflix_clean
netflix_yearly_summary
netflix_country_summary
💡 Business Impact

This pipeline enables automated analysis of Netflix content trends such as yearly content growth and country-level distribution.

🚀 How to Run
1. Start PostgreSQL

Make sure PostgreSQL is running locally on port 5433.

2. Set environment variable
export POSTGRES_PASSWORD="your_password"
3. Start Airflow
airflow webserver
airflow scheduler
4. Trigger DAG

Trigger this DAG in the Airflow UI:

netflix_etl
👨‍💻 Author

Achintya Vamshi Nudurupati
eof
