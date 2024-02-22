from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Email, InputRequired


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), Email()])
    subject = StringField("Subject", validators=[InputRequired()])
    message = StringField("Message", validators=[InputRequired()])
