import unittest
import json
from app.views.product import app


class TestProduct(unittest.TestCase):
    """This class represents the Product Test Case"""

    def setUp(self):
        """Defining Test Variables"""
        self.client = app.test_client()
        self.product = {
            "title": "Stylish off shoulder dress",
            "description": "Short, Blue Off shoulder dress for ages between 2 and 3 Years old",
            "quantity": 4,
            "price": 23000
        }

    def test_create_product(self):
        """Test a POST request for CREATING A PRODUCT"""
        response = self.client.post(
            '/api/v1/products', data=json.dumps(self.product))
        self.assertIn("Stylish off shoulder dress", str(response.data))
        # self.assertEqual(response.status_code, 201)


if __name__ == "__main__":
    unittest.main()
