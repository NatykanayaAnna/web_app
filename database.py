from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://banner_admin:postgres@localhost:5432/banners_project"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
class BannersModel(db.Model):
    __tablename__ = 'banners'

    banner_id = db.Column(db.String(), primary_key=True)
    image_path = db.Column(db.String(), nullable=False)
    image_name = db.Column(db.String(), nullable=False)
    url = db.Column(db.String(), nullable=False)
    status = db.Column(db.Boolean, default=False)
    position = db.Column(db.Integer, nullable=False)


    def init(self, banner_id, image_path, image_name, status, position):
        self.banner_id = banner_id
        self.image_path = image_path
        self.image_name = image_name
        self.status = status
        self.position = position

@app.route('/')
def handle_banners():
    print(BannersModel.query.all())
    return render_template('home.html', my_string='Wheeeee!', my_list=[0, 1, 2, 3, 4, 5])