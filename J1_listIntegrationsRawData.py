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
        r = requests.get("https://api.us.jupiterone.io/entities/4655ea65-f7be-4393-9ff6-98a14b304183/raw-data",
                        headers=headers, verify=True)
        
        print(r.content)

except Exception as e:
        
        print("GET request failed. Exception: {}".format(e))

try:
        r = requests.get("https://api.us.jupiterone.io/entities/4655ea65-f7be-4393-9ff6-98a14b304183/raw-data-versions",
                        headers=headers, verify=True)

        print(r.content)

except Exception as e:
        
        print("GET request failed. Exception: {}".format(e))
