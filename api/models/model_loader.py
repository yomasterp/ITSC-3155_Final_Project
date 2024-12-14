from .OrdersModel import Orders
from .CustomerModel import Customer
from .MenuItemModel import MenuItems
from .PaymentInformationModel import PaymentInfo
from .PromosModel import Promotions
from .RatingReviewsModel import RatingsReviews
from .OrderDetailsModel import OrderDetails
from .ResourcesModel import Resources
from .IngredientsModel import Ingredients

from ..dependencies.Database import engine


def index():

    Customer.metadata.create_all(engine)
    Orders.metadata.create_all(engine)
    MenuItems.metadata.create_all(engine)
    PaymentInfo.metadata.create_all(engine)
    Promotions.metadata.create_all(engine)
    RatingsReviews.metadata.create_all(engine)
    OrderDetails.metadata.create_all(engine)
    Ingredients.metadata.create_all(engine)
    Resources.metadata.create_all(engine)
