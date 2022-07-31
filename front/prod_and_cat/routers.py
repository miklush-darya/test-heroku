from itertools import product
from flask import Flask, Blueprint, jsonify
from flask import redirect, render_template, url_for, request
from config import Config
import requests

from prod_and_cat.forms import ProductrForm, CategoryForm, ShopProductForm
from user.api import get_current_user

from prod_and_cat.api import add_category, add_product
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


products_blueprint = Blueprint(
        "products", __name__,
        template_folder="templates",
        url_prefix="/products",
    )

API = "http://127.0.0.1:8000"



@products_blueprint.route("/", methods=["GET"])
def list_product():
    prod = requests.get(f"{API}/api/products/").json()
    categ = requests.get(f"{API}/api/category/").json()
    return render_template("prodlist.html", product=prod, category=categ)


@products_blueprint.route("/categ", methods=["GET", "POST"])
def categ():
    filter_cat = request.args.get("category")
    if filter_cat:
        a = requests.get(f"{API}/api/category/?category={filter_cat}").json()
    # else:
    #     a = requests.get(f"{API}/api/executor/").json()
    b = requests.get(f"{API}/api/category/").json()

    return render_template("executors.html", a=a, b=b)


@products_blueprint.route("/addproduct", methods=["GET", "POST"])
def add_prod():
    form = ProductrForm()
    if form.validate_on_submit():
        user = get_current_user()
        user.store_in_session()
        form_data = dict(form.data)
        form_data['category'] = list(form_data['category'])
        add_product(**form_data)
        # categ = add_category(**form.data)
        return redirect(url_for("products.list_product"))
    return render_template("addprod.html", form=form)



# @app.products_blueprint("/post-create-ajax", methods=["POST"])
# @products_blueprint.route("/addproduct", methods=["GET", "POST"])
# def prost_create():
#     name_product=request.form.get("name_product")
#     description = request.form.get("description")
#     characteristics=request.form.get("characteristics")
#     category=request.form.get("category")
#     post = prost_create_request(name_product=name_product, description=description, characteristics=characteristics, category=category)
#     return jsonify(post), 201

# @order_blueprint.route("/add", methods=["GET", "POST"])
# def add():
#     form = OrderForm()
#     if form.validate_on_submit():
#         user = get_current_user()
#         user.store_in_session()
#         form_data = dict(form.data)
#         order_add(**form_data)
#         
#         return redirect(url_for("index"))
#     return render_template("add.html", form=form)


# @products_blueprint.route("/category", methods=["GET"])
# def list_category():
#     categ = requests.get(f"{API}/api/category/").json()
#     return render_template("categorylist.html", category=categ)
