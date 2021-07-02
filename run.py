from app import app
from app import db
from app.models import Item
from app import stockchecker


if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    stockchecker.add_items()
    app.run(debug=True)