from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from ..models import OrdersModel as orderModel


def createOrder(db: Session, request):
    newOrder = orderModel.CustOrder(
        customerId=request.customerId,
        orderType=request.orderType,
        orderDate=datetime.utcnow(),
        orderStatus='Pending',
        trackingNumber=request.trackingNumber,
        promotionId=request.promotionId
    )

    try:
        db.add(newOrder)
        db.commit()
        db.refresh(newOrder)
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))

    return newOrder

def readAllOrders(db: Session):
    try:
        orders = db.query(orderModel.CustOrder).all()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return orders

def readOrder(db: Session, orderId):
    try:
        order = db.query(orderModel.CustOrder).filter(orderModel.CustOrder.customerId == orderId).first()
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order ID not found!")
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return order

def updateOrder(db: Session, orderId, request):
    try:
        order = db.query(orderModel.CustOrder).filter(orderModel.CustOrder.customerId == orderId)
        if not order.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order ID not found!")
        updateData = request.dict(exclude_unset=True)
        order.update(updateData, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return order.first()

def deleteOrder(db: Session, orderId):
    try:
        order = db.query(orderModel.CustOrder).filter(orderModel.CustOrder.customerId == orderId)
        if not order.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order ID not found!")
        order.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def getOrderStatus(db: Session, customerId, trackingNumber: str):
    order = db.query(orderModel.CustOrder).filter(
        (orderModel.CustOrder.customerId == customerId) &
        (orderModel.CustOrder.trackingNumber == trackingNumber)
    ).first()

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order with this tracking number not found for the given customer."
        )

    return {
        "orderStatus": order.orderStatus,
        "trackingNumber": order.trackingNumber,
        "orderId": order.orderId
    }
