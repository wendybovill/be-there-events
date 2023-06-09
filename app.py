import os
import pathlib
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

app.config['MAIL_SERVER'] = 'mail.wideworldwebhosting.co.uk'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USER_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'event_lister@wideworldwebhosting.co.uk'
mail = Mail(app)


mongo = PyMongo(app)


def send_email(email):
    msg = Message("Testing",
                  sender="event_lister@wideworldwebhosting.co.uk",
                  recipients=["wendybovill@gmail.com"])

    msg.body = """
    Hi,

    Name: {}
    Email: {}
    Subject: {}
    Message: {}

    sent from webforms

    """.format(
        email['name'], email['email'], email['subject'], email['message'])

    mail.send(msg)


def send_thankyou_email(email):
    msg2 = Message("Thank you for contacting Event Lister Team",
                  sender="event_lister@wideworldwebhosting.co.uk",
                  recipients=email['email'])

    msg2.body = """
    Hi {},

    Thank you for your email.
    We have received it and will respond as soon as possible.

    The information you have sent us is:

    Name: {}
    Email: {}
    Subject: {}
    Message: {}

    Regards,

    from Event Lister Team

    """.format(
        email['name'], email['name'], email['email'], email['subject'], email['message'])

    mail.send(msg2)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        existing_username = mongo.db.users.find_one(
            {"username": request.form.get("username")}
        )
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()}
        )
        sign_up = {
            "username": request.form.get("username"),
            "fname": request.form.get("fname").lower(),
            "lname": request.form.get("lname").lower(),
            "dob": request.form.get("dob").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(
                request.form.get("password")),
        }
        if existing_username:
            flash("That username is taken")
            return redirect(url_for("sign_up"))
        elif existing_email:
            flash("That email address is already registered")
            return redirect(url_for("sign_up"))

        mongo.db.users.insert_one(sign_up)

        session["user"] = request.form.get("username")
        flash("Welcome to BeThere Events!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get(
                        "password")):
                session["user"] = request.form.get("username")
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # password not matching
                flash("Please check your login details")
                return redirect(url_for(("log_in")))
        else:
            # user is not found in database
            flash("Please check your login details")
            return redirect(url_for("log_in"))

        session["user"] = request.form.get("username")
        flash("Welcome to BeThere Events!")
    return render_template("login.html")


@app.route("/log_out")
def log_out():
    # redirect to confirmation page
    flash("Are you sure you want to log out?")
    return render_template("log_out_confirm.html")


@app.route("/log_out_confirm")
def log_out_confirm():
    session.pop("user")
    flash("You are now logged out.")
    return redirect(url_for("get_events"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):

    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

    users = mongo.db.users.find().sort("username", 1)
    user = mongo.db.users.find_one({"username": username})
    return render_template(
        "profile.html", username=username, user=user, users=users)


@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username):
    if request.method == "POST":
        existing_username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        update = {
            "username": request.form.get("username"),
            "fname": request.form.get("fname").title(),
            "lname": request.form.get("lname").title(),
            "email": request.form.get("email").lower(),
            "address_1": request.form.get("address_1").title(),
            "address_2": request.form.get("address_2").title(),
            "town": request.form.get("town").title(),
            "postcode": request.form.get("postcode").upper(),
            "phone": request.form.get("phone").lower()
        }

        mongo.db.users.update_one({"username": username}, {"$set": update})

        session["user"] = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        users = mongo.db.users.find().sort("username", 1)
        user = mongo.db.users.find_one({"username": username})
        flash("Your Profile has been updated " + username)
        return render_template(
            "profile.html", username=username, user=user, users=users)
    users = mongo.db.users.find().sort("username", 1)
    user = mongo.db.users.find_one({"username": username})
    return render_template(
        "edit_profile.html", username=username, user=user, users=users)


@app.route("/get_types")
def get_types():
    types = list(mongo.db.types.find().sort("type_name", 1))
    return render_template("types.html", types=types)


