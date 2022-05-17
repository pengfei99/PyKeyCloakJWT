import json

import requests
from keycloak import KeycloakOpenID
from requests.auth import HTTPBasicAuth


class OidcClient:
    def __init__(self, keycloak_server_url, realm_name, client_id, client_secret):
        self.__url = keycloak_server_url
        self.__realm_name = realm_name
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__oidc_client = KeycloakOpenID(server_url=keycloak_server_url, realm_name=realm_name, client_id=client_id,
                                            client_secret_key=client_secret)

    def get_user_token(self, user_name, user_secret):
        return self.__oidc_client.token(user_name, user_secret)

    def get_service_account_token(self):
        payload = "grant_type=client_credentials"
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        endpoint = f"{self.__url}/realms/pengfei-test/protocol/openid-connect/token"
        response = requests.request("POST", endpoint, headers=headers, data=payload,
                                    auth=HTTPBasicAuth(self.__client_id, self.__client_secret))
        oidc_token_str = response.text
        oidc_token = json.loads(oidc_token_str)
        return oidc_token
