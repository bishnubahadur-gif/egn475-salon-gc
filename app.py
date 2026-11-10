# Import Flask to build a simple web application.
from flask import Flask

# Create the Flask app and disable the unused static folder.
app = Flask(__name__, static_folder=None)

# This route opens the home page when someone visits the main URL.
@app.route("/")
def home():
    # Show a welcome message on the home page.
    return "Welcome to Nexa Salon"

# This route opens the About page when someone visits /about.
@app.route("/about")
def about():
    # Display information about the salon and its services.
    return "Nexa Salon provides haircuts, coloring, and styling with convenient appointment booking."