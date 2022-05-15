import pytest

from creds import ssp_token
from src.JWTTokenValidator import JWTTokenValidator


def test_is_expired():
    validator = JWTTokenValidator()
    actual_val = validator.is_expired(ssp_token)
    assert actual_val == False