@app.route("/add_type", methods=["GET", "POST"])
def add_type():
    if request.method == "POST":
        type = {
            "added_by": session["user"],
            "type_name": request.form.get("type_name"),
            "type_description": request.form.get("type_description"),
        }

        mongo.db.types.insert_one(type)
        flash("You have added an Event Type")
        return redirect(url_for("get_types"))
    types = mongo.db.types.find().sort("type_name", 1)
    return render_template("add_type.html", types=types)


@app.route("/edit_type/<type_id>", methods=["GET", "POST"])
def edit_type(type_id):
    if request.method == "POST":
        type = {
            "type_name": request.form.get("type_name"),
            "type_description": request.form.get("type_description"),
        }
        flash("You have updated an Event Type")
        mongo.db.types.update_one(
            {"_id": ObjectId(type_id)}, {"$set": type})
    types = mongo.db.types.find().sort("type_name", 1)
    type = mongo.db.types.find_one({"_id": ObjectId(type_id)})
    return render_template("edit_type.html", type=type, types=types)


@app.route("/delete_type/<type_id>", methods=["GET", "POST"])
def delete_type(type_id):
    types = mongo.db.types.find().sort("type_name", 1)
    type = mongo.db.types.find_one({"_id": ObjectId(type_id)})
    flash("Are you sure you want to delete this Event Type?")
    return render_template("delete_type.html", type=type, types=types)


@app.route("/delete_type_confirm/<type_id>")
def delete_type_confirm(type_id):
    mongo.db.types.delete_one({"_id": ObjectId(type_id)})
    flash("Event Type Deleted")
    return redirect(url_for("get_types"))


@app.route("/get_events")
def get_events():
    events = list(mongo.db.events.find())
    return render_template("events.html", events=events)


@app.route("/add_event", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        event_paid_for = "paid" if request.form.get(
            "event_paid_for") else "free"
        event = {
            "added_by": session["user"],
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
            "event_paid_for": event_paid_for
        }

        mongo.db.events.insert_one(event)
        flash("You have added an Event: {{ event_title }}")
        return redirect(url_for("get_events"))
    types = mongo.db.types.find().sort("type_name", 1)
    return render_template("add_event.html", types=types)


@app.route("/edit_event/<event_id>", methods=["GET", "POST"])
def edit_event(event_id):
    if request.method == "POST":
        event_paid_for = "paid" if request.form.get(
            "event_paid_for") else "free"
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
        flash("You have updated an Event")
        mongo.db.events.update_one(
            {"_id": ObjectId(event_id)}, {"$set": submit})
    types = mongo.db.types.find().sort("type_name", 1)
    event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    return render_template("edit_events.html", event=event, types=types)


@app.route("/search_event", methods=["GET", "POST"])
def search_event():
    search_query = request.form.get("search_event")
    events = list(mongo.db.events.find({"$text": {"$search": search_query}}))
    return render_template("events.html", events=events)


@app.route("/contact_page", methods=["GET", "POST"])

def contact_page():

    if request.method == "POST":

        email = {}

        email["name"] = request.form["fname"] + " " + request.form["lname"]
        email["email"] = request.form["email"].replace(" ", "").lower()
        email["subject"] = request.form["subject"]
        email["message"] = request.form["message"]

        send_email(email)
        send_thankyou_email(email)
        flash("Thank you for your email. We will respond as soon as we can")
        return render_template('contact.html')

    return render_template('contact.html')


@app.route("/contact_thankyou", methods=["GET", "POST"])
def contact_thankyou():

    if request.method == "POST":

        email = {}

        email["name"] = request.form["fname"] + " " + request.form["lname"]
        email["email"] = request.form["email"].replace(" ", "").lower()
        email["subject"] = request.form["subject"]
        email["message"] = request.form["message"]

        send_thankyou_email(email)

        return render_template('contact.html')

    return render_template('contact.html')


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


"""Error Handling
As part of Error handling I have redirected the HPPT 404 Not found request
back to the Index Home page, with a flash message informing the user
what they have looked for can't be found
"""


@app.errorhandler(404)
def redirect_http(e):
    flash("We can't find what you searched for, or it can't be loaded")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), debug=True)
