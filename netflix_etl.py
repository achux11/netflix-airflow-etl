import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import psycopg2


def run_sql(sql):
    conn = psycopg2.connect(
        host="localhost",
        port=5433,
        database="learning",
        user="postgres",
        password=os.getenv("POSTGRES_PASSWORD")
    )
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


def validate_data():
    run_sql("""
        SELECT COUNT(*)
        FROM netflix_data;
    """)


def create_clean_table():
    run_sql("""
        DROP TABLE IF EXISTS netflix_clean;

        CREATE TABLE netflix_clean AS
        SELECT *
        FROM netflix_data
        WHERE title IS NOT NULL;
    """)


def create_year_summary():
    run_sql("""
        DROP TABLE IF EXISTS netflix_yearly_summary;

        CREATE TABLE netflix_yearly_summary AS
        SELECT
            release_year,
            COUNT(*) AS total_titles
        FROM netflix_clean
        GROUP BY release_year;
    """)


def create_country_summary():
    run_sql("""
        DROP TABLE IF EXISTS netflix_country_summary;

        CREATE TABLE netflix_country_summary AS
        SELECT
            country,
            COUNT(*) AS total_titles
        FROM netflix_clean
        WHERE country IS NOT NULL
        GROUP BY country;
    """)


with DAG(
    dag_id="netflix_etl",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    validate = PythonOperator(
        task_id="validate_data",
        python_callable=validate_data
    )

    clean = PythonOperator(
        task_id="create_clean_table",
        python_callable=create_clean_table
    )

    year_summary = PythonOperator(
        task_id="create_year_summary",
        python_callable=create_year_summary
    )

    country_summary = PythonOperator(
        task_id="create_country_summary",
        python_callable=create_country_summary
    )

    validate >> clean >> year_summary >> country_summary
