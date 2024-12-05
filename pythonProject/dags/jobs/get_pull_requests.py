import requests
import logging

from jobs.base_class import BaseClass


class GetPullRequests(BaseClass):

    def get_main_url(self):
        return f"{self._url}/repos/{self._owner}/{self._repo}/pulls"

    def execute(self):
        # self.get_main_url()
        logging.info(f"self._main_url : {self._main_url}")
        response = requests.get(self._main_url, headers=self._header)
        if response.status_code == 200:
            result_lst = response.json()
            logging.info("Here are the pull requests")
            logging.info(result_lst)
        else:
            logging.info("Not good")