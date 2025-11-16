import pytest
import random

class TestCreateItem:
    
    def test_success_item_creation(self, api_client, api_url, test_data):
        response = api_client.post(f"{api_url}/api/1/item", json=test_data)
        assert response.status_code == 200
    
    def test_invalid_item_creation(self, api_client, api_url):
        data = {
            "sellerId": "invalid_str",
            "name": "Test Item",
            "price": "not_num",
            "statistics": {
                "likes": 5,
                "viewCount": 100,
                "contacts": 3
            }
        }
        response = api_client.post(f"{api_url}/api/1/item", json=data)
        assert response.status_code == 400

    def test_03_empty_item_creation(self, api_client, api_url):
        response = api_client.post(f"{api_url}/api/1/item", json={})
        assert response.status_code == 400

    def test_create_item_without_seller_id(self, api_client, api_url):
        data = {
            "name": "Test Item",
            "price": 1000,
            "statistics": {
                "likes": 5,
                "viewCount": 100,
                "contacts": 3
            }
        }
        response = api_client.post(f"{api_url}/api/1/item", json=data)
        assert response.status_code == 400


class TestGetItemById:
    
    def test_get_item_success(self, api_client, api_url, random_seller_id):
        data = {
            "sellerId": random_seller_id,
            "name": "Test Item",
            "price": 1000,
            "statistics": {
                "likes": 5,
                "viewCount": 100,
                "contacts": 3
            }
        }
        post_response = api_client.post(f"{api_url}/api/1/item", json=data)
        
        if post_response.status_code == 200:
            item_id = post_response.json()['status'].split(' - ')[1]
            get_response = api_client.get(f"{api_url}/api/1/item/{item_id}")
            assert get_response.status_code == 200

    def test_get_not_existed_item(self, api_client, api_url):
        response = api_client.get(f"{api_url}/api/1/item/not_existed_id")
        assert response.status_code == 400

    def test_get_item_with_invalid_id(self, api_client, api_url):
        response = api_client.get(f"{api_url}/api/1/item/invalid_id")
        assert response.status_code == 400


class TestGetItemsBySeller:
    
    def test_get_items_by_seller_id_success(self, api_client, api_url, random_seller_id):
        seller_id = random_seller_id
        response = api_client.get(f"{api_url}/api/1/{seller_id}/item")
        assert response.status_code == 200

    def test_get_items_not_existed_seller_id(self, api_client, api_url):
        seller_id = 1000
        response = api_client.get(f"{api_url}/api/1/{seller_id}/item")
        assert response.status_code == 200

    def test_get_items_with_invalid_seller_id(self, api_client, api_url):
        response = api_client.get(f"{api_url}/api/1/invalid_seller_id/item")
        assert response.status_code == 400


class TestGetStatistics:
    
    def test_get_statistics_success(self, api_client, api_url, random_seller_id):
        data = {
            "sellerId": random_seller_id,
            "name": "Test Item",
            "price": 1000,
            "statistics": {
                "likes": 5,
                "viewCount": 100,
                "contacts": 3
            }
        }
        post_responce = api_client.post(f"{api_url}/api/1/item", json=data)
        
        if post_responce.status_code == 200:
            item_id = post_responce.json()['status'].split(' - ')[1]
            get_response = api_client.get(f"{api_url}/api/1/statistic/{item_id}")
            assert get_response.status_code == 200

    def test_get_statistics_not_existed_item(self, api_client, api_url):
        response = api_client.get(f"{api_url}/api/1/statistic/not_existed")
        assert response.status_code == 400