from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import MenuItem as controller
from ..schemas import MenuItemSchema as schema
from ..dependencies.Database import getDb

router = APIRouter(
    tags=['Menu Items'],
    prefix="/menu_items"
)

@router.post("/", response_model=schema.MenuItems)
def createMenuItem(request: schema.MenuItemsCreate, db: Session = Depends(getDb)):
    """
    Create a new menu item
    """
    return controller.createMenuItem(db=db, request=request)

@router.get("/", response_model=list[schema.MenuItems])
def readAllMenuItems(db: Session = Depends(getDb)):
    """
    Retrieve all menu items
    """
    return controller.readAllMenuItems(db)

@router.get("/{menuItemId}", response_model=schema.MenuItems)
def readMenuItem(menuItemId: int, db: Session = Depends(getDb)):
    """
    Retrieve a single menu item by ID
    """
    return controller.readMenuItem(db, menuItemId=menuItemId)

@router.put("/{menuItemId}", response_model=schema.MenuItems)
def updateMenuItem(menuItemId: int, request: schema.MenuItemsUpdate, db: Session = Depends(getDb)):
    """
    Update a menu item by ID
    """
    return controller.updateMenuItem(db=db, request=request, menuItemId=menuItemId)

@router.delete("/{menuItemId}")
def deleteMenuItem(menuItemId: int, db: Session = Depends(getDb)):
    """
    Delete a menu item by ID
    """
    return controller.deleteMenuItem(db=db, menuItemId=menuItemId)
