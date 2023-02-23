import requests

# Account-Level API Key - Admin Group
acct = "x"
token = "x"

headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(token),
        "Jupiterone-Account": acct
        }

r = requests.get("https://api.us.jupiterone.io/entities/4655ea65-f7be-4393-9ff6-98a14b304183/raw-data",
                 headers=headers, verify=True)
print(r.content)

r = requests.get("https://api.us.jupiterone.io/entities/4655ea65-f7be-4393-9ff6-98a14b304183/raw-data-versions",
                 headers=headers, verify=True)
print(r.content)
