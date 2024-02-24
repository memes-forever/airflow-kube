from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from time import sleep


DAGS_ID_PREFIX = 'SLEEP'
DAGS_COUNT = 20
TASK_ID_PREFIX = 'TASK'
TASK_COUNT = 100
SLEEP_TIME = 10


def test_function_sleep(sec=SLEEP_TIME):
    print("start")
    sleep(sec)
    print("end")


for di in range(DAGS_COUNT):
    with DAG(
        f"{DAGS_ID_PREFIX}_{di}",
        start_date=datetime(2024, 2, 1),
        schedule='* * * * *',
        catchup=True,
        max_active_runs=2,
        max_active_tasks=20,
    ):
        for ti in range(TASK_COUNT):
            python_task = PythonOperator(
                task_id=f"{TASK_ID_PREFIX}_{ti}",
                python_callable=test_function_sleep,
            )
