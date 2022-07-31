from datetime import datetime, date
from typing import Optional, List, Union
from pydantic import BaseModel, Field, Extra


class ProductsAdd(BaseModel):
    # id: int
    # created: Optional[datetime]
    # modified: datetime = None
    name_product: str = Field(min_length=2, max_length=30)
    description: str
    characteristics: str
    # category: str
    category: List[Union[int, str]]

    class Config:
        extra = Extra.ignore


class CategoryAdd(BaseModel):
    id: int
    created: Optional[datetime]
    modified: datetime = None
    name_category: str = Field(min_length=2, max_length=30)

    class Config:
        extra = Extra.ignore


class ShopProductsAdd(BaseModel):
    id: int
    created: Optional[datetime]
    modified: datetime = None
    price: str
    quantity: int
    product: str
    shop: str

    class Config:
        extra = Extra.ignore
