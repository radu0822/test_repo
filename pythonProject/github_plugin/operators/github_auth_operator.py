import logging
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from github_plugin.hooks.github_hook import GitHubHook


class GitHubAuthOperator(BaseOperator):
    @apply_defaults
    def __init__(self, conn_id: str = 'github_default', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conn_id = conn_id

    def execute(self, context):
        hook = GitHubHook(conn_id=self.conn_id)
        user_data = hook.get("/user")
        logging.info(f"user data: {user_data}")