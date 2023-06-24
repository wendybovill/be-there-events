""" Module Purpose:

    This module is the main module that runs the app's
    basic and extended functions. Without this the app
    will not run. Pep8 requirements are adhered to.

App description:

    The app is created to be an Event Lister, for users to list
    their events for free. There is a login required for a user
    to add an event. However the events listed are viewable by
    the a site visitor. In order to receive a login, a user has
    to sign up. They then receive an email to verify email address.
    After verification, they are logged into their user profile.

    Each member can add and event and an event type. But each user
    is restricted to only edit or update or delete their own event
    and event type.

    Events are searchable by the title, descriptions and if its
    'paid' or 'free'.

    There is one 'admin' user, who is allowed to edit, update, and
    delete other members events, event types, as well as their
    profiles, and admin can also delete a member by ID.

    Members can edit their own profiles but not profiles of others.

Each route and function is explained in doc strings, as well as
information on the next route/function called.

"""


import os
import pathlib
import time
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


"""

App configurations for Database

"""


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


"""

App configurations for Email Sending

"""


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
    """
    Email types defined for Contact forms:

    Email template sending contact form for logged out user

    """
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
    """
    Email types defined for Contact forms:

    Email template for email to thank user for signing up.
    Sent to user and admin.

    The a link below cannot be shortened or url doesn't work.
    Therefore complaint of 'too long' is ignored.

    """
    msg = Message("New Sign Up on BeThere! Events",
                  sender=("Event List Team",
                          "event_lister@wideworldwebhosting.co.uk"),
                  recipients=[sign_up_email['email']],
                  bcc=["wendybovill@gmail.com"])

    msg.html = """

    <div>
    <p>Hi {},</p>
    <p>{} thank you for registering on BeThere! Events Website.<br>
    You can list your events for free. But first you need to verify<br>
    your email address, then you can login and list your first event!
    </p>
    <p><em>Please remember your username and password.</em><br>
    <br>These are Case Sensitive. eg. Username must match {}<br>
    Click the link below to verify your email.</p>
    <p>
    <a href="https://event-lister.herokuapp.com/verify_email/{}" target="_blank">Verify Email</a>
    <p>Don't forget to tell your friends about us!</p>
    <p>Kind regards,
    <br>
    The Event Lister Team.
    <br>
    Regards
    </p>
    </div>

    """.format(sign_up_email['username'], sign_up_email['name'],
               sign_up_email['username'], sign_up_email['username'],
               sign_up_email['email'])

    mail.send(msg)


