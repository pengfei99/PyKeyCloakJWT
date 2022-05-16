import logging

from keycloak import KeycloakOpenID

from src.JwtTokenValidator import JwtTokenValidator

my_logger = logging.getLogger(__name__)


class OidcTokenManager:
    def __init__(self, keycloak_server_url: str, realm_name: str, client_id: str, client_secret: str, user_name: str,
                 user_secret: str):
        self.__url = keycloak_server_url
        self.__realm_name = realm_name
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__user_name = user_name
        self.__user_secret = user_secret
        self.__oidc_client = KeycloakOpenID(server_url=keycloak_server_url, realm_name=realm_name, client_id=client_id,
                                            client_secret_key=client_secret)
        self.oidc_token = self.generate_oidc_token()
        self.__jwt_token_validator = JwtTokenValidator()

    def generate_oidc_token(self, ) -> dict:
        """
        This method connect to a keycloak server, and generate an oidc token
        :return:
        """
        return self.__oidc_client.token(self.__user_name, self.__user_secret)

    def get_current_access_token(self, ) -> str:
        """
        This method returns the access token of current oidc token
        :return: str
        """
        return self.oidc_token["access_token"]

    def renew_oidc_token(self, ) -> bool:
        """
        This method will check if the current token is expired or not. If expired, then generate a new token and return
        True. Otherwise, do nothing and return false
        :return: bool
        """
        # if current token is expired, ask a new one from the keycloak server
        if self.__jwt_token_validator.is_expired(self.get_current_access_token()):
            my_logger.info("Current token is expired, generate a new token")
            self.oidc_token = self.generate_oidc_token()
            return True
        else:
            my_logger.info("Current token is still valid.")
            return False
