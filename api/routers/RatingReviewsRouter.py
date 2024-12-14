from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import RatingsReviews as controller
from ..schemas import RatingReviewsSchema as schema
from ..dependencies.Database import getDb

router = APIRouter(
    tags=['Ratings and Reviews'],
    prefix="/ratings_reviews"
)

@router.post("/", response_model=schema.RatingsReviews)
def createRating(request: schema.RatingsReviewsCreate, db: Session = Depends(getDb)):
    """
    Create a new rating and review
    """
    return controller.createRating(db=db, request=request)

@router.get("/", response_model=list[schema.RatingsReviews])
def readAllRatings(db: Session = Depends(getDb)):
    """
    Retrieve all ratings and reviews
    """
    return controller.readAllRatings(db)

@router.get("/{reviewId}", response_model=schema.RatingsReviews)
def readRating(reviewId: int, db: Session = Depends(getDb)):
    """
    Retrieve a rating and review by ID
    """
    return controller.readRating(db, reviewId=reviewId)

@router.put("/{reviewId}", response_model=schema.RatingsReviews)
def updateRating(reviewId: int, request: schema.RatingsReviewsUpdate, db: Session = Depends(getDb)):
    """
    Update a rating and review by ID
    """
    return controller.updateRating(db=db, request=request, reviewId=reviewId)

@router.delete("/{reviewId}")
def deleteRating(reviewId: int, db: Session = Depends(getDb)):
    """
    Delete a rating and review by ID
    """
    return controller.deleteRating(db=db, reviewId=reviewId)

@router.get("/low_rated", response_model=list[schema.RatingsReviews])
def getLowRatedDishes(db: Session = Depends(getDb)):
    """
    Retrieve dishes with ratings of 3 or lower
    """
    return controller.getLowRatedDishes(db)
