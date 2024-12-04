import requests


class GetPullRequests:
    def __init__(self, url, header):
        self.final_url = f"{url}/pulls"
        self.header = header


    def get_pull_requests(self):

        response = requests.get(self.final_url, headers=self.header)
        if response.status_code == 200:
            result_lst = response.json()
            print("Here are the pull requests")
            print(result_lst)
        else:
            print("Not good")