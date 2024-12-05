import requests
import logging

from jobs.base_class import BaseClass


class GetBranches(BaseClass):

    def get_main_url(self):
        return f"{self._url}/repos/{self._owner}/{self._repo}/branches"

    def execute(self):
        # self.get_main_url()
        logging.info(f"self._main_url : {self._main_url}")
        response = requests.get(self._main_url, headers=self._header)
        if response.status_code == 200:
            result_lst = response.json()
            logging.info("Branches are good!")
            for r in result_lst:
                logging.info(r["name"])
        else:
            logging.info("Branches are nor good!")