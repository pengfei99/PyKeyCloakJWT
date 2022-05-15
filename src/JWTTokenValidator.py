import calendar
import os
import time

from cryptography.hazmat.primitives import serialization
import jwt
from jwt import ExpiredSignatureError
import logging

my_logger = logging.getLogger(__name__)


class JWTTokenValidator:
    DEFAULT_MARGIN = 86400

    def __init__(self, pub_key_path: str = None):
        self.pub_key = pub_key_path

    @staticmethod
    def get_pub_key(pub_key_path):
        if pub_key_path:
            public_key = open(pub_key_path, 'r').read()
            return serialization.load_ssh_public_key(public_key.encode())
        else:
            return None

    def get_valid_token_payload(self, input_token: str) -> dict:
        payload = None
        header = jwt.get_unverified_header(input_token)
        try:
            payload = jwt.decode(
                input_token,
                key=self.pub_key,
                algorithms=[header['alg'], ],
                options={"verify_exp": False
                         }
            )
            my_logger.debug(f"Read token payload: {payload}")
        except ExpiredSignatureError as error:
            my_logger.error(f'Unable to decode the token, error: {error}')
        return payload

    @staticmethod
    def get_invalid_token_payload(input_token: str) -> dict:
        payload = jwt.decode(input_token,
                             options={"verify_signature": False,
                                      "verify_exp": False
                                      }
                             )
        my_logger.debug(f"Read token payload: {payload}")
        return payload

    def is_expired(self, token: str):
        # get expiration margin
        margin = os.getenv("TOKEN_EXP_MARGIN", JWTTokenValidator.DEFAULT_MARGIN)
        # get current timestamp
        current_ts = calendar.timegm(time.gmtime())
        # get token payload
        if self.pub_key:
            payload = self.get_valid_token_payload(token)
        else:
            payload = self.get_invalid_token_payload(token)
        token_expiration = payload["exp"]
        return True if current_ts + margin > token_expiration else False
