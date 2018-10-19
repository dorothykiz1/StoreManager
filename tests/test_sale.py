from app.views import sale
from app.views import app

import json
import pytest


@pytest.fixture()
def client():
    test_client = app.test_client()
    return test_client


class TestSale:
    """Testing the sales class"""

    def test_create_new_sale(self, client):
        """testing if asale attendant can create a sale record"""
        resp = client.post('/api/v1/sales/',
                           content_type="application/json",
                           data=json.dumps({
                               "attendant_Id": 234567,
                               "attendant_name": "Kabarozi",
                           }
                           ))
        assert resp.status_code == 201

    def test_get_all_sales(self, client):
        """testing if admin can get all sale records"""
        resp = client.get('/api/v1/sales/', content_type="application/json")
        assert resp.status_code == 200

    def test_get_single_sale_record(self, client):
        """testing if admin/attendant can get asingle sale records"""
        resp = client.get('/api/v1/sales/1',
                          content_type="application/json")
        assert resp.status_code == 200
