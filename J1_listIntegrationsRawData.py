import requests

# Account-Level API Key - Admin Group
acct = "x"
token = "x"

headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(token),
        "Jupiterone-Account": acct
        }

try:
        r = requests.get("https://api.us.jupiterone.io/entities/<ID>/raw-data",
                        headers=headers, verify=True)
        
        print(r.content)

except Exception as e:
        
        print("GET request failed. Exception: {}".format(e))

try:
        r = requests.get("https://api.us.jupiterone.io/entities/<ID>/raw-data-versions",
                        headers=headers, verify=True)

        print(r.content)

except Exception as e:
        
        print("GET request failed. Exception: {}".format(e))
