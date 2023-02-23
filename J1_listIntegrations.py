import requests
import json


def const():

    # Account-Level API Key - Admin Group
    acct = "x"
    token = "x"

    return [acct, token]


def make_headers(token, acct):

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(token),
        "Jupiterone-Account": acct
    }

    return headers


def make_request(method, url, headers, data):

    if method == "POST":
        r = requests.post(url, headers=headers, json=data, verify=True)
        return r
    else:
        return "method not implemented"


def get_integrations():

    # GraphQL query to get intgrations
    query = """
        query testQuery {
        integrationDefinitions {
        definitions {
            id
            name
            type
            title
        }
        pageInfo {
        endCursor
        hasNextPage
        }
    }
    }
    """

    data = {
        "query": query
    }

    headers = make_headers(const()[1], const()[0])
    r = make_request("POST", "https://graphql.us.jupiterone.io", headers, data)
    rdict = json.loads(r.content.decode('utf-8'))
    return rdict


if __name__ == '__main__':

    # Run GraphQL query to fetch all Active Integrations from J1
    r = get_integrations()
    print(json.dumps(r, indent=1))
