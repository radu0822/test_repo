import requests
from airflow.hooks.base_hook import BaseHook


class GitHubHook(BaseHook):
    def __init__(self, conn_id: str = "github_default"):
        self.conn_id = conn_id
        self.session = self._get_session()


    def _get_session(self):
        conn = self.get_connection(self.conn_id)
        if not conn.password:
            raise ValueError(f"Connection {self.conn_id} must have a valid token in the password field.")

        token = conn.password
        session = requests.Session()
        session.headers.update({
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
        })
        return session


    def get(self, endpoint: str, params: dict = None):
        url = f"https://api.github.com/{endpoint}"
        response = self.session.get(url, params=params)
        if response.status_code != 200 and "X-RateLimit-Remaining" in response.headers:
            reset_time = int(response.headers["X-RateLimit-Remaining"])
            raise RuntimeError(f"Rate limit exceed. Retry after {reset_time} seconds.")
        response.raise_for_status()
        return response.json()