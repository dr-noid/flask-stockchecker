from app import app
from app import db
from app import stockchecker


if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    stockchecker.run()
    app.run(debug=True)