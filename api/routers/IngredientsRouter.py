from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import Ingredients as controller
from ..schemas import IngredientsSchema as schema
from ..dependencies.Database import getDb

router = APIRouter(
    tags=['Ingredients'],
    prefix="/ingredients"
)

@router.post("/", response_model=schema.Ingredients)
def createIngredient(request: schema.IngredientsCreate, db: Session = Depends(getDb)):
    """
    Create a new ingredient
    """
    return controller.createIngredient(db=db, request=request)

@router.get("/", response_model=list[schema.Ingredients])
def readAllIngredients(db: Session = Depends(getDb)):
    """
    Retrieve all ingredients
    """
    return controller.readAllIngredients(db)

@router.get("/{ingredientId}", response_model=schema.Ingredients)
def readIngredient(ingredientId: int, db: Session = Depends(getDb)):
    """
    Retrieve a single ingredient by ID
    """
    return controller.readIngredient(db, ingredientId=ingredientId)

@router.put("/{ingredientId}", response_model=schema.Ingredients)
def updateIngredient(ingredientId: int, request: schema.IngredientsUpdate, db: Session = Depends(getDb)):
    """
    Update an ingredient by ID
    """
    return controller.updateIngredient(db=db, request=request, ingredientId=ingredientId)

@router.delete("/{ingredientId}")
def deleteIngredient(ingredientId: int, db: Session = Depends(getDb)):
    """
    Delete an ingredient by ID
    """
    return controller.deleteIngredient(db=db, ingredientId=ingredientId)