def send_user_email(user_email):
    """
    Email types defined for Contact forms:

    Email template for contact form for logged in user.
    Sent to user and admin.

    """
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
    """
    Sign Up route and functions:

    The user is found in the database when the form
    posts the users name, and it is then retrieved
    along with the email addres.

    This is compared with the database to see if there
    is a match to an existing username or email address.
    If there is the user is notified and has to change
    it or login. If there is no username match the user
    is registered and sent an email to verify their
    email address.

    They are notified of a successful sign up on the page
    using the email 'sign_up_thankyou' template.

    """
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
    """
    Route & functions to Verify Email Address:

    The email the user received when signing up contains
    a url to verify their email. They will only receive
    this if their email address was valid.

    They fill in the form the url takes them to and they are
    then logged in. They need to enter the same details they to
    register. The user is given feedback in the page.

    If the user can't be found or their username is different
    they are informed of a login error and told to check their
    details.

    Upon subission of the verification form they are redirected
    to their profile page.

    """
    if request.method == "POST":
        user = mongo.db.users.find_one(
                    {"username": request.form.get("username")})
        username = mongo.db.users.find_one(
                    {"username": request.form.get("username")})
        verify = "yes" if request.form.get("verified") else "no"

        update = {

            "verified": verify
        }

        mongo.db.users.update_one(
            {"username": request.form.get("username")}, {"$set": update})

        flash("Your email has been verified " + request.form.get("username"))

        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get(
                        "password")):
                session["user"] = request.form.get("username")
                flash("Welcome, {}".format(
                    request.form.get("username")))
                users = mongo.db.users.find().sort("username", 1)
                user = mongo.db.users.find_one({"username": username})
                username = mongo.db.users.find_one(
                    {"username": session["user"]})["username"]
                return render_template(
                    "profile.html", username=username, user=user, users=users)

        users = mongo.db.users.find().sort("username", 1)
        user = mongo.db.users.find_one({"username": username})
        session["user"] = request.form.get("username")
        username = mongo.db.users.find_one(
                {"username": session["user"]})["username"]
    return render_template(
        "verify.html", username=username)


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    """
    Route & functions to Log in:

    The users email address and password are compared to
    what is stored in the database, from checking and
    comparing the login form info to the users database info.

    If their details match they are logged in and redirected
    to their profile page. If they do not match the user is
    notified of needing to check their details on the login
    page.

    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})
        username = existing_user
        users = mongo.db.users.find().sort("username", 1)
        user = mongo.db.users.find_one({"username": username})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get(
                        "password")):
                session["user"] = request.form.get("username")
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return render_template(
                    "profile.html", username=username, user=user, users=users)
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


@app.route("/log_out/<username>")
def log_out(username):
    """
    Route and functions to Log out:

    The user requests to logout in the menu.
    The user is directed to a page to confirm
    if they really want to log out.

    """
    users = mongo.db.users.find().sort("username", 1)
    user = mongo.db.users.find_one({"username": username})
    # redirect to confirmation page
    flash("Are you sure you want to log out?")
    return render_template(
        "log_out_confirm.html", username=username, user=user, users=users)


@app.route("/log_out_confirm/<username>")
def log_out_confirm(username):
    """
    Route and functions to Confirm Log out:

    In this view the user has to confirm
    if they really want to log out. The user
    clicks confirm or cancel. If confirmed
    they are then logged out of the session.
    If they cancel the log out they are redirected
    to the events page.

    """
    users = mongo.db.users.find().sort("username", 1)
    user = mongo.db.users.find_one({"username": username})
    session.pop("user")
    flash("You are now logged out.")
    return redirect(url_for("get_events"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Route  and functions for a user to view their profile:

    Upon login the user is redirected to their profile page.
    They can also access their profile page in the menu,
    once logged in.

    Upon choosing 'Profile' in the navigation menu:
    The user is directed to their profile view.
    In the profile view, they can see the basic details they entered
    and have the option to edit them or add more.

    The site admin has access to view all the members profiles
    and edit them if there is a security concern.

    """
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    users = mongo.db.users.find().sort("username", 1)
    user = mongo.db.users.find_one({"username": username})

    if session["user"]:

        return render_template(
            "profile.html", username=username, user=user, users=users)

    flash("You are not logged in, please log in")
    return redirect(url_for("home"))


@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username):
    """
    Route  and functions for a user to Edit their profile:

    In this view, the user form is made available where they
    can see the basic details they previously entered
    and have the option to Edit them or add more.

    The site admin has access to Edit all the members profiles
    and edit them if there is a security concern.

    """
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

        users = mongo.db.users.find().sort("username", 1)
        user = mongo.db.users.find_one({"username": username})
        username = user
        flash("Your Profile has been updated " + request.form.get("username"))
        return render_template(
            "profile.html", username=username, user=user, users=users)

    users = mongo.db.users.find().sort("username", 1)
    user = mongo.db.users.find_one({"username": username})
    return render_template(
        "edit_profile.html", username=username, user=user, users=users)


@app.route("/get_types")
def get_types():
    """
    Route and functions to get the Event Types:

    Each Event is allocted a 'type of event' by the member
    who is creating the event. 
    The get types view allows the user to view the event types
    in a list format. If there is one they have created
    they are then given the option to view or edit their event type.

    """
    types = list(mongo.db.types.find().sort("type_name", 1))
    return render_template("types.html", types=types)


