from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
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
