from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired


class RegisterShopForm(FlaskForm):
    name_shop = StringField("name_shop", validators=[DataRequired(), ])
    unp = IntegerField("unp", validators=[DataRequired(), ])
    submit = SubmitField("Add shop")