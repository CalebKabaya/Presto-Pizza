from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired





class UpdateProfile(FlaskForm):
    bio = TextAreaField('bio', validators=[DataRequired()])
    submit = SubmitField('Post')
