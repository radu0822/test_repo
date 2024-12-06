import logging
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from github_plugin.hooks.github_hook import GitHubHook

class GitHubBranchesOperator(BaseOperator):
    @apply_defaults
    def __init__(self, repository: str, conn_id: str = 'github_default', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.repository = repository
        self.conn_id = conn_id

    def execute(self, context):
        hook = GitHubHook(conn_id=self.conn_id)
        endpoint = f"/repos/{self.repository}/branches"
        branches = hook.get(endpoint)
        context['ti'].xcom_push(key='branches', value=branches)
        logging.info(f"Number of branches: {len(branches)}")
