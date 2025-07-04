from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print("Hello from Airflow!")

with DAG(dag_id="hello_world", start_date=datetime(2023, 1, 1), schedule="@daily", catchup=False) as dag:
    t1 = PythonOperator(
        task_id="say_hello",
        python_callable=hello,
    )
