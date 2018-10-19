from app.views import product
from app.views import app
import json
import pytest


@pytest.fixture()
def client():
    test_client = app.test_client()
    return test_client


class TestProduct:
    """Testing the product class"""

    def test_create_product(self, client):
        """testing if user can create a product"""

        resp = client.post('/api/v1/products/', content_type="application/json", data=json.dumps({
            "title": "Off-shoulder dress",
            "description": "stripped dress in only two shades(blue,red)",
            "quantity": 4
        }
        ))
        assert resp.status_code == 201

    def test_get_all_products(self, client):
        """testing if user can get all products"""
        resp = client.get('/api/v1/products/', content_type="application/json")
        assert resp.status_code == 200

    def test_get_single_product(self, client):
        """testing if user can get all products"""
        resp = client.get('/api/v1/products/1',
                          content_type="application/json")
        assert resp.status_code == 200
