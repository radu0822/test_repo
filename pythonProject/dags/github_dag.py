"""This module serves for creation of DAG."""
from datetime import timedelta, datetime
from airflow import DAG

from github_plugin.operators.github_auth_operator import GitHubAuthOperator
from github_plugin.operators.github_branches_operator import GitHubBranchesOperator
from github_plugin.operators.github_commits_operator import GitHubCommitsOperator
from github_plugin.operators.github_issues_operator import GitHubIssuesOperator
from github_plugin.operators.github_pull_requests_operator import GitHubPullRequestsOperator

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


with DAG("github_api_task_dag", default_args=default_args, schedule_interval=None) as dag:
    auth = GitHubAuthOperator(task_id="authenticate")

    wip_prs = GitHubPullRequestsOperator(
        task_id="draft_pull_requests",
        repository='user/repo')

    commits = GitHubCommitsOperator(
        task_id="commits",
        repository='user/repo',
        branch='main'
    )

    issues = GitHubIssuesOperator(
        task_id="issues",
        repository="user/repo",
        filters={'labels': 'bug'}
    )

    branches = GitHubBranchesOperator(
        task_id="branches",
        repository="user/repo"
    )


    auth >> wip_prs >> commits >> issues >> branches