from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,IntegerField
from wtforms.validators import DataRequired



class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    size = SelectField('Size', choices=[('Small','Small'),('Medium','Medium'),('Large','Large ')],validators=[DataRequired()])
    price = IntegerField('Price of the product', validators=[DataRequired()])
    submit = SubmitField('ADD PRODUCT')