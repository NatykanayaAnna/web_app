from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, BooleanField, IntegerField, SelectField


class AddBannerForm(FlaskForm):
    banners_name = StringField('Banners Name')
    image = FileField()
    url = StringField('Url')
    status = BooleanField('Status', default=False)
    position = SelectField('Position', choices=[(1, 1), (2, 2), (3, 3)])
