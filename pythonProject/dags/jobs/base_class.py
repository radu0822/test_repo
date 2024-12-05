"""Module for base class."""
from abc import ABC, abstractmethod

class BaseClass(ABC):
    """Class for abstract methods. Class used to get header and url that it is working with."""
    def __init__(self, url, repo, owner, token):
        self._url = url
        self._repo = repo
        self._owner = owner
        self._token = token
        self._header = self.get_header()
        self._main_url = self.get_main_url()

    def get_header(self) -> dict[str, str]:
        """
        Method to get header.
        :return: dictionary that contains the token.
        """
        headers = {'Authorization': f"Bearer {self._token}"}
        return headers

    def get_main_url(self) -> str:
        """
        Method to get main url.
        :return: string that contains the url.
        """
        return f"{self._url}/repos/{self._owner}/{self._repo}"

    @abstractmethod
    def execute(self) -> None:
        """
        Abstract method that is going to be used for writing executnig.
        :return: None.
        """
        pass