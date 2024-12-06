"""Module used to get pull requests."""

import requests
import logging
from jobs.base_class import BaseClass


class GetPullRequests(BaseClass):
    """Class used to get pull requests"""
    def get_main_url(self) -> str:
        """
        Method to override url for pull requests.
        :return: URL for commits
        """
        return f"{self._url}/repos/{self._owner}/{self._repo}/pulls"

    def execute(self) -> None:
        """
        Method to execute the request and get the necessary data.
        :return: None
        """
        logging.info(f"self._main_url : {self._main_url}")
        response = requests.get(self._main_url, headers=self._header)
        if response.status_code == 200:
            result_lst = response.json()
            logging.info("Here are the pull requests")
            for result in result_lst:
                if result["draft"]:
                    logging.info(f"PR : {result['title']} : {result['body']}")
        else:
            logging.info("Not good")