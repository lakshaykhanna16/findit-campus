from extensions import db

class Item(db.Model):
    __tablename__ = "items"

    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(150))
    date = db.Column(db.Date)
    description = db.Column(db.Text)

    image_filename = db.Column(db.String(255))