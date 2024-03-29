from flask_wtf import FlaskForm

from wtforms import EmailField, SubmitField, StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, URL
from flask_ckeditor import CKEditorField

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
class RegisterForm(FlaskForm):
    email = EmailField("Email: ", validators=[DataRequired(), Email()])
    username = StringField("Username: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(min=8)])
    bg_color = SelectField('Choice a background color',
                           choices=[('000000', 'Black'), ('37306B', 'Navy'),
                                    ('862B0D', 'Maroon'), ('454545', 'Dark Gray')]
                           )
    bio = TextAreaField("Bio: ", validators=[Length(max=250)])
    submit = SubmitField("Submit", render_kw={"style": "margin-top: 15px;"})


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    # img_url = StringField("Blog Image URL", validators=[URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")


class EditProfileForm(FlaskForm):
    email = EmailField("Email: ", validators=[DataRequired(), Email()])
    username = StringField("Username: ", validators=[DataRequired()])
    bg_color = SelectField('Choice a background color',
                           choices=[('000000', 'Black'), ('37306B', 'Navy'),
                                    ('862B0D', 'Maroon'), ('454545', 'Dark Gray')]
                           )
    bio = TextAreaField("Bio: ", validators=[Length(max=250)])
    submit = SubmitField("Save", render_kw={"style": "margin-top: 15px;"})



