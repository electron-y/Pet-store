import pytest

from src.wrappers.authentication import Authentication


@pytest.fixture()
def login_user():

    params = {"username": "Johnny", "password": "Johnny228"}

    login_user = Authentication().get_login_user(params)
    login_user.should_have_status_code(200)
    login_user.should_have_body_field("code", 200)
    login_user.does_str_in_value("message", "logged in user session:")
