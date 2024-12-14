from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from ..models import CustomerModel as customerModel


def createCustomer(db: Session, request):
    if db.query(customerModel.Customers).filter(customerModel.Customers.email == request.email).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A customer with this email already exists."
        )

    newCustomer = customerModel.Customers(
        name=request.name,
        email=request.email,
        phoneNumber=request.phoneNumber,
        address=request.address
    )

    try:
        db.add(newCustomer)
        db.commit()
        db.refresh(newCustomer)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Database integrity error. Possible duplicate entry."
        )
    except SQLAlchemyError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error.__dict__['orig'])
        )

    return newCustomer

def readAllCustomers(db: Session):
    try:
        customers = db.query(customerModel.Customers).all()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error.__dict__['orig']))
    return customers

def readCustomer(db: Session, customerId):
    try:
        customer = db.query(customerModel.Customers).filter(customerModel.Customers.customerId == customerId).first()
        if not customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Customer with ID {customerId} not found."
            )
    except SQLAlchemyError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error.__dict__['orig'])
        )
    return customer

def updateCustomer(db: Session, customerId, request):
    try:
        customer = db.query(customerModel.Customers).filter(customerModel.Customers.customerId == customerId)
        if not customer.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Customer with ID {customerId} not found."
            )
        updateData = request.dict(exclude_unset=True)
        customer.update(updateData, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error.__dict__['orig'])
        )
    return customer.first()

def deleteCustomer(db: Session, customerId):
    try:
        customer = db.query(customerModel.Customers).filter(customerModel.Customers.customerId == customerId)
        if not customer.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Customer with ID {customerId} not found."
            )
        customer.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot delete customer because they have associated orders."
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
