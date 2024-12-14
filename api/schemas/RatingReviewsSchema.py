from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Base schema for Ratings and Reviews
class RatingsReviewsBase(BaseModel):
    menuItemId: int
    customerId: int
    rating: int
    reviewText: Optional[str] = None

# Schema for creating a new Rating and Review
class RatingsReviewsCreate(RatingsReviewsBase):
    pass

# Schema for updating an existing Rating and Review
class RatingsReviewsUpdate(BaseModel):
    rating: Optional[int] = None
    reviewText: Optional[str] = None

# Schema for returning Ratings and Reviews data (includes reviewId and createdAt)
class RatingsReviews(RatingsReviewsBase):
    reviewId: int
    createdAt: datetime

    class Config:
        orm_mode = True
