from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    query = StringField('Query',validators=[DataRequired()],render_kw={"placeholder": "Search albums"})
    submit = SubmitField('Search')