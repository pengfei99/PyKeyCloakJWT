from keycloak import KeycloakOpenID


class JwtTokenManager:
    def __init__(self, keycloak_server_url: str, realm_name: str, client_id: str, client_secret: str, user_name: str,
                 user_secret: str):
        self.__url = keycloak_server_url
        self.__realm_name = realm_name
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__user_name = user_name
        self.__user_secret = user_secret
        self.oidc_client = KeycloakOpenID(server_url=keycloak_server_url, realm_name=realm_name, client_id=client_id,
                                          client_secret_key=client_secret)

    def generate_oidc_token(self,):
        self.oidc_client.token(self.__user_name, self.__user_secret)

    def get_access_token(self,oidc_token):


    def refresh_oidc_token
