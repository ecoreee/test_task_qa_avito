import pytest
import requests
import random

@pytest.fixture
def api_client():
    session = requests.Session()
    session.headers.update({'Content-Type': 'application/json'})
    return session

@pytest.fixture
def api_url():
    return "https://qa-internship.avito.com"

@pytest.fixture
def random_seller_id():
    return random.randint(111111, 999999)

@pytest.fixture
def test_data(random_seller_id):
    return {
        "sellerId": random_seller_id,
        "name": f"Test Item {random.randint(1000, 10000)}",
        "price": 1000,
        "statistics": {
            "likes": 5,
            "viewCount": 100,
            "contacts": 3
        }
    }