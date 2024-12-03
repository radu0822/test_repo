import requests


class GetBranches:
    def __init__(self, url, header):
        self.final_url = f"{url}/branches"
        self.header = header


    def get_branches(self):

        response = requests.get(self.final_url, headers=self.header)
        if response.status_code == 200:
            result_lst = response.json()
            print("Branches are good!")
            for r in result_lst:
                print(r["name"])
        else:
            print("Branches are nor good!")