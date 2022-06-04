import pytest

from src.wrappers.pet import Pet


create_payload = {
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

    add_new_pet = Pet().post_new_pet(create_payload)
    add_new_pet.should_have_status_code(200)
    add_new_pet.should_have_body_field("id", create_payload["id"])
    add_new_pet.should_have_body_field("category", create_payload["category"])
    add_new_pet.should_have_body_field("name", create_payload["name"])
    add_new_pet.should_have_body_field("status", create_payload["status"])


@pytest.fixture()
def delete_pet():

    yield

    delete_pet = Pet().delete_pet(create_payload["id"])
    delete_pet.should_have_status_code(200)
    delete_pet.should_have_body_field("code", 200)
    delete_pet.should_have_body_field("message", str(create_payload["id"]))
