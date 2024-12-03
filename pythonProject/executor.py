import os

from authenticate import Authenticate
from get_branches import GetBranches
from get_commits import GetCommits
from get_issues import GetIssues
from get_pull_requests import GetPullRequests


class Executor:
    def __init__(self):
        self._url = os.getenv('GITHUB_BASE_URL')
        self._repo = os.getenv('repo_name')
        self._owner = os.getenv('user_name')
        self._token = os.getenv('pat')
        self._header = self.get_header()
        self._main_url = self.get_main_url()


    def get_main_url(self):
        return f"{self._url}/repos/{self._owner}/{self._repo}"

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, new_value : str):
        self._url = new_value

    @property
    def header(self):
        return self._header


    def get_header(self):
        headers = {'Authorization':
                       f"Bearer {os.getenv('pat')}" }
        return headers

    def execute(self):

        auth = Authenticate(self._main_url, self.header)
        auth.get_authentication()
        
        pr = GetPullRequests(self._main_url, self.header)
        pr.get_pull_requests()

        commit = GetCommits(self._main_url, self.header)
        commit.get_commits()

        issues = GetIssues(self._main_url, self.header)
        issues.get_commits()

        branches = GetBranches(self._main_url, self.header)
        branches.get_branches()