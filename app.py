import os
import pathlib
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/get_events")
def get_events():
    events = list(mongo.db.events.find())
    return render_template("events.html", events=events)


@app.route("/add_event", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        event_paid_for = "true" if request.form.get(
            "event_paid_for") else "false"
        event = {
            "event_type": request.form.get("event_type"),
            "event_title": request.form.get("event_title"),
            "event_date": request.form.get("event_date"),
            "event_time": request.form.get("event_time"),
            "event_description": request.form.get("event_description"),
            "event_location_town": request.form.get("event_location_town"),
            "event_location_postcode": request.form.get(
                "event_location_postcode"),
            "event_organiser": request.form.get("event_organiser"),
            "event_contact_details": request.form.get("event_contact_details"),
            "event_url": request.form.get("event_url"),
            "event_entrance_fee": request.form.get("event_entrance_fee"),
            "event_paid_for": event_paid_for,
        }

        mongo.db.events.insert_one(event)
        flash("You have added an event: {{ event_title }}")
        return redirect(url_for("get_events"))
    types = mongo.db.types.find().sort("type_name", 1)
    return render_template("add_event.html", types=types)


@app.route("/edit_event/<event_id>", methods=["GET", "POST"])
def edit_event(event_id):
    if request.method == "POST":
        event_paid_for = "true" if request.form.get(
            "event_paid_for") else "false"
        submit = {
            "event_type": request.form.get("event_type"),
            "event_title": request.form.get("event_title"),
            "event_date": request.form.get("event_date"),
            "event_time": request.form.get("event_time"),
            "event_description": request.form.get("event_description"),
            "event_location_town": request.form.get("event_location_town"),
            "event_location_postcode": request.form.get(
                "event_location_postcode"),
            "event_organiser": request.form.get("event_organiser"),
            "event_contact_details": request.form.get("event_contact_details"),
            "event_url": request.form.get("event_url"),
            "event_entrance_fee": request.form.get("event_entrance_fee"),
            "event_paid_for": event_paid_for,
        }
        flash("You have updated an event")
        mongo.db.events.update_one(
            {"_id": ObjectId(event_id)}, {"$set": submit})
    types = mongo.db.types.find().sort("type_name", 1)
    event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    return render_template("edit_events.html", event=event, types=types)


@app.route("/delete_event/<event_id>", methods=["GET", "POST"])
def delete_event(event_id):
    types = mongo.db.types.find().sort("type_name", 1)
    event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    flash("Are you sure you want to delete this event?")
    return render_template("delete_event.html", event=event, types=types)


@app.route("/delete_event_confirm/<event_id>")
def delete_event_confirm(event_id):
    mongo.db.events.delete_one({"_id": ObjectId(event_id)})
    flash("Event Deleted")
    return redirect(url_for("get_events"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), debug=True)
