from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from time import sleep


DAGS_ID_PREFIX = 'SLEEP'
DAGS_COUNT = 10
TASK_ID_PREFIX = 'TASK'
TASK_COUNT = 10
SLEEP_TIME = 10


def test_function_sleep(sec=SLEEP_TIME):
    print("start")
    sleep(sec)
    print("end")


for di in range(DAGS_COUNT):
    my_dag = DAG(
        f"{DAGS_ID_PREFIX}_{di}",
        start_date=datetime(2024, 2, 1),
        schedule='* * * * *',
        catchup=False,
    )
    for ti in range(TASK_COUNT):
        python_task = PythonOperator(
            dag=my_dag,
            task_id=f"{TASK_ID_PREFIX}_{di}",
            python_callable=test_function_sleep,
        )
