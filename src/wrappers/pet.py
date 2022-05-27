import json
import os

import requests

from src.assertable_response import AssertableResponse


class Pet:

    def __init__(self):
        self.url = os.environ["BASE_URL"]
        self.headers = {'Content-Type': 'application/json'}

    def get_pet_by_id(self, pet_id):
        url = self.url + f"pet/{pet_id}"
        response = requests.get(url=url)
        return AssertableResponse(response)

    def get_pets_by_status(self, params):
        url = self.url + "pet/findByStatus"
        response = requests.get(url=url, params=params)
        return AssertableResponse(response)

    def post_new_pet(self, payload):
        url = self.url + "pet"
        response = requests.post(url=url, data=json.dumps(payload), headers=self.headers)
        return AssertableResponse(response)

    def post_existing_pet_with_form_data(self, pet_id, data):
        url = self.url + f"pet/{pet_id}"
        response = requests.post(url=url, data=data)
        return AssertableResponse(response)

    def post_image_to_pet(self, pet_id, file):
        url = self.url + f"pet/{pet_id}/uploadImage"
        response = requests.post(url=url, files=file)
        return AssertableResponse(response)

    def put_existing_pet(self, payload):
        url = self.url + "pet"
        response = requests.put(url=url, data=json.dumps(payload), headers=self.headers)
        return AssertableResponse(response)

    def delete_pet(self, pet_id):
        url = self.url + f"pet/{pet_id}"
        response = requests.delete(url=url)
        return AssertableResponse(response)
