import requests
import logging

from jobs.base_class import BaseClass


class GetIssues(BaseClass):

    def get_main_url(self):
        return f"{self._url}/repos/{self._owner}/{self._repo}/issues"

    def execute(self):
        # self.get_main_url()
        logging.info(f"self._main_url : {self._main_url}")
        params = {
                'state': 'open',
                'per_page': 100,
            }
        respo = requests.get(self._main_url, headers=self._header, params=params)

        if respo.status_code == 200:
            logging.info("Issues are good")
            result_lst = respo.json()
            logging.info(result_lst)
        else:
            logging.info("Issues are not good")
