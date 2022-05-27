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

    post_order = Store().post_order(payload)
    post_order.should_have_status_code(200)
    post_order.should_have_body_field("id", payload["id"])
    post_order.should_have_body_field("petId", payload["petId"])
    post_order.should_have_body_field("quantity", payload["quantity"])
    post_order.should_have_body_field("status", payload["status"])

    get_order = Store().get_order(payload["id"])
    get_order.should_have_status_code(200)
    get_order.should_have_body_field("id", payload["id"])
    get_order.should_have_body_field("petId", payload["petId"])
    get_order.should_have_body_field("quantity", payload["quantity"])
    get_order.should_have_body_field("status", payload["status"])

    delete_order = Store().delete_order(payload["id"])
    delete_order.should_have_status_code(200)
    delete_order.should_have_body_field("code", 200)
    delete_order.should_have_body_field("message", str(payload["id"]))
