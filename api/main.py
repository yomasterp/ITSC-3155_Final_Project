import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import (
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

origins = ["*"]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routers
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
    Home endpoint to verify API is running.
    """
    return {"message": "API is up and running!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