@app.route("/add_type", methods=["GET", "POST"])
def add_type():
    """
    Route and functions to Add an Event Type:

    A form is offered to the user to add an event type.
    The fields from this form is retrieved and then sent
    to the database to be stored. This is then listed in
    the view 'get_types' above.

    """
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
    """
    Route and functions to get Edit an Event Type:

    Each event type has buttons to edit the event type.
    Only the user who created the event type or the user 'admin'
    can view these buttons. On Editing the event type, the
    new form data is retrieved and that event type is updated in
    the database by its id. Feedback flash message is sent to user.

    """
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
    """
    Route and functions to get Delete an Event Type:

    Each event type has buttons to delete the event type.
    Only the user who created the event type or the user 'admin'
    can view these buttons. On selecting delete button the user is
    directed to a page that asks the user to confirm if they want
    to delete that event type.

    """
    types = mongo.db.types.find().sort("type_name", 1)
    type = mongo.db.types.find_one({"_id": ObjectId(type_id)})
    flash("Are you sure you want to delete this Event Type?")
    return render_template("delete_type.html", type=type, types=types)


@app.route("/delete_type_confirm/<type_id>")
def delete_type_confirm(type_id):
    """
    Route and functions to Confirm to Delete an Event Type:

    Each event type has buttons to delete the event type.
    Only the user who created the event type or the user 'admin'
    can view these buttons. A view to confirm delete is loaded 
    in the page, if the user selects 'delete' the event type
    by its id, is deleted. If the user select cancel the
    event type is not cancelled. In either instance the
    user is redirected by to the 'get_types' view.

    """
    mongo.db.types.delete_one({"_id": ObjectId(type_id)})
    flash("Event Type Deleted")
    return redirect(url_for("get_types"))


@app.route("/get_events")
def get_events():
    """
    Route to Events Listed:
    The events are retrieved from the database and listed using 
    loops within the view template.
    The Events are publically accessible. They can be searched.

    Only logged in members can add, edit and delete their own
    events.

    Admins have access to all the Events to be able to edit or
    delete them if necessary due to security concerns.

    """
    events = list(mongo.db.events.find())
    return render_template("events.html", events=events)


@app.route("/add_event", methods=["GET", "POST"])
def add_event():
    """
    Route to Add an Event:
    There is a form that gets filled in for the user to add
    an event. This information is retrieved from the form and 
    then inserted into the database. The user is returned to
    the Event list view after adding their event.
    Only logged in members can add an event.

    """
    if request.method == "POST":
        event_paid_for = "paid" if request.form.get(
            "event_paid_for") else "free"
        event = {
            "added_by": session["user"],
            "event_type": request.form.get("event_type").title(),
            "event_title": request.form.get("event_title").title(),
            "event_date": request.form.get("event_date"),
            "event_time": request.form.get("event_time"),
            "event_description": request.form.get("event_description"),
            "event_location_town": request.form.get(
                "event_location_town").title(),
            "event_location_postcode": request.form.get(
                "event_location_postcode").upper(),
            "event_organiser": request.form.get(
                "event_organiser").title(),
            "event_contact_details": request.form.get(
                "event_contact_details").title(),
            "event_url": request.form.get("event_url"),
            "event_entrance_fee": request.form.get("event_entrance_fee"),
            "event_paid_for": event_paid_for
        }

        mongo.db.events.insert_one(event)
        flash("You have added an Event: " + request.form.get(
            "event_title").title())
        return redirect(url_for("get_events"))

    types = mongo.db.types.find().sort("type_name", 1)
    return render_template("add_event.html", types=types)


