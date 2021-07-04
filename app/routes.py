from app import app
from app import db
from flask import render_template, url_for, flash, redirect
from app.models import Item
from app import stockchecker
import asyncio

@app.route("/")
def index():
    return render_template("index.html", items = Item.query.all())


@app.route("/reload", methods=["GET", "POST"])
async def reload():
    await stockchecker.run()
    return redirect("/")