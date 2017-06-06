from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import email, length, DataRequired

class SignupForm(FlaskForm):
    email = StringField("Please enter your email", validators=[DataRequired("You must enter an email"), email("This doesn't look like an email")])
    first_name = StringField("Please enter your first name", validators=[DataRequired("This field can't be empty")])
    last_name = StringField("Please enter your last name", validators=[DataRequired("This field can't be empty")])
    password = PasswordField("Please enter your password", validators=[DataRequired("This field can't be empty"), length(min=5, message="Your password must be more than 5 characters long")])
    submit = SubmitField("Submit")
    
