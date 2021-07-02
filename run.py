from app import app
from app import db
from app.models import Item


def first_run():
    print("first run")
    db.drop_all()
    db.create_all()
    item = Item(name="RTX 3070", url="https://www.nu.nl", price=799.95)
    db.session.add(item)
    db.session.commit()


if __name__ == "__main__":
    first_run()
    app.run(debug=True)