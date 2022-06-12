import pytest

from src.wrappers.pet import Pet


payload_create_pet = {
    "available": {
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
    },

    "pending": {
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
        "status": "pending"
    },

    "sold": {
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
        "status": "sold"
    }
}

payload_update_pet = {
        "id": 1212,
        "category": {
            "id": 2121,
            "name": "Dog"
        },
        "name": "Bonny",
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


def test_create_pet(delete_pet):

    add_new_pet = Pet().post_new_pet(payload_create_pet["available"])
    add_new_pet.should_have_status_code(200)
    add_new_pet.should_have_body_field("id", payload_create_pet["available"]["id"])
    add_new_pet.should_have_body_field("category", payload_create_pet["available"]["category"])
    add_new_pet.should_have_body_field("name", payload_create_pet["available"]["name"])
    add_new_pet.should_have_body_field("status", payload_create_pet["available"]["status"])


def test_delete_pet(add_pet):

    delete_pet = Pet().delete_pet(payload_create_pet["available"]["id"])
    delete_pet.should_have_status_code(200)
    delete_pet.should_have_body_field("code", 200)
    delete_pet.should_have_body_field("message", str(payload_create_pet["available"]["id"]))


def test_update_existing_pet(add_pet, delete_pet):

    update_existing_pet = Pet().put_existing_pet(payload_update_pet)
    update_existing_pet.should_have_status_code(200)
    update_existing_pet.should_have_body_field("id", payload_update_pet["id"])
    update_existing_pet.should_have_body_field("category", payload_update_pet["category"])
    update_existing_pet.should_have_body_field("name", payload_update_pet["name"])
    update_existing_pet.should_have_body_field("status", payload_update_pet["status"])

    get_pet_by_id = Pet().get_pet_by_id(payload_update_pet["id"])
    get_pet_by_id.should_have_status_code(200)
    get_pet_by_id.should_have_body_field("id", payload_update_pet["id"])
    get_pet_by_id.should_have_body_field("category", payload_update_pet["category"])
    get_pet_by_id.should_have_body_field("name", payload_update_pet["name"])
    get_pet_by_id.should_have_body_field("status", payload_update_pet["status"])


@pytest.mark.parametrize("status, payload", [('available', payload_create_pet["available"]),
                                             ('pending', payload_create_pet["pending"]),
                                             ('sold', payload_create_pet["sold"])])
def test_get_pets_by_status(status, payload):

    params = {"status": status}

    add_pet = Pet().post_new_pet(payload)
    add_pet.should_have_status_code(200)
    add_pet.should_have_body_field("id", payload["id"])
    add_pet.should_have_body_field("category", payload["category"])
    add_pet.should_have_body_field("name", payload["name"])
    add_pet.should_have_body_field("status", payload["status"])

    get_pets_by_status = Pet().get_pets_by_status(params)
    get_pets_by_status.should_have_status_code(200)
    get_pets_by_status.should_have_body_field("id", payload["id"])
    get_pets_by_status.should_have_body_field("category", payload["category"])
    get_pets_by_status.should_have_body_field("name", payload["name"])
    get_pets_by_status.should_have_body_field("status", payload["status"])

    delete_pet = Pet().delete_pet(payload["id"])
    delete_pet.should_have_status_code(200)
    delete_pet.should_have_body_field("code", 200)
    delete_pet.should_have_body_field("message", str(payload["id"]))


def test_update_existing_pet_with_new_form_data(add_pet, delete_pet):

    params = {"name": "Bonny1", "status": "sold"}

    update_existing_pet_with_new_form_data = Pet().post_existing_pet_with_form_data(payload_update_pet["id"], params)
    update_existing_pet_with_new_form_data.should_have_status_code(200)
    update_existing_pet_with_new_form_data.should_have_body_field("code", 200)
    update_existing_pet_with_new_form_data.should_have_body_field("message", str(payload_update_pet["id"]))

    get_pet_by_id = Pet().get_pet_by_id(payload_update_pet["id"])
    get_pet_by_id.should_have_status_code(200)
    get_pet_by_id.should_have_body_field("name", params["name"])
    get_pet_by_id.should_have_body_field("status", params["status"])


def test_upload_image_to_existing_pet(add_pet, delete_pet):

    file = {'file': ('image_png_1MB.png', open('/Users/y.khomych/Desktop/test files/image_png_1MB.png', 'rb'), 'image/png')}

    upload_image_to_existing_pet = Pet().post_image_to_pet(payload_update_pet["id"], file)
    upload_image_to_existing_pet.should_have_status_code(200)
    upload_image_to_existing_pet.should_have_body_field("code", 200)
    upload_image_to_existing_pet.should_have_body_field("message",
                                                        "additionalMetadata: null\nFile uploaded to ./image_png_1MB.png, 1108353 bytes")
