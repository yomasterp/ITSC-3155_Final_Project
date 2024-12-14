from fastapi import FastAPI
from . import (
    CustomerRouter,
    OrdersRouter,
    IngredientsRouter,
    MenuItemRouter,
    OrderDetailsRouter,
    PaymentInformationRouter,
    PromosRouter,
    RatingReviewsRouter,
    ResourcesRouter,
)

app = FastAPI()

# Including routers for various resources
app.include_router(CustomerRouter.router)
app.include_router(OrdersRouter.router)
app.include_router(IngredientsRouter.router)
app.include_router(MenuItemRouter.router)
app.include_router(OrderDetailsRouter.router)
app.include_router(PaymentInformationRouter.router)
app.include_router(PromosRouter.router)
app.include_router(RatingReviewsRouter.router)
app.include_router(ResourcesRouter.router)

@app.get("/")
def home():
    """
    Home endpoint to verify API is running
    """
    return {"message": "Welcome to the Sandwich Maker API Project!"}
