from flask import Flask;
from flask import render_template;

# Create an instance of Flask named app
#   This controls the webpage server to serve the client with pages, data, and more.
app = Flask(__name__)


# Index Page
#   Serves index.html to the client
@app.route("/")
def index(name=None):
  return render_template("index.html", person=name)


@app.route("/dollar-amount")
def dollarAmount(dollarAmount=0):
  return dollarAmount