import pytest

from src.wrappers.user import User


payload_create_user = {
        "id": 112233,
        "username": "Johnny",
        "firstName": "John",
        "lastName": "Smith",
        "email": "john228@gmail.com",
        "password": "Johnny228",
        "phone": "380777777777",
        "userStatus": 0
    }


@pytest.fixture()
def create_user():

    create_user = User().post_user(payload_create_user)
    create_user.should_have_status_code(200)


@pytest.fixture()
def delete_user():

    yield

    delete_user = User().delete_user(payload_create_user["username"])
    delete_user.should_have_status_code(200)
