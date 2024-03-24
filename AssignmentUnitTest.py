import unittest
import requests
import os
from datetime import datetime

class TestAPIEndpoints(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:5000"
        self.test_results_folder = "test_results"
        if not os.path.exists(self.test_results_folder):
            os.makedirs(self.test_results_folder)

    def tearDown(self):
        pass

    def test_getProducts(self):
        url = self.base_url + "/getProducts"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_getTitles(self):
        url = self.base_url + "/getTitles"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_insertProduct(self):
        url = self.base_url + "/insertProduct"
        params = {'api_key': 'custom_api_key'}
        data = {
            "ProductId": "123",
            "Title": "Test Product",
            "Price": 10.99,
            "Quantity": 100
        }
        response = requests.post(url, json=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_apiDescription(self):
        url = self.base_url + "/"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    test_results_folder = "test_results"
    if not os.path.exists(test_results_folder):
        os.makedirs(test_results_folder)
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    test_results_file = os.path.join(test_results_folder, f"test_results_{now}.txt")
    with open(test_results_file, 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        unittest.main(testRunner=runner)