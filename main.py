import json

"""
followers:
People who follow you.
followings:
People you currently follow.
followRequests:
People you requested but they haven’t accepted yet.
"""


followersFile = "followers_file.json"
followingRequestsFile = "followingRequests_file.json"

#----followers script
followers = set ()
with open(followersFile, 'r') as File:
    followersFile = json.load(File)

for i in followersFile:
    followers.add(i["string_list_data"][0]["value"])

#----following requests script
followRequests = set ()
with open(followingRequestsFile, 'r') as File:
    followingRequestsFile = json.load(File)

print("Accounts that aren't following back:")
for i in followingRequestsFile["relationships_permanent_follow_requests"]:
    followRequests.add(i["string_list_data"][0]["value"])

#----final
final = followRequests-followers

for i,user in enumerate(sorted(final),start=1):
    print(f"{i}){user}")
