from flask import Flask, Blueprint
from flask import redirect, render_template, session, url_for, request
from test-heroku.front.shop.forms import RegisterShopForm
from test_heroku.front.shop.api import create_shop, get_current_shop
from config import Config
from test_heroku.front.user.models import BaseModel


app = Flask(__name__)
app.config.from_object(Config)
shop_blueprint = Blueprint("shop",
                            __name__,
                            template_folder="templates",
                            static_folder="static",
                            url_prefix="/shop",
                        )


@shop_blueprint.route("/shop", methods=["GET", "POST"])
def shop():
    form = RegisterShopForm()
    if form.validate_on_submit():
        form = create_shop(**form.data)
        form.store_in_session()
        return redirect(url_for("shop.home"))
    return render_template("shop.html", form=form)


