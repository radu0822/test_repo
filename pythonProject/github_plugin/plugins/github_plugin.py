from airflow.plugins_manager import AirflowPlugin
from github_plugin.hooks.github_hook import GitHubHook
from github_plugin.operators.github_auth_operator import GitHubAuthOperator
from github_plugin.operators.github_branches_operator import GitHubBranchesOperator
from github_plugin.operators.github_commits_operator import GitHubCommitsOperator
from github_plugin.operators.github_issues_operator import GitHubIssuesOperator
from github_plugin.operators.github_pull_requests_operator import GitHubPullRequestsOperator


class GitHubPlugin(AirflowPlugin):
    name = "github_plugin"
    hooks = [GitHubHook]
    operators = [
        GitHubAuthOperator,
        GitHubPullRequestsOperator,
        GitHubCommitsOperator,
        GitHubIssuesOperator,
        GitHubBranchesOperator,
    ]