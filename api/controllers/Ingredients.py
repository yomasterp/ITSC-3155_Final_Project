from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from sqlalchemy.exc import SQLAlchemyError
from ..models import IngredientsModel as ingredientModel


def createIngredient(db: Session, request):
    newIngredient = ingredientModel.Ingredient(
        name=request.name
    )
    try:
        db.add(newIngredient)
        db.commit()
        db.refresh(newIngredient)
    except SQLAlchemyError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error.__dict__['orig'])
        )
    return newIngredient

def readAllIngredients(db: Session):
    try:
        ingredients = db.query(ingredientModel.Ingredient).all()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return ingredients

def readIngredient(db: Session, ingredientId):
    try:
        ingredient = db.query(ingredientModel.Ingredient).filter(ingredientModel.Ingredient.id == ingredientId).first()
        if not ingredient:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ingredient ID not found!")
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return ingredient

def updateIngredient(db: Session, ingredientId, request):
    try:
        ingredient = db.query(ingredientModel.Ingredient).filter(ingredientModel.Ingredient.id == ingredientId)
        if not ingredient.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ingredient ID not found!")
        updateData = request.dict(exclude_unset=True)
        ingredient.update(updateData, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return ingredient.first()

def deleteIngredient(db: Session, ingredientId):
    try:
        ingredient = db.query(ingredientModel.Ingredient).filter(ingredientModel.Ingredient.id == ingredientId)
        if not ingredient.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ingredient ID not found!")
        ingredient.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return Response(status_code=status.HTTP_204_NO_CONTENT)
