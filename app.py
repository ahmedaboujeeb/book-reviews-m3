import os
from flask import (Flask, render_template, 
flash, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
if os.path.exists("env.py"):
    import env
# Required libraries imported


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Login required security feature
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" in session and session ["user"] is not None:
            return f(*args, **kwargs)
        return redirect(url_for('login', next=request.url))
    return decorated_function


# Route to home page
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

# Route to reviews page
@app.route("/reviews")
def reviews():
    reviews = mongo.db.reviews.find()
    return render_template("reviews.html", reviews=reviews)


# Search functionality
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    reviews = list(mongo.db.reviews.find({"$text": {"$search": query}}))
    return render_template("reviews.html", reviews=reviews)


# Sign up functionality
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
             {"username": request.form.get("username").lower()})

        # if user already exists show warning msg
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))

        signup = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
    }
        mongo.db.users.insert_one(signup)

        session["user"] = request.form.get("username").lower()
        flash("You are signed up!")
        return redirect(url_for("account", username=session["user"]))

    return render_template("signup.html")


# Login functionality
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # Confirm password/username match user input
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Logged In!")
                    return redirect(url_for("account", username=session["user"]))

            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Account page
@app.route("/account/<username>", methods=["GET", "POST"])
@login_required
def account(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("account.html", username=username)

    return redirect(url_for("login"))


# Log out functionality
@app.route("/logout")
def logout():
    flash("Logged Out!")
    session.pop("user")
    return redirect(url_for("login"))


# Add review functionality
@app.route("/add_review", methods=["GET", "POST"])
@login_required
def add_review():
    if request.method == "POST":
        review = {
            "genre": request.form.get("genre"),
            "book_name": request.form.get("book_name"),
            "author_name": request.form.get("author_name"),
            "image_link": request.form.get("image_link"),
            "review": request.form.get("review"),
            "review_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for("add_review"))

    return render_template("add_review.html")


# Review page
@app.route("/review_page/<review_id>")
def review_page(review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("review_page.html", review=review)


# Edit review functionality
@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
@login_required
def edit_review(review_id):
    if request.method == "POST":
        submit = {
            "genre": request.form.get("genre"),
            "book_name": request.form.get("book_name"),
            "author_name": request.form.get("author_name"),
            "image_link": request.form.get("image_link"),
            "review": request.form.get("review"),
            "review_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Updated")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("edit_review.html", review=review)


# Delete review functionality
@app.route("/delete_review/<review_id>")
@login_required
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("reviews"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
