"""Module used to get variables from xcom and use this variable for executing the job."""

from jobs.authenticate import Authenticate
from jobs.get_pull_requests import GetPullRequests
from jobs.get_commits import GetCommits
from jobs.get_branches import GetBranches
from jobs.get_issues import GetIssues
from jobs.help import get_data_from_xcom


def get_authentication_from_xcom(**kwargs) -> None:
    """Wrapper to call the get authentication method using XCom values."""
    variables = get_data_from_xcom(**kwargs)
    auth = Authenticate(variables[3], variables[1], variables[2], variables[0])
    auth.execute()



def get_pull_request_from_xcom(**kwargs) -> None:
    """Wrapper to call the get pull requests method using XCom values."""
    variables = get_data_from_xcom(**kwargs)
    pulls = GetPullRequests(variables[3], variables[1], variables[2], variables[0])
    pulls.execute()


def get_commits_from_xcom(**kwargs) -> None:
    """Wrapper to call the get commits method using XCom values."""
    variables = get_data_from_xcom(**kwargs)
    cmt = GetCommits(variables[3], variables[1], variables[2], variables[0])
    cmt.execute()


def get_issues_from_xcom(**kwargs) -> None:
    """Wrapper to call the get issues method using XCom values."""
    variables = get_data_from_xcom(**kwargs)
    issue = GetIssues(variables[3], variables[1], variables[2], variables[0])
    issue.execute()


def get_branches_from_xcom(**kwargs) -> None:
    """Wrapper to call the get branches method using XCom values."""
    variables = get_data_from_xcom(**kwargs)
    branches= GetBranches(variables[3], variables[1], variables[2], variables[0])
    branches.execute()