import pytest

from src.wrappers.store import Store


def test_place_find_delete_order():

    payload = {
        "id": 123,
        "petId": 1111,
        "quantity": 1,
        "shipDate": "2022-05-16T13:32:37.914+0000",
        "status": "placed"
    }

    place_order = Store().post_order(payload)
    place_order.should_have_status_code(200)
    place_order.should_have_body_field("id", payload["id"])
    place_order.should_have_body_field("petId", payload["petId"])
    place_order.should_have_body_field("quantity", payload["quantity"])
    place_order.should_have_body_field("status", payload["status"])

    find_order_by_id = Store().get_order(payload["id"])
    find_order_by_id.should_have_status_code(200)
    find_order_by_id.should_have_body_field("id", payload["id"])
    find_order_by_id.should_have_body_field("petId", payload["petId"])
    find_order_by_id.should_have_body_field("quantity", payload["quantity"])
    find_order_by_id.should_have_body_field("status", payload["status"])

    delete_order_by_id = Store().delete_order(payload["id"])
    delete_order_by_id.should_have_status_code(200)
    delete_order_by_id.should_have_body_field("code", 200)
    delete_order_by_id.should_have_body_field("message", str(payload["id"]))
