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
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USER_TLS'] = False
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'event_lister@wideworldwebhosting.co.uk'
mail = Mail(app)


mongo = PyMongo(app)


def send_email(email):
    msg = Message("Contact form on Event Lister Website",
                  sender=("Event List Team",
                          "event_lister@wideworldwebhosting.co.uk"),
                  recipients=[email['email']],
                  bcc=["wendybovill@gmail.com"])

    msg.html = """

    <div>
    Hi,
    <br>
    <p>
    We have received an email from {}.
    We will respond as soon as we can.
    <br>The content of the contact form is below:
    <br>
    Name: {}<br>
    Email: {}<br>
    Message: {}<br>
    Kind regards,<br>
    The Event Lister Team.
    </p>
    </div>

    """.format(
        email['name'], email['name'], email['email'], email['message'])

    mail.send(msg)


def sign_up_thankyou(sign_up_email):
    msg = Message("New Sign Up on Event Lister Website",
                  sender=("Event List Team",
                          "event_lister@wideworldwebhosting.co.uk"),
                  recipients=[sign_up_email['email']],
                  bcc=["wendybovill@gmail.com"])

    msg.html = """

    <div>
    <p>Hi {},</p>
    <p>{} thank you for registering on the Event Lister Website.<br>
    You can list your events for free. But first you need to verify<br>
    your email address, then you can login and list your first event!
    <p>You will not be able to login unless you have verified your<br>
    email address first.<br>
    Click the link below to verify your email.</p>
    <p>
    <a href="https://event-lister.herokuapp.com/verify_email/{}" target="_blank">Verify Email</a>
    <p>Don't forget to tell your friends about us!</p>
    <p>The information below is what we received when you signed up:<br>
    Your message: {}</p>
    <p>Kind regards,
    <br>
    The Event Lister Team.
    <br>
    Regards
    </p>
    </div>

    """.format(sign_up_email['username'], sign_up_email['name'],
               sign_up_email['username'], sign_up_email['email'])

    mail.send(msg)


def send_user_email(user_email):
    msg = Message("User Contact Form on Event Lister",
                  sender=("Event List Team",
                          "event_lister@wideworldwebhosting.co.uk"),
                  recipients=[user_email['email']],
                  bcc=["wendybovill@gmail.com"])

    msg.html = """

    <div>
    <p>Hi {},<br>
    <br>The information below is what we received from our contact form:<p>
    <p>Your message: {}</p>
    <p>Kind regards,
    <br>
    The Event Lister Team.
    <br>
    Regards
    </p>
    </div>

    """.format(user_email['username'], user_email['name'],
               user_email['message'], user_email['email'])

    mail.send(msg)


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

        if existing_username:
            flash("That username is taken")
            return redirect(url_for("sign_up"))
        elif existing_email:
            flash("That email address is already registered")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username"),
            "fname": request.form.get("fname").lower(),
            "lname": request.form.get("lname").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(
                request.form.get("password")),
            "verified": "no"
        }
        mongo.db.users.insert_one(sign_up)
        fullname = request.form["fname"] + " " + request.form["lname"]

        sign_up_email = {}

        sign_up_email["name"] = fullname
        sign_up_email["email"] = request.form["email"].replace(" ", "").lower()
        sign_up_email["username"] = request.form["username"]

        sign_up_thankyou(sign_up_email)

        session["user"] = request.form.get("username")
        flashmessage1 = "Thankyou for registering. Please check "
        flashmessage2 = "your emails and verify your email address."

        flash(flashmessage1 + flashmessage2)
        flash("Welcome to BeThere Events!")
        return render_template("index.html")
    return render_template("register.html")


@app.route("/verify_email/<username>", methods=["GET", "POST"])
def verify_email(username):
    if request.method == "POST":
        users = mongo.db.users.find().sort("username", 1)
        user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        verify = "yes" if request.form.get("verified") else "no"

        update = {
            "verified": verify
        }

        mongo.db.users.update_one({"username": username}, {"$set": update})

        users = mongo.db.users.find().sort("username", 1)
        user = mongo.db.users.find_one({"username": username})
        flash("Your email has been verified " + username)
        return redirect(url_for(
            "profile.html", username=username, user=user, users=users))

    users = mongo.db.users.find().sort("username", 1)
    user = mongo.db.users.find_one({"username": username})
    return render_template(
        "verify.html", username=username, user=user, users=users)


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        users = mongo.db.users.find().sort("username", 1)
        user = mongo.db.users.find_one(
            {"username": request.form.get("username")})
        verified = mongo.db.users.find_one({"username": verified})

        if "verified" == "yes":
            users = mongo.db.users.find().sort("username", 1)
            user = mongo.db.users.find_one(
                {"username": request.form.get("username")})
            existing_user = user
            session["user"] = request.form.get("username")
            session_user = session["user"]

            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username")
                user_password == "matches"
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for('profile', username=session['user']))
            elif user_password == "":
                # password not matching
                flash("Please check your login details")
                return redirect(url_for(("log_in")))
            else:
                # user is not found in database
                flash("Please check your login details")
                return redirect(url_for("log_in"))

        else:
            flashmessage1 = "Please check your emails"
            flashmessage2 = " and verify your email address"
            flash(flashmessage1 + flashmessage2)
        
        users = mongo.db.users.find().sort("username", 1)
        session["user"] = request.form.get("username")
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        return render_template("profile.html",
                               username=username,
                               user=user, users=users)

    session["user"] = request.form.get("username")
    flash("Welcome to BeThere! Events")
    return render_template("login.html")


@app.route("/log_out/<username>")
def log_out(username):
    users = mongo.db.users.find().sort("username", 1)
    user = mongo.db.users.find_one({"username": username})
    # redirect to confirmation page
    flash("Are you sure you want to log out?")
    return render_template(
        "log_out_confirm.html", username=username, user=user, users=users)


@app.route("/log_out_confirm/<username>")
def log_out_confirm(username):
    users = mongo.db.users.find().sort("username", 1)
    user = mongo.db.users.find_one({"username": username})
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
        email["message"] = request.form["message"]

        send_email(email)
        flash("Thank you for your email. We will respond as soon as we can")
        return render_template('contact.html')

    return render_template('contact.html')


@app.route("/user_contact_page/<username>", methods=["GET", "POST"])
def user_contact_page(username):
    existing_username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    session["user"] = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    users = mongo.db.users.find().sort("username", 1)
    user = mongo.db.users.find_one({"username": username})

    if request.method == "POST":
        fullname = request.form["fname"] + " " + request.form["lname"]
        user_email = {}
        user_email["username"] = existing_username
        user_email["name"] = fullname
        user_email["message"] = request.form["message"]
        user_email["email"] = user["email"]

        flashmessage1 = "Thank you for your email " + username
        flashmessage2 = ". We will respond as soon as we can"

        send_user_email(user_email)
        flash(flashmessage1 + flashmessage2)

        return render_template(
            "user_contact.html", username=username, user=user, users=users)
    users = mongo.db.users.find().sort("username", 1)
    user = mongo.db.users.find_one({"username": username})
    return render_template(
            "user_contact.html", username=username, user=user, users=users)


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
