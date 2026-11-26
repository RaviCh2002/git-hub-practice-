
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def hello_world():
    print("Hello from Google Cloud Composer!")
    print("My first Airflow DAG executed successfully.")


with DAG(
    dag_id="hello_world_dag",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["demo"],
) as dag:

    hello_task = PythonOperator(
        task_id="hello_task",
        python_callable=hello_world,
    )
