import pytest

from src.wrappers.pet import Pet


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


@pytest.fixture()
def delete_pet():

    yield

    delete_pet = Pet().delete_pet(payload_create_pet["id"])
    delete_pet.should_have_status_code(200)
