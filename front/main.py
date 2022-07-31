from unicodedata import category
from flask import Flask
from flask import redirect, render_template, session, url_for
import requests
from config import Config
from user.routers import user_blueprint
from prod_and_cat.routers import products_blueprint


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(user_blueprint)
app.register_blueprint(products_blueprint)

API = "http://127.0.0.1:8000"


@app.route("/", methods=["GET"])
def start():
    categ = requests.get(f"{API}/api/category/").json()
    return render_template("index.html", category = categ)


if __name__ == "__main__":
    app.run()