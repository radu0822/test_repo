import logging
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from github_plugin.hooks.github_hook import GitHubHook

class GitHubCommitsOperator(BaseOperator):
    @apply_defaults
    def __init__(self,
                 repository: str,
                 branch:str = "main",
                 conn_id="github_default", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.repository = repository
        self.branch = branch
        self.conn_id = conn_id


    def execute(self, context):
        hook = GitHubHook(conn_id=self.conn_id)
        endpoint = f"/repos/{self.repository}/commits"
        commits = hook.get(endpoint, {"sha": self.branch})
        context["ti"].xcom_push(key='latest', values=commits)
        logging.info(f"Number of commit : {len(commits)}")
