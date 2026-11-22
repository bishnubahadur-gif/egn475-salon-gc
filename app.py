# Import Flask to build a simple web application.
import os
from decimal import Decimal

import db
from db import get_db
from flask import Flask, render_template, abort, redirect, request, url_for

# Create the Flask application with its templates and static folders.
app = Flask(__name__)
app.config["DATABASE"] = os.path.join(app.instance_path, "salon.sqlite")
os.makedirs(app.instance_path, exist_ok=True)
db.init_app(app)


# Sample salon services for the Flask prototype.
# All prices are stored in cents.
SAMPLE_SERVICES = [
    {"id": 1, "name": "Haircut", "category": "Hair", "price_cents": 3500, "duration": 45},
    {"id": 2, "name": "Hair Coloring", "category": "Hair", "price_cents": 9000, "duration": 120},
    {"id": 3, "name": "Hair Styling", "category": "Styling", "price_cents": 5000, "duration": 60},
    {"id": 4, "name": "Hair Wash", "category": "Hair Care", "price_cents": 2000, "duration": 30},
    {"id": 5, "name": "Deep Conditioning", "category": "Treatment", "price_cents": 4500, "duration": 45},
    {"id": 6, "name": "Blow Dry", "category": "Styling", "price_cents": 3000, "duration": 30},
]
# Sample appointments for the staff calendar.
SAMPLE_APPOINTMENTS = [
    {
        "id": 1,
        "client": "Maya Patel",
        "service": "Haircut",
        "date": "2026-11-18",
        "time": "10:00 AM",
        "stylist": "Alex",
        "status": "Pending"
    },
    {
        "id": 2,
        "client": "Jordan Lee",
        "service": "Hair Styling",
        "date": "2026-11-18",
        "time": "11:30 AM",
        "stylist": "Sam",
        "status": "Confirmed"
    },
    {
        "id": 3,
        "client": "Sofia Garcia",
        "service": "Hair Coloring",
        "date": "2026-11-18",
        "time": "2:00 PM",
        "stylist": "Taylor",
        "status": "Confirmed"
    }
]

# This route opens the home page when someone visits the main URL.
@app.route("/")
def home():
    return render_template("index.html")

# This route opens the About page when someone visits /about.
@app.route("/about")
def about():
    # Display information about the salon and its services.
    return "Nexa Salon provides haircuts, coloring, and styling with convenient appointment booking."
# Display the salon's available services.
@app.route("/services")
def services():
    services = get_db().execute(
        "SELECT id, name, category, price_cents, duration_minutes, "
        "duration_minutes AS duration "
        "FROM services WHERE active = 1 ORDER BY name"
    ).fetchall()

    return render_template(
        "services.html",
        services=services
    )
# Display one salon service using its ID.
@app.route("/services/<int:service_id>")
def service_detail(service_id):
    service = get_db().execute(
        "SELECT id, name, category, price_cents, duration_minutes, "
        "duration_minutes AS duration "
        "FROM services WHERE id = ?",
        (service_id,)
    ).fetchone()

    if service is None:
        abort(404, description="Service not found")

    return render_template("service_detail.html", service=service)


@app.route("/admin/services/new", methods=("GET", "POST"))
def new_service():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if not name:
            return render_template(
                "service_new.html",
                error="Service name is required."
            ), 400

        category = request.form["category"].strip()
        duration_minutes = int(request.form["duration_minutes"])
        price_cents = int(Decimal(request.form["price"]) * 100)

        connection = get_db()
        connection.execute(
            "INSERT INTO services "
            "(name, category, duration_minutes, price_cents) "
            "VALUES (?, ?, ?, ?)",
            (name, category, duration_minutes, price_cents)
        )
        connection.commit()

        return redirect(url_for("services"))

    return render_template("service_new.html")


# Display the appointment booking form.
# Booking information will not be saved until Week 4.
@app.route("/book")
def book():
    return render_template(
        "book.html",
        services=SAMPLE_SERVICES
    )

# Display the staff calendar with sample appointments.
@app.route("/calendar")
def calendar():
    return render_template(
        "calendar.html",
        appointments=SAMPLE_APPOINTMENTS
    )

# Display appointment history using sample data.
@app.route("/appointments")
def appointments():
    return render_template(
        "appointments.html",
        appointments=SAMPLE_APPOINTMENTS
    )
# Display a custom 404 error page.
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404