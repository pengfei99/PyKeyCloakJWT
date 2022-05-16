import calendar
import time

import pytest

from creds import ssp_token
from src.JwtTokenValidator import JwtTokenValidator


@pytest.fixture
def token_validator():
    return JwtTokenValidator()


def test_is_expired(token_validator):
    actual_val = token_validator.is_expired(ssp_token)
    assert actual_val == False


def test_get_current_unix_ts(token_validator):
    expected_ts = calendar.timegm(time.gmtime())
    actual_ts = token_validator.get_current_unix_ts()
    print(f"expected value: {expected_ts}")
    print(f"actual value: {actual_ts}")
    assert actual_ts == expected_ts
