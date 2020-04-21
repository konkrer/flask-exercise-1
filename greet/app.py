from flask import Flask


app = Flask(__name__)


@app.route("/welcome")
def welcome():
    """Welocome page."""
    return "welcome"


@app.route("/welcome/home")
def welcome_home():
    """Welocome home page."""
    return "welcome home"


@app.route("/welcome/back")
def welcome_back():
    """Welocome back page."""
    return "welcome back"
