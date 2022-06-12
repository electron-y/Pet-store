import pytest

from src.wrappers.store import Store


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


@pytest.fixture()
def delete_order():

    yield

    delete_order_by_id = Store().delete_order(payload_create_order["id"])
    delete_order_by_id.should_have_status_code(200)
