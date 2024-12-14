from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import Orders as controller
from ..controllers.Orders import getOrderStatus
from ..schemas import OrdersSchema as schema
from ..dependencies.Database import getDb

router = APIRouter(
    tags=['Customer Orders'],
    prefix="/orders"
)

@router.get("/order/status")
def readOrderStatus(customerId: int, trackingNumber: str, db: Session = Depends(getDb)):
    """
    Retrieve the status of an order by customer ID and tracking number
    """
    return getOrderStatus(db, customerId, trackingNumber)

@router.post("/", response_model=schema.Orders)
def createOrder(request: schema.OrdersCreate, db: Session = Depends(getDb)):
    """
    Create a new order
    """
    return controller.createOrder(db=db, request=request)

@router.get("/", response_model=list[schema.Orders])
def readAllOrders(db: Session = Depends(getDb)):
    """
    Retrieve all orders
    """
    return controller.readAllOrders(db)

@router.get("/{orderId}", response_model=schema.Orders)
def readOneOrder(orderId: int, db: Session = Depends(getDb)):
    """
    Retrieve a single order by ID
    """
    return controller.readOrder(db, orderId=orderId)

@router.put("/{orderId}", response_model=schema.Orders)
def updateOrder(orderId: int, request: schema.OrdersUpdate, db: Session = Depends(getDb)):
    """
    Update an order by ID
    """
    return controller.updateOrder(db=db, request=request, orderId=orderId)

@router.delete("/{orderId}")
def deleteOrder(orderId: int, db: Session = Depends(getDb)):
    """
    Delete an order by ID
    """
    return controller.deleteOrder(db=db, orderId=orderId)
