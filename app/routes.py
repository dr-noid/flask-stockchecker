from app import app
from app import db
from flask import render_template, url_for, flash, redirect
from app.models import Item
from app import stockchecker

@app.route("/")
def index():
    print(Item.query.all())
    return "test ok"


@app.route("/reload", methods=["GET", "POST"])
def reload():
    stockchecker.run()
    return redirect("/")