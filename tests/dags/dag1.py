from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def test_function():
    print("hello world python")

my_dag = DAG(
    'dag1',
    start_date=datetime(2024, 2, 1),
    schedule='* * * * *',
    catchup=False,
)

python_task = PythonOperator(
    dag=my_dag,
    task_id='python_task',
    python_callable=test_function,
)
