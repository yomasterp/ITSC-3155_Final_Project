from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from sqlalchemy.exc import SQLAlchemyError
from ..models import RatingReviewsModel as ratingsModel


def createRating(db: Session, request):
    newRating = ratingsModel.RatingsReviews(
        menuItemId=request.menuItemId,
        customerId=request.customerId,
        rating=request.rating,
        reviewText=request.reviewText,
        createdAt=request.createdAt
    )

    try:
        db.add(newRating)
        db.commit()
        db.refresh(newRating)
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))

    return newRating

def readAllRatings(db: Session):
    try:
        ratings = db.query(ratingsModel.RatingsReviews).all()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return ratings

def readRating(db: Session, ratingId):
    try:
        rating = db.query(ratingsModel.RatingsReviews).filter(ratingsModel.RatingsReviews.reviewId == ratingId).first()
        if not rating:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rating ID not found!")
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return rating

def updateRating(db: Session, ratingId, request):
    try:
        rating = db.query(ratingsModel.RatingsReviews).filter(ratingsModel.RatingsReviews.reviewId == ratingId)
        if not rating.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rating ID not found!")
        updateData = request.dict(exclude_unset=True)
        rating.update(updateData, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return rating.first()

def deleteRating(db: Session, ratingId):
    try:
        rating = db.query(ratingsModel.RatingsReviews).filter(ratingsModel.RatingsReviews.reviewId == ratingId)
        if not rating.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rating ID not found!")
        rating.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def getLowRatedDishes(db: Session):
    try:
        lowRatedDishes = db.query(ratingsModel.RatingsReviews) \
            .filter(ratingsModel.RatingsReviews.rating <= 3) \
            .all()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))

    return lowRatedDishes
