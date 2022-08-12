from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, BooleanField, IntegerField, SelectField, validators


class AddBannerForm(FlaskForm):
    banners_name = StringField('Banners Name', [validators.DataRequired(), validators.Length(min=2, max=50)])
    image = FileField()
    url = StringField('Url', [validators.DataRequired(), validators.Length(min=9)])
    status = BooleanField('Status', default=False)
    position = SelectField('Position', choices=[(1, 1), (2, 2), (3, 3)])
