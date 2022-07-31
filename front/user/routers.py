from flask import Flask, Blueprint
from flask import redirect, render_template, session, url_for, request
from user.forms import LoginForm, RegisterUserForm
from user.api import access, create_user, get_current_user
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


user_blueprint = Blueprint("user",
                            __name__,
                            template_folder="templates",
                            static_folder="static",
                            url_prefix="/user",
                        )

# @app.route("/", methods=["GET"])
@user_blueprint.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# @app.route("/login", methods=["GET", "POST"])
@user_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        auth = access(**form.data)
        auth.store_in_session()
        user = get_current_user()
        user.store_in_session()
        return redirect(url_for("user.home")) #Vinesti
    return render_template("userlogin.html", form=form)


# @app.route("/logout", methods=["GET"])
@user_blueprint.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect(url_for("user.login"))




@user_blueprint.route("/register", methods=["GET", "POST"])
# @app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterUserForm()
    if form.validate_on_submit():
        user = create_user(**form.data)
        user.store_in_session()
        auth = access(**form.data)
        auth.store_in_session()
        return redirect(url_for("user.home"))
    return render_template("userregister.html", form=form)


# @user_blueprint.route("/register", methods=["GET", "POST"])
# def register():
#     form = RegisterUserForm()
#     if request.method == "POST":
#         user = create_user(**form.data)
#         return redirect(url_for("home"))
#
#     return render_template("register.html", form=form)

