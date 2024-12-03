import requests


class Authenticate:
    def __init__(self, url, header):
        self.final_url = f"{url}"
        self.header = header


    def get_authentication(self):

        response = requests.get(self.final_url, headers=self.header)
        if response.status_code == 200:
            print("All good, you are authenticated")
        else:
            print("Not good")
