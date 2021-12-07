
import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from helpers import apology, login_required


# Configure application
app = Flask(__name__, static_url_path="/static")
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
#app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///homerunner.db") 


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
#@login_required
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/about")
def about():
           return render_template("about.html")

@app.route("/map")
def map():
           return render_template("maps.html")

@app.route("/map2")
def map2():
           return render_template("mapscopy.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Contact"""
    if request.method == "POST":

  # Ensure username was submitted
     #   if not request.form.get("name"):
      #      return apology("missing name")
    
        name = request.form.get("name")        
     #   if not request.form.get("email"):
    #        return apology("missing email") 

        email = request.form.get("email")
        phone = request.form.get("phone")
        title = request.form.get("subject")

        if not name or not email or not phone or not title:
            return apology("invalid username and/or password", 403)

        db.execute("INSERT INTO contact_message (Name, Email, Phone, Title) VALUES (?,?,?,?)", name, email, phone, title)    
        return redirect("/")
        

    else:
     return render_template("contact.html")               

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any userName
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Clear session
    session.clear()

    if request.method == "POST":

        # Make sure username provided
        if not request.form.get("username"):
            return apology("missing username")

        # Get username
        username = request.form.get("username")

        # Make sure user doesn't exist
        if len(db.execute("SELECT * FROM users WHERE username = ?", username)) != 0:
            return apology("user already exists")

        # Make sure password & confirmation provided
        if not request.form.get("password") or not request.form.get("confirm_password"):
            return apology("missing password")

        # Get password & confirmation
        password = request.form.get("password")
        confirmation = request.form.get("confirm_password")

        # Make sure password equals confirmation
        if password != confirmation:
            return apology("password and confirmation don't match")

        # Hash password
        password_hash = generate_password_hash(password)

        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        usertype = request.form.get("usertype")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        zipcode = request.form.get("zipcode")
        phone = request.form.get("phone")
        email = request.form.get("email")
        note = request.form.get("note")


        # Add user to users table
        
        #db.execute("INSERT INTO users (username, hash, usertype, firstname, lastname, address, city, state, country, zipcode, phone, email, note) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", username, password_hash, usertype, firstname,lastname,address, city, state, country, zipcode, phone, email, note)

        try:
            id = db.execute("INSERT INTO users (username, hash, usertype, firstname, lastname, address, city, state, country, zipcode, phone, email, note) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", username, password_hash, usertype, firstname,lastname,address, city, state, country, zipcode, phone, email, note)

        except ValueError:
            return apology("username taken")

          # Log user in
        session["user_id"] = id

        # Let user know they're registered
        flash("Registered!")

        return redirect("/")
       
    else:
        return render_template("register.html")

@app.route("/userinput", methods=["GET", "POST"])
@login_required
def userinput():
    """userinput"""
    if request.method == "POST":

        username = request.form.get("username")
        requestnote = request.form.get("resource")
        location = request.form.get("location")

        if not username or not requestnote or not location:
            return apology("invalid entry", 403)

        db.execute("INSERT INTO requests (location, username, requestnote) VALUES (?,?,?)", location, username, requestnote)    
        return redirect("/")

    else:
        return render_template("userinput.html")               

@app.route("/fridge", methods=["GET", "POST"])
@login_required
def fridge():
    if request.method == "POST":
        firstname = request.form.get("fname")
        lastname = request.form.get("lname")
        note = request.form.get("food")

       #check if input
        if not firstname:
            return apology("must provide firstname", 403)
        
        elif not lastname:
            return apology("must provide lastname", 403)

        elif not note:
            return apology("must provide note", 403)
        
        db.execute("INSERT INTO posts (firstname, lastname, note, location) VALUES (?,?,?,?)")
        # print index page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("fridge.html")
#def errorhandler(e):
    #"""Handle error"""
    #if not isinstance(e, HTTPException):
        #e = InternalServerError()
    #return apology(e.name, e.code)


#Listen for errors
#for code in default_exceptions:
    #app.errorhandler(code)(errorhandler)


