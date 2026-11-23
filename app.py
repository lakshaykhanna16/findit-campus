
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os

from extensions import db
from models import Item


app = Flask(__name__)

# Secret key for flash messages and sessions
app.config["SECRET_KEY"] = "findit-development-key"

# Database configuration
# Vercel can only write to /tmp, so the database goes there when deployed.
# Locally it stays in the instance/ folder.
if os.environ.get("VERCEL"):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/items.db"
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///items.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialise database
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/browse-items")
def browse():
    items = Item.query.all()
    return render_template("browse-items.html", items=items)


@app.route("/report-items", methods=["GET", "POST"])
def report():

    if request.method == "POST":

        # Convert form date into Python date format
        item_date = datetime.strptime(
            request.form["date"], "%Y-%m-%d"
        ).date()

        # Create a new item
        new_item = Item(
            item_name=request.form["item_name"],
            category=request.form["category"],
            status=request.form["status"],
            location=request.form["location"],
            date=item_date,
            description=request.form["description"]
        )

        # Save item to database
        db.session.add(new_item)
        db.session.commit()
        
        # Show success message
        flash("Your item has been reported successfully!", "success")

        # Redirect back to report page
        return redirect(url_for("report"))

    # Display report form (GET request)
    return render_template("report-items.html")


if __name__ == "__main__":
    app.run(debug=True)
