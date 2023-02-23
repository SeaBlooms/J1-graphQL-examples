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


def run_query(q):

    query = '''
        query J1QL($query: String!, $variables: JSON, $cursor: String, $scopeFilters: [JSON!], $flags: QueryV1Flags) {
      queryV1(query: $query, variables: $variables, cursor: $cursor, scopeFilters: $scopeFilters, flags: $flags) {
        type
        data
        cursor
      }
    }
        '''

    data = {
        "query": query,
        "variables": {
            "query": q
        }
    }

    headers = make_headers(const()[1], const()[0])
    r = make_request("POST", "https://graphql.us.jupiterone.io", headers, data)
    rdict = json.loads(r.content.decode('utf-8'))
    return rdict


def create_entity():

    query = '''
    mutation CreateEntity (
    $entityK    ey: String!
    $entityType: String!
    $entityClass: [String!]!
    $timestamp: Long
    $properties: JSON
    ) {
    createEntity (
        entityKey: $entityKey,
        entityType: $entityType,
        entityClass: $entityClass,
        timestamp: $timestamp,
        properties: $properties
    ) {
        entity {
        _id
        }
        vertex {
        id,
        entity {
            _id
        }
        properties
        }
    }
    }
    '''

    data = {
        "query": query,
        "variables": {
            "entityKey": "graphQL Device 1",
            "entityType": "custom_device",
            "entityClass": "Device",
            "properties": {
                "propertyKey": "propertyValue",
                "displayName": "graphQL Device Upload 1",
                "owner": "upload.user@jupiterone.com",
                "customProperty": "graphQL-updated-value",
                "tag.Production": "false"
                }
            }
    }

    headers = make_headers(const()[1], const()[0])
    r = make_request("POST", "https://graphql.us.jupiterone.io", headers, data)
    rdict = json.loads(r.content.decode('utf-8'))
    return rdict


def get_assets():
    # GraphQL query to get alerts
    query = '''
            query J1QL($query: String!, $variables: JSON, $cursor: String, $scopeFilters: [JSON!], $flags: QueryV1Flags) {
          queryV1(query: $query, variables: $variables, cursor: $cursor, scopeFilters: $scopeFilters, flags: $flags) {
            type
            data
            cursor
          }
        }
            '''

    data = {
        "query": query,
        "variables": {
            "query": "FIND (Device | Host)"
        }
    }

    headers = make_headers(const()[1], const()[0])
    r = make_request("POST", "https://graphql.us.jupiterone.io", headers, data)
    rdict = json.loads(r.content.decode('utf-8'))
    return rdict


if __name__ == '__main__':

    # Execute GraphQL Query
    # query = "FIND Device"
    # r = run_query(query)
    # print(json.dumps(r, indent=1))

    # Create/Update Entity via GraphQL
    # r = create_entity()
    # print(json.dumps(r, indent=1))

    # Run GraphQL query to fetch all Device & Host entities from J1
    r = get_assets()
    print(json.dumps(r, indent=1))
