from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import Customers as controller
from ..schemas.CustomerSchema import CustomerCreate, CustomerUpdate, Customer
from ..dependencies.Database import getDb

router = APIRouter(
    tags=['Customer Details'],
    prefix="/customer_details"
)

@router.post("/", response_model=Customer)
def createCustomer(request: CustomerCreate, db: Session = Depends(getDb)):
    """
    Create a new customer
    """
    return controller.createCustomer(db=db, request=request)

@router.get("/", response_model=list[Customer])
def readAllCustomers(db: Session = Depends(getDb)):
    """
    Retrieve all customers
    """
    return controller.readAllCustomers(db)

@router.get("/{customerId}", response_model=Customer)
def readOneCustomer(customerId: int, db: Session = Depends(getDb)):
    """
    Retrieve a single customer by ID
    """
    return controller.readCustomer(db, customerId=customerId)

@router.put("/{customerId}", response_model=Customer)
def updateCustomer(customerId: int, request: CustomerUpdate, db: Session = Depends(getDb)):
    """
    Update customer details
    """
    return controller.updateCustomer(db=db, request=request, customerId=customerId)

@router.delete("/{customerId}", status_code=status.HTTP_204_NO_CONTENT)
def deleteCustomer(customerId: int, db: Session = Depends(getDb)):
    """
    Delete a customer by ID
    """
    controller.deleteCustomer(db=db, customerId=customerId)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
