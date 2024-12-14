from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import PaymentInformation as controller
from ..schemas import PaymentInformationSchema as schema
from ..dependencies.Database import getDb

router = APIRouter(
    tags=['Payment Information'],
    prefix="/payment_information"
)

@router.post("/", response_model=schema.PaymentInfo)
def createPaymentInfo(request: schema.PaymentInfoCreate, db: Session = Depends(getDb)):
    """
    Create a new payment information entry
    """
    return controller.createPaymentInfo(db=db, request=request)

@router.get("/", response_model=list[schema.PaymentInfo])
def readAllPaymentInfo(db: Session = Depends(getDb)):
    """
    Retrieve all payment information entries
    """
    return controller.readAllPaymentInfo(db)

@router.get("/{paymentInfoId}", response_model=schema.PaymentInfo)
def readPaymentInfo(paymentInfoId: int, db: Session = Depends(getDb)):
    """
    Retrieve payment information by ID
    """
    return controller.readPaymentInfo(db, paymentInfoId=paymentInfoId)

@router.put("/{paymentInfoId}", response_model=schema.PaymentInfo)
def updatePaymentInfo(paymentInfoId: int, request: schema.PaymentInfoUpdate, db: Session = Depends(getDb)):
    """
    Update payment information by ID
    """
    return controller.updatePaymentInfo(db=db, request=request, paymentInfoId=paymentInfoId)

@router.delete("/{paymentInfoId}")
def deletePaymentInfo(paymentInfoId: int, db: Session = Depends(getDb)):
    """
    Delete payment information by ID
    """
    return controller.deletePaymentInfo(db=db, paymentInfoId=paymentInfoId)
