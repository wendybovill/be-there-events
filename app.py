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
    events = list(mongo.db.events.find())

    def show_last_event(event_id):
        last_event = list(mongo.db.events.find_one().sort({"_id": ObjectId(
            event_id)}).limit(1))
        return render_template("index.html", events=last_event)
    return render_template("index.html", events=events)


@app.route("/get_events")
def get_events():
    events = list(mongo.db.events.find())
    return render_template("events.html", events=events)


@app.route("/add_events", methods=["GET", "POST"])
def add_events():
    if request.method == "POST":
        is_paid_for = "yes" if request.form.get("is_paid_for") else "free"
        events = {
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
            "event_paid_for": request.form.get("event_paid_for"),
        }
        flash("You have added an event: {{ event_title }}")
        mongo.db.events.insert_one(event)
        return redirect(url_for("get_events"))
    return render_template("events.html", events=events)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), debug=True)
