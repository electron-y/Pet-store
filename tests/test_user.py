import pytest

from src.wrappers.user import User


def test_user():

    create_payload = {
        "id": 112233,
        "username": "Johnny",
        "firstName": "John",
        "lastName": "Smith",
        "email": "john228@gmail.com",
        "password": "Johnny228",
        "phone": "380777777777",
        "userStatus": 0
    }

    update_payload = {
        "id": 112233,
        "username": "Johnny_update",
        "firstName": "John_update",
        "lastName": "Smith_update",
        "email": "john228_update@gmail.com",
        "password": "Johnny228_update",
        "phone": "380888888888",
        "userStatus": 0
    }

    params = {"username": "Johnny", "password": "Johnny228"}

    post_user = User().post_user(create_payload)
    post_user.should_have_status_code(200)
    post_user.should_have_body_field("code", 200)
    post_user.should_have_body_field("message", str(create_payload["id"]))

    get_login_user = User().get_login_user(params)
    get_login_user.should_have_status_code(200)
    get_login_user.should_have_body_field("code", 200)
    get_login_user.does_str_in_value("message", "logged in user session:")

    put_user = User().put_user(create_payload["username"], update_payload)
    put_user.should_have_status_code(200)
    put_user.should_have_body_field("code", 200)
    put_user.should_have_body_field("message", str(update_payload["id"]))

    get_user = User().get_user_by_username(update_payload["username"])
    get_user.should_have_status_code(200)
    get_user.should_have_body_field("id", update_payload["id"])
    get_user.should_have_body_field("username", update_payload["username"])
    get_user.should_have_body_field("firstName", update_payload["firstName"])
    get_user.should_have_body_field("lastName", update_payload["lastName"])
    get_user.should_have_body_field("email", update_payload["email"])
    get_user.should_have_body_field("password", update_payload["password"])
    get_user.should_have_body_field("phone", update_payload["phone"])

    delete_user = User().delete_user(update_payload["username"])
    delete_user.should_have_status_code(200)
    delete_user.should_have_body_field("code", 200)
    delete_user.should_have_body_field("message", str(update_payload["username"]))

    get_logout_user = User().get_logout_user()
    get_logout_user.should_have_status_code(200)
    get_logout_user.should_have_body_field("code", 200)
    get_logout_user.should_have_body_field("message", "ok")


def test_create_list_of_users():

    payload = [
        {
            "id": 11100,
            "username": "Brady",
            "firstName": "Brad",
            "lastName": "Pitt",
            "email": "brad@gmail.com",
            "password": "brad1963",
            "phone": "380636784545",
            "userStatus": 0
        },
        {
            "id": 22200,
            "username": "James_007",
            "firstName": "James",
            "lastName": "Bond",
            "email": "james@gmail.com",
            "password": "james007",
            "phone": "380969990007",
            "userStatus": 0
        }
    ]

    post_users_with_array = User().post_list_of_users_with_array(payload)
    post_users_with_array.should_have_status_code(200)
    post_users_with_array.should_have_body_field("code", 200)
    post_users_with_array.should_have_body_field("message", "ok")

    post_users_with_list = User().post_list_of_users_with_list(payload)
    post_users_with_list.should_have_status_code(200)
    post_users_with_list.should_have_body_field("code", 200)
    post_users_with_list.should_have_body_field("message", "ok")


def test_get_user_with_not_existing_username():

    get_user = User().get_user_by_username("21312312312qwe213")
    get_user.should_have_status_code(404)
    get_user.should_have_body_field("code", 1)
    get_user.should_have_body_field("message", "User not found")
