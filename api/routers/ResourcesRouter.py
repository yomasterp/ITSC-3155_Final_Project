from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import Resources as controller
from ..schemas import ResourcesSchema as schema
from ..dependencies.Database import getDb

router = APIRouter(
    tags=['Resources'],
    prefix="/resources"
)

@router.post("/", response_model=schema.Resources)
def createResource(request: schema.ResourcesCreate, db: Session = Depends(getDb)):
    """
    Create a new resource
    """
    return controller.createResource(db=db, request=request)

@router.get("/", response_model=list[schema.Resources])
def readAllResources(db: Session = Depends(getDb)):
    """
    Retrieve all resources
    """
    return controller.readAllResources(db)

@router.get("/{resourceId}", response_model=schema.Resources)
def readResource(resourceId: int, db: Session = Depends(getDb)):
    """
    Retrieve a single resource by ID
    """
    return controller.readResource(db, resourceId=resourceId)

@router.put("/{resourceId}", response_model=schema.Resources)
def updateResource(resourceId: int, request: schema.ResourcesUpdate, db: Session = Depends(getDb)):
    """
    Update a resource by ID
    """
    return controller.updateResource(db=db, request=request, resourceId=resourceId)

@router.delete("/{resourceId}")
def deleteResource(resourceId: int, db: Session = Depends(getDb)):
    """
    Delete a resource by ID
    """
    return controller.deleteResource(db=db, resourceId=resourceId)
