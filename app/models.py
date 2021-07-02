from datetime import datetime
from app import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    image_file = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"User('{self.name}', '{self.url}', '{self.price}')"