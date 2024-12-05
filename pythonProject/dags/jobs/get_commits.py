"""Module used to get commits."""

import requests
import logging
from jobs.base_class import BaseClass


class GetCommits(BaseClass):
    """Class used to get commits"""
    def get_main_url(self) -> str:
        """
        Method to override url for commits.
        :return: URL for commits
        """
        return f"{self._url}/repos/{self._owner}/{self._repo}/commits"

    def execute(self) -> None:
        """
        Method to execute the request and get the necessary data.
        :return: None
        """
        logging.info(f"self._main_url : {self._main_url}")
        response = requests.get(self._main_url, headers=self._header)
        if response.status_code == 200:
            commits = response.json()
            logging.info("Here are the commits")
            res = [(commit["sha"], commit["commit"]["message"]) for commit in commits]
            for result in res:
                logging.info(result)
        else:
            logging.info("Not good")