from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from sqlalchemy.exc import SQLAlchemyError
from ..models import ResourcesModel as resourceModel


def createResource(db: Session, request):
    newResource = resourceModel.ResourceManagement(
        item=request.item,
        amount=request.amount,
        unit=request.unit
    )

    try:
        db.add(newResource)
        db.commit()
        db.refresh(newResource)
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))

    return newResource

def readAllResources(db: Session):
    try:
        resources = db.query(resourceModel.ResourceManagement).all()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return resources

def readResource(db: Session, resourceId):
    try:
        resource = db.query(resourceModel.ResourceManagement).filter(resourceModel.ResourceManagement.resourceId == resourceId).first()
        if not resource:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource ID not found!")
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return resource

def updateResource(db: Session, resourceId, request):
    try:
        resource = db.query(resourceModel.ResourceManagement).filter(resourceModel.ResourceManagement.resourceId == resourceId)
        if not resource.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource ID not found!")
        updateData = request.dict(exclude_unset=True)
        resource.update(updateData, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return resource.first()

def deleteResource(db: Session, resourceId):
    try:
        resource = db.query(resourceModel.ResourceManagement).filter(resourceModel.ResourceManagement.resourceId == resourceId)
        if not resource.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource ID not found!")
        resource.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return Response(status_code=status.HTTP_204_NO_CONTENT)
