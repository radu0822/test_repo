import requests


class GetIssues:
    def __init__(self, url, header):
        self.final_url = f"{url}/issues"
        self.header = header


    def get_commits(self):
        params = {
                'state': 'closed',  # Only fetch open issues
                'per_page': 100,  # Fetch up to 100 issues per page
            }

        respo = requests.get(self.final_url, headers=self.header, params=params)

        if respo.status_code == 200:
            print("Issues are good")
            result_lst = respo.json()
            print(result_lst)
        else:
            print("Issues are not good")
