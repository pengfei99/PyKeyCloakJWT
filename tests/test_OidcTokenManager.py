import pytest

from src.OidcTokenManager import OidcTokenManager


@pytest.fixture
def service_account():
    keycloak_url = "http://localhost:8080"
    realm_name = "pengfei-test"
    client_id = "pengfei-dv-app"
    client_secret = "8BJOcHtXlXpKVLGFOjGoAJ4nxo1WyNKT"
    user_name = "pengfei-dv-app"
    user_secret = "8BJOcHtXlXpKVLGFOjGoAJ4nxo1WyNKT"
    return OidcTokenManager(keycloak_server_url=keycloak_url, realm_name=realm_name, client_id=client_id,
                            client_secret=client_secret, user_name=user_name, user_secret=user_secret)


@pytest.fixture
def custom_account():
    keycloak_url = "http://localhost:8080"
    realm_name = "pengfei-test"
    client_id = "pengfei-dv-app"
    client_secret = "8BJOcHtXlXpKVLGFOjGoAJ4nxo1WyNKT"
    user_name = "pengfei"
    user_secret = "toto"
    return OidcTokenManager(keycloak_server_url=keycloak_url, realm_name=realm_name, client_id=client_id,
                            client_secret=client_secret, user_name=user_name, user_secret=user_secret)


def test_generate_oidc_token_with_custom_account(custom_account):
    token = custom_account.generate_oidc_token()
    print(token)


def test_generate_oidc_token_with_service_account(service_account):
    token = service_account.generate_oidc_token()
    print(token)
