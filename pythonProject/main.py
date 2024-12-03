import requests




# # result_lst = []

# #
# response = requests.get(repository_url_to_get_pulls, headers=headers)
# if response.status_code == 200:
#     result_lst = response.json()
#     print(result_lst)
#     for r in result_lst:
#         if r["draft"]:
#             print(r["title"])
#     print("Everything is working")
# else:
#     print("Not working")



# Commit

# params = {"sha": "test_pr"}
# respo = requests.get(repository_url_to_get_commits, params=params, headers=headers)
# res = []
# if respo.status_code == 200:
#     commits = respo.json()
#     print(commits)
#     res = [(commit["sha"], commit["commit"]["message"]) for commit in commits]
#
#
# print(res)




# Issues

params = {
        'state': 'open',  # Only fetch open issues
        'per_page': 100,  # Fetch up to 100 issues per page
    }

respo = requests.get(repository_url_to_get_issues, headers=headers, params=params)

if respo.status_code == 200:
    result_lst = respo.json()

for r in result_lst:
    print(r)