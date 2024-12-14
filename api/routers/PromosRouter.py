from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import Promos as controller
from ..schemas import PromosSchema as schema
from ..dependencies.Database import getDb

router = APIRouter(
    tags=['Promotions'],
    prefix="/promotions"
)

@router.post("/", response_model=schema.Promotions)
def createPromotion(request: schema.PromotionsCreate, db: Session = Depends(getDb)):
    """
    Create a new promotion
    """
    return controller.createPromotion(db=db, request=request)

@router.get("/", response_model=list[schema.Promotions])
def readAllPromotions(db: Session = Depends(getDb)):
    """
    Retrieve all promotions
    """
    return controller.readAllPromotions(db)

@router.get("/{promotionId}", response_model=schema.Promotions)
def readPromotion(promotionId: int, db: Session = Depends(getDb)):
    """
    Retrieve a promotion by ID
    """
    return controller.readPromotion(db, promotionId=promotionId)

@router.put("/{promotionId}", response_model=schema.Promotions)
def updatePromotion(promotionId: int, request: schema.PromotionsUpdate, db: Session = Depends(getDb)):
    """
    Update a promotion by ID
    """
    return controller.updatePromotion(db=db, request=request, promotionId=promotionId)

@router.delete("/{promotionId}")
def deletePromotion(promotionId: int, db: Session = Depends(getDb)):
    """
    Delete a promotion by ID
    """
    return controller.deletePromotion(db=db, promotionId=promotionId)
