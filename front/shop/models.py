from datetime import datetime
from typing import Optional
from flask import session
from pydantic import BaseModel as PyModel, EmailStr, Extra, validator
from test_heroku.front.user.models import BaseModel,  StoreInSessionMixin


class RegisterShop(PyModel):

    name_shop: str
    unp: int

    class Config:
        extra = Extra.ignore


class Shop(StoreInSessionMixin, BaseModel):
    name_shop: str
    is_active: bool = True
    is_superuser: bool = False

    class Config:
        extra = Extra.ignore