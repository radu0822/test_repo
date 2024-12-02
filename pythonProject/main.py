import requests

from const import GITHUB_BASE_URL, user_name, repo_name, pat

repository_url = f"{GITHUB_BASE_URL}/repos/{user_name}/{repo_name}/pulls"


# headers = {
#     'Authorization': f"Bearer {pat}" }

response = requests.get(repository_url)
if response.status_code == 200:
    print(response.json())
    print("Everything is working")
else:
    print("Not working")