import requests
import logging

from jobs.base_class import BaseClass


class GetCommits(BaseClass):

    def get_main_url(self):
        return f"{self._url}/repos/{self._owner}/{self._repo}/commits"

    def execute(self):
        logging.info(f"self._main_url : {self._main_url}")
        response = requests.get(self._main_url, headers=self._header)
        if response.status_code == 200:
            commits = response.json()
            logging.info("Here are the commits")
            res = [(commit["sha"], commit["commit"]["message"]) for commit in commits]
            logging.info(res)
        else:
            logging.info("Not good")