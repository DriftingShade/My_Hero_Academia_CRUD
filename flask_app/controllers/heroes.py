from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.hero import Hero


@app.route("/")
def index():
    return render_template("index.html")


@app.post("/create")
def create():
    Hero.create_hero(request.form)
    return redirect("/all_heroes")


@app.route("/all_heroes")
def all_heroes():
    heroes = Hero.get_all()
    return render_template("all_heroes.html", heroes=heroes)


@app.route("/edit_hero/<int:id>")
def edit_hero(id):
    hero = Hero.get_hero_by_id({"id": id})
    return render_template("edit_hero.html", hero=hero)


@app.post("/update_hero/<int:id>")
def update_hero(id):
    data = {
        "id": id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "quirk": request.form["quirk"],
        "age": request.form["age"],
    }
    Hero.update(data)
    return redirect("/all_heroes")


@app.post("/delete_hero/<int:id>")
def delete_hero(id):
    Hero.delete({"id": id})
    return redirect("/all_heroes")
