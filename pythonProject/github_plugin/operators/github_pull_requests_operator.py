import logging
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from github_plugin.hooks.github_hook import GitHubHook

class GitHubPullRequestsOperator(BaseOperator):

    @apply_defaults
    def __init__(self, repository, conn_id='github_default', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.repository = repository
        self.conn_id = conn_id


    def execute(self, context):
        hook = GitHubHook(conn_id=self.conn_id)
        endpoint = f"/repos/{self.repository}/pulls"
        pulls = hook.get(endpoint, {"state" : "open", "draft" : "true"})
        context["ti"].xcom_push(key='wip_pull_requests', values=pulls)
        logging.info(f"Pull {len(pulls)} pull requests")