import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask("__name__")

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

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

@app.route("/")
@login_required
def index():
    return render_template("register.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # get firstname, lastname, email, phone, username, password, and confirmation
        firstname = request.form.get("fname")
        lastname = request.form.get("lname")
        email = request.form.get("email")
        phone = request.form.get("phone")
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure password was submitted
        if not firstname:
            return apology("must provide firstname", 400)
            
        # Ensure password was submitted
        elif not lastname:
            return apology("must provide lastname", 400)
        # Ensure password was submitted
        elif not email:
            return apology("must provide email", 400)

        # Ensure password was submitted
        elif not phone:
            return apology("must provide phone", 400)
            
        # Ensure username was submitted
        elif not username:
            return apology("must provide username", 400)

        elif db.execute("SELECT * FROM users WHERE username = ?", username):
            return apology("username in use, try another", 400)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 400)
        
        # Ensure password confirmation was submitted
        elif not confirmation:
            return apology("must provide password confirmation", 400)

        # make sure tha pass/confirmation match
        elif confirmation != password:
            return apology("passwords do not match", 400)
        
        # get hash value and insert with user information
        hash = generate_password_hash(password)
        
        nuser = db.execute("INSERT INTO users (username, hash) VALUES (?,?)", username, hash)
        session["user_id"] = nuser

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # get firstname, lastname, email, phone, username, password, and confirmation
        firstname = request.form.get("fname")
        lastname = request.form.get("lname")
        email = request.form.get("email")
        food = request.form.get("phone")

        # Ensure password was submitted
        if not firstname:
            return apology("must provide firstname", 400)
            
        # Ensure password was submitted
        elif not lastname:
            return apology("must provide lastname", 400)

        # Ensure password was submitted
        elif not email:
            return apology("must provide email", 400)

        # Ensure password was submitted
        elif not food:
            return apology("must provide food", 400)
            
        nuser = db.execute("INSERT INTO users (username, hash) VALUES (?,?)", username, hash)
        session["user_id"] = nuser

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")