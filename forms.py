from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, URL, Length, Email, EqualTo, InputRequired
from flask_ckeditor import CKEditorField
from wtforms.widgets.core import Input


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email Address', validators=[DataRequired(), Length(min=11, max=50),Email(message='Invalid email address', check_deliverability=True)])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')


# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = EmailField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Log In')

# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment = CKEditorField('Leave a comment', validators=[DataRequired()])
    submit = SubmitField('Tweet Comment')