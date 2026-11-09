import pytest

from utils.api_client import ApiClient

BASE_URL = "https://dummyjson.com"

@pytest.fixture
def api_client():
    return ApiClient(BASE_URL)

