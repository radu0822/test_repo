"""Module used to get authenticated."""

import requests
import logging
from jobs.base_class import BaseClass


class Authenticate(BaseClass):
    """Class used to get authenticated"""
    def execute(self) -> None:
        """
        Method to execute the request and get the necessary data.
        :return: None
        """
        logging.info(f"self._main_url : {self._main_url}")
        response = requests.get(self._main_url, headers=self._header)
        if response.status_code == 200:
            logging.info("All good, you are authenticated")
        else:
            logging.info(f"Authentication failed. Status code: {response.status_code}")
