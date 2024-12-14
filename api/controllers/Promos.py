from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from sqlalchemy.exc import SQLAlchemyError
from ..models import PromosModel as promotionModel


def createPromotion(db: Session, request):
    newPromotion = promotionModel.Promotion(
        code=request.code,
        expirationDate=request.expirationDate,
        discountPercentage=request.discountPercentage,
        status="Valid" if request.expirationDate > datetime.now() else "Expired"
    )

    try:
        db.add(newPromotion)
        db.commit()
        db.refresh(newPromotion)
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))

    return newPromotion

def readAllPromotions(db: Session):
    try:
        promotions = db.query(promotionModel.Promotion).all()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return promotions

def readPromotion(db: Session, promotionId):
    try:
        promotion = db.query(promotionModel.Promotion).filter(promotionModel.Promotion.promotionId == promotionId).first()
        if not promotion:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion ID not found!")
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return promotion

def updatePromotion(db: Session, promotionId, request):
    try:
        promotion = db.query(promotionModel.Promotion).filter(promotionModel.Promotion.promotionId == promotionId)
        if not promotion.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion ID not found!")
        updateData = request.dict(exclude_unset=True)
        promotion.update(updateData, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return promotion.first()

def deletePromotion(db: Session, promotionId):
    try:
        promotion = db.query(promotionModel.Promotion).filter(promotionModel.Promotion.promotionId == promotionId)
        if not promotion.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion ID not found!")
        promotion.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return Response(status_code=status.HTTP_204_NO_CONTENT)
