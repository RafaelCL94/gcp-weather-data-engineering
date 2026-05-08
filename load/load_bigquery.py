import pandas as pd
from google.cloud import bigquery

PROJECT_ID = "gcp-weather-data-engineering"
DATASET = "weather"
TABLE = "weather_history"

CSV_PATH = "data/processed/weather_history.csv"

client = bigquery.Client(project=PROJECT_ID)

table_id = f"{PROJECT_ID}.{DATASET}.{TABLE}"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=False,
    write_disposition="WRITE_APPEND"
)

with open(CSV_PATH, "rb") as source_file:
    job = client.load_table_from_file(
        source_file,
        table_id,
        job_config=job_config
    )

job.result()

print("Carga concluída no BigQuery")