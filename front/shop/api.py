import requests
from config import Config
# from app.utils import check_response_errors
from test_heroku.front.shop.models import RegisterShop, Shop
from test_heroku.front.user.api import request_with_auth


CURRENT_SHOP_URL = f"{Config.API_URL}/shop/me"
CREATE_SHOP_URL = f"{Config.API_URL}/shop/"


def get_current_shop() -> Shop:
    res = request_with_auth("GET", CURRENT_SHOP_URL)
    # check_response_errors(res, 200)
    shop = Shop(**res.json())
    return shop


def create_shop(*args, **kwargs) -> Shop:
    register_shop = RegisterShop(**kwargs)
    res = requests.post(CREATE_SHOP_URL, json=register_shop.dict())
    # check_response_errors(res, 201)
    shop = Shop(**res.json())
    return shop

