from datetime import datetime

from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import (
    GCSToBigQueryOperator,
)

# Update this value to the name of the bucket where employee.csv is uploaded.
GCS_BUCKET = "gs://1st_bucket1234"

# BigQuery destination: project.dataset.table
BIGQUERY_TABLE = (
    "my-project-ravi007.employee_dataset.employee_details"
)

with DAG(
    dag_id="employee_gcs_to_bigquery",
    description="Load employee CSV from Cloud Storage into BigQuery",
    start_date=datetime(2026, 1, 1),
    schedule=None,  # Trigger manually from the Airflow UI
    catchup=False,
    tags=["employee", "gcs", "bigquery"],
) as dag:

    load_to_bigquery = GCSToBigQueryOperator(
        task_id="load_to_bigquery",
        bucket=GCS_BUCKET,
        source_objects=["employee.csv"],
        destination_project_dataset_table=BIGQUERY_TABLE,
        source_format="CSV",
        skip_leading_rows=1,
        autodetect=True,
        write_disposition="WRITE_TRUNCATE",
        create_disposition="CREATE_IF_NEEDED",
    )
