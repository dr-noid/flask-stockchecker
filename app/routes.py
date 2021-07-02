from app import app
from app import db
from flask import render_template, url_for, flash, redirect
from app.models import Item

@app.route("/")
def index():
    db.create_all()
    print(Item.query.all())
    return "test ok"