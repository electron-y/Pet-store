import json
import os

import requests

from src.assertable_response import AssertableResponse


class Authentication:

    def __init__(self):
        self.url = os.environ["BASE_URL"]
        self.headers = {'Content-Type': 'application/json'}

    def get_login_user(self, params):
        url = self.url + "user/login"
        response = requests.get(url=url, params=params)
        return AssertableResponse(response)
