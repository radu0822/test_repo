"""Module used to get issues."""

import requests
import logging
from jobs.base_class import BaseClass


class GetIssues(BaseClass):
    """Class used to get issues"""
    def get_main_url(self) -> str:
        """
        Method to override url for issues.
        :return: URL for commits
        """
        return f"{self._url}/repos/{self._owner}/{self._repo}/issues"

    def execute(self) -> None:
        """
        Method to execute the request and get the necessary data.
        :return: None
        """
        logging.info(f"self._main_url : {self._main_url}")
        params = {
                'state': 'open',
                'per_page': 100,
            }
        respo = requests.get(self._main_url, headers=self._header, params=params)

        if respo.status_code == 200:
            logging.info("Issues are good")
            result_lst = respo.json()
            for result in result_lst:
                logging.info(f"Issue : {result['title']} : {result['body']}")
        else:
            logging.info("Issues are not good")
