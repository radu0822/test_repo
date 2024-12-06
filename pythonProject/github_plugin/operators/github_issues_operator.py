import logging
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from github_plugin.hooks.github_hook import GitHubHook

class GitHubIssuesOperator(BaseOperator):
    @apply_defaults
    def __init__(self, repository: str, filters: dict = None, conn_id: str = 'github_default', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.repository = repository
        self.filters = filters
        self.conn_id = conn_id


    def execute(self, context):
        hook = GitHubHook(conn_id=self.conn_id)
        endpoint = f"/repos/{self.repository}/issues"
        issues = hook.get_issues(endpoint, params=self.filters)
        context['ti'].xcom_push(key='open_issues', value=issues)
        self.log.info(f"Number of {len(issues)} ")