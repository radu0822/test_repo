import requests

GITHUB_BASE_URL = 'https://api.github.com'
user_name = 'radu0822'
repo_name = 'test_repo'

repository_url = f"{GITHUB_BASE_URL}/repos/{user_name}/{repo_name}/pulls"

pat = "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"

headers = {
    'Authorization': f"Bearer {pat}" }

response = requests.get(repository_url, headers=headers)
if response.status_code == 200:
    print(response.json())
    print("Everything is working")
else:
    print("Not working")