import pytest

from src.wrappers.pet import Pet


def test_pet():

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

    update_payload = {
        "id": 1212,
        "category": {
            "id": 2,
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

    params = {"name": "Bonny1", "status": "sold"}

    file = {'file': ('image_png_1MB.png', open('/Users/y.khomych/Desktop/test files/image_png_1MB.png', 'rb'), 'image/png')}

    add_new_pet = Pet().post_new_pet(create_payload)
    add_new_pet.should_have_status_code(200)
    add_new_pet.should_have_body_field("id", create_payload["id"])
    add_new_pet.should_have_body_field("category", create_payload["category"])
    add_new_pet.should_have_body_field("name", create_payload["name"])
    add_new_pet.should_have_body_field("status", create_payload["status"])

    get_pet_by_id = Pet().get_pet_by_id(create_payload["id"])
    get_pet_by_id.should_have_status_code(200)
    get_pet_by_id.should_have_body_field("id", create_payload["id"])
    get_pet_by_id.should_have_body_field("category", create_payload["category"])
    get_pet_by_id.should_have_body_field("name", create_payload["name"])
    get_pet_by_id.should_have_body_field("status", create_payload["status"])

    update_existing_pet = Pet().put_existing_pet(update_payload)
    update_existing_pet.should_have_status_code(200)
    update_existing_pet.should_have_body_field("id", update_payload["id"])
    update_existing_pet.should_have_body_field("category", update_payload["category"])
    update_existing_pet.should_have_body_field("name", update_payload["name"])
    update_existing_pet.should_have_body_field("status", update_payload["status"])

    update_existing_pet_with_new_form_data = Pet().post_existing_pet_with_form_data(create_payload["id"], params)
    update_existing_pet_with_new_form_data.should_have_status_code(200)
    update_existing_pet_with_new_form_data.should_have_body_field("code", 200)
    update_existing_pet_with_new_form_data.should_have_body_field("message", str(update_payload["id"]))

    get_pet_by_id = Pet().get_pet_by_id(create_payload["id"])
    get_pet_by_id.should_have_status_code(200)
    get_pet_by_id.should_have_body_field("id", update_payload["id"])
    get_pet_by_id.should_have_body_field("category", update_payload["category"])
    get_pet_by_id.should_have_body_field("name", params["name"])
    get_pet_by_id.should_have_body_field("status", params["status"])

    upload_image_to_existing_pet = Pet().post_image_to_pet(create_payload["id"], file)
    upload_image_to_existing_pet.should_have_status_code(200)
    upload_image_to_existing_pet.should_have_body_field("code", 200)
    upload_image_to_existing_pet.should_have_body_field("message",
                                                        "additionalMetadata: null\nFile uploaded to ./image_png_1MB.png, 1108353 bytes")

    delete_pet = Pet().delete_pet(create_payload["id"])
    delete_pet.should_have_status_code(200)
    delete_pet.should_have_body_field("code", 200)
    delete_pet.should_have_body_field("message", str(update_payload["id"]))


@pytest.mark.parametrize("status", ['available', 'pending', 'sold'])
def test_pet_status(status):

    params = {"status": status}

    get_pets_by_status = Pet().get_pets_by_status(params)
    get_pets_by_status.should_have_status_code(200)
