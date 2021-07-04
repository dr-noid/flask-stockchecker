from app import app
from flask import render_template, redirect, request
from app.models import Item
from app import stockchecker

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", items = Item.query.all())


@app.get("/reload")
async def reload():
    Item.query.delete()
    # gpus = request.values.getlist("gpu")
    gpus = []
    await stockchecker.run(gpus)
    return redirect("/")