from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from sqlalchemy.exc import SQLAlchemyError
from ..models import MenuItemModel as menuItemModel


def searchMenuItems(db: Session, category):
    try:
        query = db.query(menuItemModel.MenuItem)

        if category:
            query = query.filter(menuItemModel.MenuItem.category == category)

        result = query.all()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))

    return result

def createMenuItem(db: Session, request):
    newMenuItem = menuItemModel.MenuItem(
        name=request.name,
        price=request.price,
        calories=request.calories,
        category=request.category
    )

    try:
        db.add(newMenuItem)
        db.commit()
        db.refresh(newMenuItem)
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))

    return newMenuItem

def readAllMenuItems(db: Session):
    try:
        menuItems = db.query(menuItemModel.MenuItem).all()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return menuItems

def readMenuItem(db: Session, menuItemId):
    try:
        menuItem = db.query(menuItemModel.MenuItem).filter(menuItemModel.MenuItem.menuItemId == menuItemId).first()
        if not menuItem:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu Item ID not found!")
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return menuItem

def updateMenuItem(db: Session, menuItemId, request):
    try:
        menuItem = db.query(menuItemModel.MenuItem).filter(menuItemModel.MenuItem.menuItemId == menuItemId)
        if not menuItem.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu Item ID not found!")
        updateData = request.dict(exclude_unset=True)
        menuItem.update(updateData, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return menuItem.first()

def deleteMenuItem(db: Session, menuItemId):
    try:
        menuItem = db.query(menuItemModel.MenuItem).filter(menuItemModel.MenuItem.menuItemId == menuItemId)
        if not menuItem.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu Item ID not found!")
        menuItem.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return Response(status_code=status.HTTP_204_NO_CONTENT)
