from abc import ABC, abstractmethod

class BaseClass(ABC):
    def __init__(self, url, repo, owner, token):
        self._url = url
        self._repo = repo
        self._owner = owner
        self._token = token
        self._header = self.get_header()
        self._main_url = self.get_main_url()

    def get_header(self):
        headers = {'Authorization': f"Bearer {self._token}"}
        return headers

    def get_main_url(self):
        return f"{self._url}/repos/{self._owner}/{self._repo}"

    @abstractmethod
    def execute(self):
        pass