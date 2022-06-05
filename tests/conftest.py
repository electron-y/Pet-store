import pytest

from src.wrappers.pet import Pet
from src.wrappers.user import User
from src.wrappers.store import Store
from src.wrappers.authentication import Authentication


payload_create_pet = {
        "id": 1212,
        "category": {
            "id": 1,
            "name": "Cat"
        },
        "name": "Mikasa",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }


@pytest.fixture()
def add_pet():

    add_new_pet = Pet().post_new_pet(payload_create_pet)
    add_new_pet.should_have_status_code(200)
    add_new_pet.should_have_body_field("id", payload_create_pet["id"])
    add_new_pet.should_have_body_field("category", payload_create_pet["category"])
    add_new_pet.should_have_body_field("name", payload_create_pet["name"])
    add_new_pet.should_have_body_field("status", payload_create_pet["status"])


@pytest.fixture()
def delete_pet():

    yield

    delete_pet = Pet().delete_pet(payload_create_pet["id"])
    delete_pet.should_have_status_code(200)
    delete_pet.should_have_body_field("code", 200)
    delete_pet.should_have_body_field("message", str(payload_create_pet["id"]))


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
    create_user.should_have_body_field("code", 200)
    create_user.should_have_body_field("message", str(payload_create_user["id"]))


@pytest.fixture()
def delete_user():

    yield

    delete_user = User().delete_user(payload_create_user["username"])
    delete_user.should_have_status_code(200)
    delete_user.should_have_body_field("code", 200)
    delete_user.should_have_body_field("message", str(payload_create_user["username"]))


@pytest.fixture()
def login_user():

    params = {"username": "Johnny", "password": "Johnny228"}

    login_user = Authentication().get_login_user(params)
    login_user.should_have_status_code(200)
    login_user.should_have_body_field("code", 200)
    login_user.does_str_in_value("message", "logged in user session:")


payload_create_order = {
        "id": 123,
        "petId": 1111,
        "quantity": 1,
        "shipDate": "2022-05-16T13:32:37.914+0000",
        "status": "placed"
    }


@pytest.fixture()
def place_order():

    place_order = Store().post_order(payload_create_order)
    place_order.should_have_status_code(200)
    place_order.should_have_body_field("id", payload_create_order["id"])
    place_order.should_have_body_field("petId", payload_create_order["petId"])
    place_order.should_have_body_field("quantity", payload_create_order["quantity"])
    place_order.should_have_body_field("status", payload_create_order["status"])
    return place_order.get_value("")


@pytest.fixture()
def delete_order():

    yield

    delete_order_by_id = Store().delete_order(payload_create_order["id"])
    delete_order_by_id.should_have_status_code(200)
    delete_order_by_id.should_have_body_field("code", 200)
    delete_order_by_id.should_have_body_field("message", str(payload_create_order["id"]))
