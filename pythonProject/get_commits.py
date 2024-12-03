import requests


class GetCommits:
    def __init__(self, url, header):
        self.final_url = f"{url}/commits"
        self.header = header


    def get_commits(self):

        response = requests.get(self.final_url, headers=self.header)
        if response.status_code == 200:
            commits = response.json()
            print("Here are the commits")
            res = [(commit["sha"], commit["commit"]["message"]) for commit in commits]
            print(res)
        else:
            print("Not good")