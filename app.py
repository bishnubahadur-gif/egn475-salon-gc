from flask import Flask

app = Flask(__name__, static_folder=None)


@app.route("/")
def home():
	return "Welcome to Nexa Salon"


@app.route("/about")
def about():
	return "Nexa Salon provides haircuts, coloring, and styling with convenient appointment booking."
