from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import OrderDetails as controller
from ..schemas import OrderDetailsSchema as schema
from ..dependencies.Database import getDb

router = APIRouter(
    tags=['Order Details'],
    prefix="/order_details"
)

@router.post("/", response_model=schema.OrderDetails)
def createOrderDetail(request: schema.OrderDetailsCreate, db: Session = Depends(getDb)):
    """
    Create a new order detail
    """
    return controller.createOrderDetail(db=db, request=request)

@router.get("/", response_model=list[schema.OrderDetails])
def readAllOrderDetails(db: Session = Depends(getDb)):
    """
    Retrieve all order details
    """
    return controller.readAllOrderDetails(db)

@router.get("/{orderDetailId}", response_model=schema.OrderDetails)
def readOrderDetail(orderDetailId: int, db: Session = Depends(getDb)):
    """
    Retrieve a single order detail by ID
    """
    return controller.readOrderDetail(db, orderDetailId=orderDetailId)

@router.put("/{orderDetailId}", response_model=schema.OrderDetails)
def updateOrderDetail(orderDetailId: int, request: schema.OrderDetailsUpdate, db: Session = Depends(getDb)):
    """
    Update an order detail by ID
    """
    return controller.updateOrderDetail(db=db, request=request, orderDetailId=orderDetailId)

@router.delete("/{orderDetailId}")
def deleteOrderDetail(orderDetailId: int, db: Session = Depends(getDb)):
    """
    Delete an order detail by ID
    """
    return controller.deleteOrderDetail(db=db, orderDetailId=orderDetailId)
