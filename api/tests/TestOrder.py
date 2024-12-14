from fastapi.testclient import TestClient
from ..controllers import Orders as controller
from ..main import app
import pytest
from ..models import OrdersModel as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_order(db_session):

    # Create a sample order
    order_data = {
        "customerId": 1,
        "orderType": "Delivery",
        "orderStatus": "Pending",
        "trackingNumber": "123ABC",
        "promotionId": None
    }

    order_object = model.Orders(**order_data)

    # Call the create function
    created_order = controller.createOrder(db_session, order_object)

    # Test assertions
    assert created_order is not None
    assert created_order.customerId == 1
    assert created_order.orderType == "Delivery"
    assert created_order.orderStatus == "Pending"
    assert created_order.trackingNumber == "123ABC"