@app.route("/edit_event/<event_id>", methods=["GET", "POST"])
def edit_event(event_id):
    """
    Route to Edit event:
    The event selected is retrieved from the database using their ID
    and displayed in a form.

    Only logged in members can add, edit and delete their own
    events. The button to edit is hidden from a user that
    doesn't match the user who created the event or doesn't
    match 'admin' user.

    The form data is retrieved from the form and the the
    database is updated according to the event ID.

    """
    if request.method == "POST":
        event_paid_for = "paid" if request.form.get(
            "event_paid_for") else "free"
        submit = {
            "event_type": request.form.get("event_type").title(),
            "event_title": request.form.get("event_title").title(),
            "event_date": request.form.get("event_date"),
            "event_time": request.form.get("event_time"),
            "event_description": request.form.get("event_description"),
            "event_location_town": request.form.get(
                "event_location_town").title(),
            "event_location_postcode": request.form.get(
                "event_location_postcode").upper(),
            "event_organiser": request.form.get("event_organiser").title(),
            "event_contact_details": request.form.get(
                "event_contact_details").title(),
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


@app.route("/delete_event/<event_id>", methods=["GET", "POST"])
def delete_event(event_id):
    """
    Route to Delete event:
    The event selected is retrieved from the database using their ID
    and displayed to the user

    Only logged in members can delete their own
    events. The button to edit is hidden from a user that
    doesn't match the user who created the event or doesn't
    match 'admin' user.

    If the user selects to delete the event they are directed
    to a view to confirm if they want to delete the event.

    """
    types = mongo.db.types.find().sort("type_name", 1)
    event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    flash("Are you sure you want to delete this event?")
    return render_template("delete_event.html", event=event, types=types)


@app.route("/delete_event_confirm/<event_id>")
def delete_event_confirm(event_id):
    """
    Route to Confirm delete of an event:

    Only logged in members can delete their own
    events. The button to edit is hidden from a user that
    doesn't match the user who created the event or doesn't
    match 'admin' user.

    The view to confirm delete offers the user an option
    to cancel or to delete. Both options return the user to 
    the get_events view. Selecting 'Yes' to delete, removes
    the event from the database by its ID.

    """
    mongo.db.events.delete_one({"_id": ObjectId(event_id)})
    flash("Event Deleted")
    return redirect(url_for("get_events"))


@app.route("/search_event", methods=["GET", "POST"])
def search_event():
    """
    Route and function to Search Events:

    This view is publically accessible.
    The search is requested in the search form. A search
    index is created in the database. This expires after 2 minutes
    if another search is not performed to extend it. This allows
    for members to add new events that are then immediately searchable.
    Its enough time for a user to search the events, note the events and
    leave the page. If they then search for new events and another member
    has just added one, that will be included in the new search results.

    The search index is dropped after 2 minutes. If there is an existing
    search and the search is requested again, the results are on the
    previous search index. After 2 minutes the index is dropped to allow
    for an updated index to be created on the next search.

    NB: The method below that creates the index is shown as an error here
    in python due to the length, but also due to no whitespace after comma.
    This has been ignored because Mongodb requires the command without 
    whitespaces after the comma, and without the array split by bracket.
    The same applies to the drop index method.

    """
    if request.method == "POST":

        search_term = request.form.get("search_event")
        """ The method below cannot have its array split
            or whitespace added to it, though 'too long',
            if it is split or whitespace added by the comma's
            it will not create the index.

        """
        mongo.db.events.create_index(
            [("event_title","text"),("event_type","text"),("event_date","text"),("event_paid_for","text"),("event_time","text"),("event_description","text"),("event_location_town","text"),("event_location_postcode","text")])

        events = list(
            mongo.db.events.find(
                {"$text": {"$search": search_term}}))

        if events is None:
            flash("There are no results for that search")
            search_completed = False
            return render_template("events.html", events=events)
        else:
            if events:
                search_completed = True
            return render_template("events.html", events=events)
        """ The method below cannot have its array split
            or whitespace added to it, though 'too long',
            if it is split or whitespace added by the comma's
            it will not create the index.

        """
        if search_completed:
            time.sleep(120)
            mongo.db.events.drop_index(
                'event_title_text_event_type_text_event_date_text_event_paid_for_text_event_time_text_event_description_text_event_location_town_text_event_location_postcode_text')

        return render_template("events.html", events=events)
    return


@app.route("/contact_page", methods=["GET", "POST"])
def contact_page():
    """
    Route to public contact page:

    A contact form is in the view for the logged out user
    to send an email. The user is required to fill in all
    details including email address, first name, last name,
    message. The data is retrieved from the form and forwarded 
    to the send_email function, which uses the logged out
    user contact template.

    This calls the send email function defined in the
    start of this file. It is used by a visitor to send
    and email, or by a member who is not logged in.

    The user is given feedback about their email sent,
    and receive a copy of their email.

    """
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
    """
    Route to member contact page:

    This calls the send email function defined in the
    start of this file. This view is for the logged
    in member to send an email to the admin. They
    receive a copy of their email. Their email address,
    username and fullname are already included in the
    send function. All the have to do is write the message
    and submit the form.
    The member is given feedback about their email and
    they receive a copy of their email sent.

    """
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


@app.route("/view_members")
def view_members():
    """
    Route to view members is for Admin only:

    This lists the site members by Username, Email Address,
    their ID and says if their email is verified or not.

    Knowing if the user is not verified, allows the Admin
    to send an email requesting they verify their email,
    and also allows the admin to keep an eye on them in
    case they misuse the site, the admin then can delete
    the member. If the member subsequently verifies their
    email address, this will show in their profile for the
    admin to see.

    Future development will include the setting a function
    to prevent the user logging in if their email is not
    verified.

    The Admin can view, edit or delete the members profiles
    if they feel the site is being misused.

    Most of the user functions search for users by username.
    The editing of the members and deleting of the members
    is performed by search using the user ID. This is incase
    their usernames are similar

    """
    users = list(mongo.db.users.find().sort("username", 1))
    return render_template(
        "view_members.html", users=users)


@app.route("/edit_member/<user_id>", methods=["GET", "POST"])
def edit_member(user_id):
    """
    Route to edit members is for Admin only:

    The edit button allows the 'admin' user to edit the
    profile form fields for the member. There isthe option
    cancel. The update button calls the update function
    which retrieves the data from the form an updates
    the single member by their ID.

    """
    if request.method == "POST":
        verify = "yes" if request.form.get("verified") else "no"

        update = {
            "username": request.form.get("username"),
            "fname": request.form.get("fname").title(),
            "lname": request.form.get("lname").title(),
            "email": request.form.get("email").lower(),
            "address_1": request.form.get("address_1").title(),
            "address_2": request.form.get("address_2").title(),
            "town": request.form.get("town").title(),
            "postcode": request.form.get("postcode").upper(),
            "phone": request.form.get("phone").lower(),
            "verified": verify
        }

        mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": update})

        flash("The member " + request.form.get("username") + " is updated")

    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("edit_member.html", user=user)


@app.route("/delete_member/<user_id>")
def delete_member(user_id):
    """
    Route to delete a member is for Admin only:

    The view to delete a member has a button that calls
    the function to load the view which  calls the delete
    member confirm view.

    """
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    flash("Are you sure you want to delete this member?")
    return render_template(
        "delete_member.html", user=user)


@app.route("/delete_member_confirm/<user_id>")
def delete_member_confirm(user_id):
    """
    Route to confirm member delete is for Admin only:

    There is a button to cancel and a button to delete
    me mber. Both options redirect to 'view members' after.
    Delete removed the single member from the database by their ID.

    """
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    flash("Member Deleted")
    return redirect(url_for(
        "view_members"))


""" Error Handling:

As part of Error handling I have redirected all HTTP Error responses
back to the Index Home page, with a flash message giving information
to the user and instructing them how to proceed where necessary

"""


@app.errorhandler(404)
def redirect_http(e):
    msg1 = " We can't find what you searched for, or it can't be loaded."
    msg2 = " If this is an error please contact us."
    flash(msg1 + " " + msg2)
    return render_template("index.html")


@app.errorhandler(500)
def redirect_http(e):
    msg1 = " There is a problem with that request. Are you logged in?"
    msg2 = " If you think its an error please contact us."
    flash(msg1 + " " + msg2)
    return render_template("index.html")


@app.errorhandler(403)
def redirect_http(e):
    msg1 = " What you have requested to do is not allowed."
    msg2 = " If you think its an error please contact us."
    flash(msg1 + " " + msg2)
    return render_template("index.html")


@app.errorhandler(401)
def redirect_http(e):
    msg1 = " What you have requested to do is not allowed."
    msg2 = " If you think its an error please contact us."
    flash(msg1 + " " + msg2)
    return render_template("index.html")


@app.errorhandler(405)
def redirect_http(e):
    msg1 = " That method is not allowed."
    msg2 = " If you think its an error please contact us."
    flash(msg1 + " " + msg2)
    return render_template("index.html")


@app.errorhandler(400)
def redirect_http(e):
    msg1 = " Its bad. Its a 400 Error."
    msg2 = " The server did not like it."
    flash(msg1 + " " + msg2)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), debug=False)
