from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message = 'Passwords must match')])
    submit = SubmitField('Submit')

class SendForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    text_body = TextAreaField('Message', validators=[DataRequired()])
    from_email = StringField('From Email', validators=[DataRequired(), Email(granular_message=True)])
    recipients_email = StringField('Add Recipients', validators=[DataRequired()])
    submit = SubmitField('Send Email')