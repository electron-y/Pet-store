import json
import os

import requests

from src.assertable_response import AssertableResponse


class User:

    def __init__(self):
        self.url = os.environ["BASE_URL"]
        self.headers = {'Content-Type': 'application/json'}

    def get_user_by_username(self, username):
        url = self.url + f"user/{username}"
        response = requests.get(url=url)
        return AssertableResponse(response)

    def get_logout_user(self):
        url = self.url + "user/logout"
        response = requests.get(url=url)
        return AssertableResponse(response)

    def post_user(self, payload):
        url = self.url + "user"
        response = requests.post(url=url, data=json.dumps(payload), headers=self.headers)
        return AssertableResponse(response)

    def post_list_of_users_with_array(self, payload):
        url = self.url + "user/createWithArray"
        response = requests.post(url=url, data=json.dumps(payload), headers=self.headers)
        return AssertableResponse(response)

    def post_list_of_users_with_list(self, payload):
        url = self.url + "user/createWithList"
        response = requests.post(url=url, data=json.dumps(payload), headers=self.headers)
        return AssertableResponse(response)

    def put_user(self, username, payload):
        url = self.url + f"user/{username}"
        response = requests.put(url=url, data=json.dumps(payload), headers=self.headers)
        return AssertableResponse(response)

    def delete_user(self, username):
        url = self.url + f"user/{username}"
        response = requests.delete(url=url)
        return AssertableResponse(response)
