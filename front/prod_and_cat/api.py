from flask import session
import requests

from config import Config
# from app.utils import check_response_errors
from prod_and_cat.models import ProductsAdd, CategoryAdd, ShopProductsAdd
from user.api import request_with_auth

# CREATE_PRODUCTS_URL = f"{Config.API_URL}/products/addproduct"
CREATE_PRODUCTS_URL = f"{Config.API_URL}/products/"
CREATE_CATEGORY_URL = f"{Config.API_URL}/category/"
CREATE_SHOPPRODUCT_URL = f"{Config.API_URL}/shopproduct/"



# LOGIN_URL = f"{Config.API_URL}/token/"
# REFRESH_URL = f"{Config.API_URL}/token/refresh/"


##################

# def refresh_token_request():
#     refresh_token = session["refresh"]
#     req = requests.post(REFRESH_URL, json={
#         "refresh": refresh_token
#     })
#     session["access"] = req.json()["access"]
#     session.modified = True

# def request_with_refresh(
#     method: str = None, url: str = None,
#     headers: dict = None, files: dict = None,
#     data: dict = None, json: dict = None,
#     **kwargs,
# ) -> requests.Response:
#     res = request_with_auth(
#         method=method, url=url,
#         headers=headers, files=files,
#         data=data, json=json,
#         **kwargs
#     )
#     if res.status_code == 403:
#         refresh_token_request()
#         res = request_with_auth(
#             method=method, url=url,
#             headers=headers, files=files,
#             data=data, json=json,
#             **kwargs
#         )
#     return res

# def add_product(*args, **kwargs) -> ProductsAdd:
#     # add_product = ProductsAdd(**kwargs)
#     # res = requests.post(CREATE_PRODUCTS_URL, json=add_product.dict())
#     # product = ProductsAdd(**res.json())
#     # return product
#     req = request_with_refresh("POST", CREATE_PRODUCTS_URL, json=add_product.dict())
#     post_data = req.json()
#     return post_data
##############################


# def get_current_product(*args, **kwargs) -> ProductsAdd:
   
#     res = request_with_auth('GET', CURENT_PROD_URL)
#     product = ProductsAdd(**res.json())
#     return product
##################

API = "http://127.0.0.1:8000/api"

# prod = requests.get(f"{API}/api/products/").json()

def add_product(*args, **kwargs) -> ProductsAdd:
    add_product = ProductsAdd(**kwargs)
    # res = requests.post(f"{API}/api/products/").json()
    res = requests.post(CREATE_PRODUCTS_URL, json=add_product.dict())
    product = ProductsAdd(**res.json())
    return product


# def prost_list_request():
#     req = request_with_refresh("GET", f"{API}/products/")
#     posts_data = req.json()
#     return posts_data

# def product_id(*args, **kwargs):
#     prod = requests.get(CREATE_PRODUCTS_URL).json()[-1]['id']
#     return prod

# def add_product(*args, **kwargs) -> ProductsAdd:
#     add_product = ProductsAdd(**kwargs)
#     res = requests.post(CREATE_PRODUCTS_URL, json=add_product.dict())
#     product = ProductsAdd(**res.json())
#     return product


def add_category(*args, **kwargs) -> CategoryAdd:
    add_category = CategoryAdd(**kwargs)
    res = requests.post(CREATE_CATEGORY_URL, json=add_category.dict())
    category = CategoryAdd(**res.json())
    return category


def add_shopproduct(*args, **kwargs) -> ShopProductsAdd:
    add_shopproduct = ShopProductsAdd(**kwargs)
    res = requests.post(CREATE_SHOPPRODUCT_URL, json=add_shopproduct.dict())
    shopproduct = ShopProductsAdd(**res.json())
    return shopproduct