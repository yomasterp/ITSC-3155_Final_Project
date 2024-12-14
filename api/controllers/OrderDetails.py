from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func
from ..models import OrderDetailsModel as orderDetailModel
from ..models import OrdersModel as customerOrderModel
from ..models import PromosModel as promotionModel
from ..models import MenuItemModel as menuItemModel


def getDailyRevenue(db: Session):
    try:
        result = db.query(
            func.date(customerOrderModel.CustOrder.orderDate).label('orderDate'),
            func.sum(orderDetailModel.OrderDetails.total).label('totalRevenue')
        ).join(
            customerOrderModel.CustOrder, orderDetailModel.OrderDetails.orderId == customerOrderModel.CustOrder.orderId
        ).group_by(
            func.date(customerOrderModel.CustOrder.orderDate)
        ).order_by(
            func.date(customerOrderModel.CustOrder.orderDate).desc()
        ).all()

        return [{"date": row.orderDate, "totalRevenue": float(row.totalRevenue)} for row in result]
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))

def createOrderDetail(db: Session, request):
    menuItem = db.query(menuItemModel.MenuItem).filter(menuItemModel.MenuItem.menuItemId == request.menuItemId).first()
    if not menuItem:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu Item not found.")

    for itemIngredient in menuItem.ingredient:
        resource = itemIngredient.resource
        if resource.amount < request.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Not enough {itemIngredient.description} available for this order."
            )

    totalPrice = menuItem.price * request.quantity

    totalAfterDiscount = totalPrice
    if request.promotionId:
        promotion = db.query(promotionModel.Promotion).filter(promotionModel.Promotion.promotionId == request.promotionId).first()
        if promotion:
            discount = (totalPrice * promotion.discountPercentage) / 100
            totalAfterDiscount = totalPrice - discount
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found.")

    newOrderDetail = orderDetailModel.OrderDetails(
        orderId=request.orderId,
        menuItemId=request.menuItemId,
        quantity=request.quantity,
        amount=totalPrice,
        total=totalAfterDiscount,
        promotionId=request.promotionId,
    )

    try:
        db.add(newOrderDetail)
        db.commit()
        db.refresh(newOrderDetail)
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))

    return newOrderDetail

def readAllOrderDetails(db: Session, startDate: Optional[datetime] = None, endDate: Optional[datetime] = None):
    try:
        query = db.query(orderDetailModel.OrderDetails).join(customerOrderModel.CustOrder, orderDetailModel.OrderDetails.orderId == customerOrderModel.CustOrder.orderId)

        if startDate:
            query = query.filter(customerOrderModel.CustOrder.orderDate >= startDate)

        if endDate:
            query = query.filter(customerOrderModel.CustOrder.orderDate <= endDate)

        result = query.all()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))

    return result

def readOrderDetail(db: Session, orderDetailId):
    try:
        orderDetail = db.query(orderDetailModel.OrderDetails).filter(orderDetailModel.OrderDetails.id == orderDetailId).first()
        if not orderDetail:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order Detail ID not found!")
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return orderDetail

def updateOrderDetail(db: Session, orderDetailId, request):
    try:
        orderDetail = db.query(orderDetailModel.OrderDetails).filter(orderDetailModel.OrderDetails.id == orderDetailId)
        if not orderDetail.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order Detail ID not found!")
        updateData = request.dict(exclude_unset=True)
        orderDetail.update(updateData, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return orderDetail.first()

def deleteOrderDetail(db: Session, orderDetailId):
    try:
        orderDetail = db.query(orderDetailModel.OrderDetails).filter(orderDetailModel.OrderDetails.id == orderDetailId)
        if not orderDetail.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order Detail ID not found!")
        orderDetail.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return Response(status_code=status.HTTP_204_NO_CONTENT)
