"""Module for helper class."""
from airflow.models import Variable

def push_variables(variable_keys: list, **kwargs) -> None:
    """
    Dynamically push Airflow Variables into XCom for downstream tasks.
    :param variable_keys: list of key variable that are needed.
    :param kwargs: kwargs.
    :return: None
    """
    for key in variable_keys:
        value = Variable.get(key)
        kwargs["ti"].xcom_push(key=key, value=value)


def get_data_from_xcom(**kwargs) -> list:
    """
    Method used to pull data from XCom for downstream tasks.
    :param kwargs: kwargs.
    :return: list of variables.
    """
    ti = kwargs['ti']
    pat = ti.xcom_pull(task_ids='push_variables', key='pat')
    repo_name = ti.xcom_pull(task_ids='push_variables', key='repo_name')
    user_name = ti.xcom_pull(task_ids='push_variables', key='user_name')
    github_base_url = ti.xcom_pull(task_ids='push_variables', key='GITHUB_BASE_URL')

    return [pat, repo_name, user_name, github_base_url]