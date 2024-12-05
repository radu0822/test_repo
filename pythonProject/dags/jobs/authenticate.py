import requests
import logging

from jobs.base_class import BaseClass


class Authenticate(BaseClass):

    def execute(self):
        logging.info(f"self._main_url : {self._main_url}")
        response = requests.get(self._main_url, headers=self._header)
        if response.status_code == 200:
            logging.info("All good, you are authenticated")
        else:
            logging.info(f"Authentication failed. Status code: {response.status_code}")
