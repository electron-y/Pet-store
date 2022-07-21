import pytest

from src.wrappers.store import Store


payload_create_order = {
        "id": 123,
        "petId": 1111,
        "quantity": 1,
        "shipDate": "2022-05-16T13:32:37.914+0000",
        "status": "placed"
    }


@pytest.mark.smoke
def test_place_order(delete_order):

    place_order = Store().post_order(payload_create_order)
    place_order.should_have_status_code(200)
    place_order.should_have_body_field("id", payload_create_order["id"])
    place_order.should_have_body_field("petId", payload_create_order["petId"])
    place_order.should_have_body_field("quantity", payload_create_order["quantity"])
    place_order.should_have_body_field("status", payload_create_order["status"])

    find_order_by_id = Store().get_order(payload_create_order["id"])
    find_order_by_id.should_have_status_code(200)
    find_order_by_id.should_have_body_field("id", payload_create_order["id"])
    find_order_by_id.should_have_body_field("petId", payload_create_order["petId"])
    find_order_by_id.should_have_body_field("quantity", payload_create_order["quantity"])
    find_order_by_id.should_have_body_field("status", payload_create_order["status"])


@pytest.mark.smoke
def test_delete_order(place_order):

    delete_order_by_id = Store().delete_order(payload_create_order["id"])
    delete_order_by_id.should_have_status_code(200)
    delete_order_by_id.should_have_body_field("code", 200)
    delete_order_by_id.should_have_body_field("message", str(payload_create_order["id"]))


def test_get_inventory():

    get_inventory = Store().get_inventory()
    get_inventory.should_have_status_code(200)
