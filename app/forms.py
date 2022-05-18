from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

class SearchForm(FlaskForm):
    query = StringField('Query', render_kw={"placeholder": "Search albums"})
    submit = SubmitField('Search')