from app.models import Item
from app import db


def add_items():
    items = [Item(name="RTX 3070", url="https://www.nu.nl", price=799.95),
            Item(name="RTX 3080", url="https://www.nu.nl", price=799.95),
            Item(name="RTX 3090", url="https://www.nu.nl", price=799.95)]

    for item in items:
        db.session.add(item)
    db.session.commit()