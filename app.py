from flask import Flask, render_template, request, flash
from flask_migrate import Migrate
import add_banner_form
from flask_bootstrap import Bootstrap
from models.banners import db, BannersModel
import config_parcer
import uuid


app = Flask(__name__)
app.secret_key = b'x4x58'
app.config['SECRET_KEY'] = 'any secret string'
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = config_parcer.db_connection_string
migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def handle_banners():
    return render_template('home.html', data=BannersModel.query.all())


@app.route('/add', methods=['GET', 'POST'])
def add_new_banner():
    form = add_banner_form.AddBannerForm(request.form)
    if request.method == 'POST' and form.validate():
        new_banner = BannersModel()
        new_banner.banner_id = uuid.uuid4()
        new_banner.image_name = form.banners_name.data
        # new_banner.image_path TBD create func to safe file
        new_banner.image_path = 'test'
        new_banner.url = form.url.data
        new_banner.status = form.status.data
        new_banner.position = form.position.data
        #  TBD try except flash error message
        db.session.add(new_banner)
        db.session.commit()
        flash('Form successfully sended', 'success')
        return render_template('home.html', data=BannersModel.query.all())
    return render_template('add_banner.html', my_form=form)


@app.route('/edit')
def edit_banner():
    banners_id = request.args.get('banners_id')
    print(banners_id)
    edit_row = BannersModel.query.get(banners_id)
    print(edit_row)
    return edit_row.image_name