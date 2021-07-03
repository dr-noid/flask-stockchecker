from app import app
from app import db
from app import stockchecker


if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    app.run(debug=True)