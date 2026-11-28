import os
from werkzeug.utils import secure_filename

from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

from extensions import db
from models import Item

load_dotenv()

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = os.path.join(
    app.root_path, "static", "uploads"
)

# Secret key for flash messages and sessions
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

# Database configuration
database_url = os.environ["DATABASE_URL"]

if database_url.startswith("postgres://"):
    database_url = database_url.replace(
        "postgres://", "postgresql+psycopg://", 1
    )
elif database_url.startswith("postgresql://"):
    database_url = database_url.replace(
        "postgresql://", "postgresql+psycopg://", 1
    )

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
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

        item_name = request.form.get("item_name")
        category = request.form.get("category")
        status = request.form.get("status")
        location = request.form.get("location")
        date = datetime.strptime(
            request.form.get("date"), "%Y-%m-%d"
        ).date()
        description = request.form.get("description")

        # Create the item first
        new_item = Item(
            item_name=item_name,
            category=category,
            status=status,
            location=location,
            date=date,
            description=description
        )

        db.session.add(new_item)
        db.session.commit()

        # Get the uploaded image
        image = request.files.get("item_image")

        if image and image.filename != "":
            filename = secure_filename(image.filename)

            # Give the image a unique filename
            filename = str(new_item.item_id) + "_" + filename

            # Save the image
            image.save(
                os.path.join(app.config["UPLOAD_FOLDER"], filename)
            )

            # Save the filename in the database
            new_item.image_filename = filename
            db.session.commit()

        flash("Item reported successfully!")
        return redirect(url_for("browse"))

    # GET request: show the empty report form
    return render_template("report-items.html")


@app.route("/edit-item/<int:item_id>", methods=["GET", "POST"])
def edit_item(item_id):

    # Find the item using its unique ID
    item = Item.query.get_or_404(item_id)

    if request.method == "POST":

        # Update the existing item's information
        item.item_name = request.form["item_name"]
        item.category = request.form["category"]
        item.status = request.form["status"]
        item.location = request.form["location"]

        # Convert submitted date string into Python date
        item.date = datetime.strptime(
            request.form["date"], "%Y-%m-%d"
        ).date()

        item.description = request.form["description"]

        # Save changes to database
        db.session.commit()

        flash("Item updated successfully!", "success")

        return redirect(url_for("browse"))

    # Display the edit form with existing information
    return render_template("edit-item.html", item=item)


@app.route("/delete-item/<int:item_id>", methods=["POST"])
def delete_item(item_id):

    # Find the item using its ID
    item = Item.query.get_or_404(item_id)

    # Delete the item from the database
    db.session.delete(item)

    # Save the deletion
    db.session.commit()

    # Show success message
    flash("Item deleted successfully!", "success")

    # Return to Browse Items
    return redirect(url_for("browse"))


if __name__ == "__main__":
    app.run(debug=True)
