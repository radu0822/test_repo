"""This module serves for creation of DAG."""
from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from jobs.airflow_task import (
    get_commits_from_xcom,
    get_issues_from_xcom,
    get_branches_from_xcom,
    get_authentication_from_xcom,
    get_pull_request_from_xcom
)

from jobs.help import push_variables

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2021, 1, 2, 0, 0, 0),
    "email": ["my_email@mail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=1),
}


with DAG("github_api_task", default_args=default_args, schedule_interval=None) as dag:
    push_variables_task = PythonOperator(
        task_id="push_variables",
        python_callable=push_variables,
        op_args=[["pat", "repo_name", "user_name", "GITHUB_BASE_URL"]],
        provide_context=True,
        dag=dag,
    )

    authenticate_to_github = PythonOperator(
        task_id="authenticate_to_github",
        python_callable=get_authentication_from_xcom,
        provide_context=True,
        dag=dag,
    )

    get_pull_requests = PythonOperator(
        task_id="get_pull_requests",
        python_callable=get_pull_request_from_xcom,
        provide_context=True,
        dag=dag,
    )

    get_commits = PythonOperator(
        task_id="get_commits",
        python_callable=get_commits_from_xcom,
        provide_context=True,
        dag=dag,
    )

    get_issues = PythonOperator(
        task_id="get_issues",
        python_callable=get_issues_from_xcom,
        provide_context=True,
        dag=dag,
    )

    get_branches = PythonOperator(
        task_id="get_branches",
        python_callable=get_branches_from_xcom,
        provide_context=True,
        dag=dag,
    )


    push_variables_task >> authenticate_to_github >> get_pull_requests >> get_commits>>get_issues>>get_branches
