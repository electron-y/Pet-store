import json
import os

import requests

from src.assertable_response import AssertableResponse


class Store:

    def __init__(self):
        self.url = os.environ["BASE_URL"]
        self.headers = {'Content-Type': 'application/json'}

    def get_order(self, order_id):
        url = self.url + f"store/order/{order_id}"
        response = requests.get(url=url)
        return AssertableResponse(response)

    def get_inventory(self):
        url = self.url + "store/inventory"
        response = requests.get(url=url)
        return AssertableResponse(response)

    def post_order(self, payload):
        url = self.url + "store/order/"
        response = requests.post(url=url, data=json.dumps(payload), headers=self.headers)
        return AssertableResponse(response)

    def delete_order(self, order_id):
        url = self.url + f"store/order/{order_id}"
        response = requests.delete(url=url)
        return AssertableResponse(response)
