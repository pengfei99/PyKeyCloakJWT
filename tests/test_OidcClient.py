import json

import requests
from requests.auth import HTTPBasicAuth


def test_service_account():
    url = "http://localhost:8080/realms/pengfei-test/protocol/openid-connect/token"
    payload = "grant_type=client_credentials"
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    client_id = "pengfei-dv-app"
    client_secret = "8BJOcHtXlXpKVLGFOjGoAJ4nxo1WyNKT"
    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=HTTPBasicAuth(client_id, client_secret))
    oidc_token_str = response.text
    oidc_token = json.loads(oidc_token_str)
    access_token = oidc_token["access_token"]
    print(f"access token: {access_token}")
