from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from sqlalchemy.exc import SQLAlchemyError
from ..models import PaymentInformationModel as paymentInfoModel


def createPaymentInfo(db: Session, request):
    newPaymentInfo = paymentInfoModel.PaymentInfo(
        orderId=request.orderId,
        cardNumber=request.cardNumber,
        expiryDate=request.expiryDate,
        cardHolderName=request.cardHolderName,
        paymentType=request.paymentType
    )

    try:
        db.add(newPaymentInfo)
        db.commit()
        db.refresh(newPaymentInfo)
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))

    return newPaymentInfo

def readAllPaymentInfo(db: Session):
    try:
        paymentInfoList = db.query(paymentInfoModel.PaymentInfo).all()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return paymentInfoList

def readPaymentInfo(db: Session, paymentInfoId):
    try:
        paymentInfo = db.query(paymentInfoModel.PaymentInfo).filter(paymentInfoModel.PaymentInfo.paymentId == paymentInfoId).first()
        if not paymentInfo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment Info ID not found!")
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return paymentInfo

def updatePaymentInfo(db: Session, paymentInfoId, request):
    try:
        paymentInfo = db.query(paymentInfoModel.PaymentInfo).filter(paymentInfoModel.PaymentInfo.paymentId == paymentInfoId)
        if not paymentInfo.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment Info ID not found!")
        updateData = request.dict(exclude_unset=True)
        paymentInfo.update(updateData, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return paymentInfo.first()

def deletePaymentInfo(db: Session, paymentInfoId):
    try:
        paymentInfo = db.query(paymentInfoModel.PaymentInfo).filter(paymentInfoModel.PaymentInfo.paymentId == paymentInfoId)
        if not paymentInfo.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment Info ID not found!")
        paymentInfo.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return Response(status_code=status.HTTP_204_NO_CONTENT)
