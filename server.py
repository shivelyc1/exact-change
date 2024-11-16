from flask import Flask, render_template, request, abort
from waitress import serve
from exact_change import CalculateExactChange
from return_types.denominations_type import DenominationsType
from exceptions.invalid_dollar_amount_range import InvalidDollarAmountRange
# IP of the server. 0.0.0.0 is your local machine.
HOST = "0.0.0.0"

# Port of the server. Change this if port 8000 is being used.
PORT = "5000"

# Create an instance of Flask named app
#   This controls the webpage server to serve the client with pages, data, and more.
app = Flask(__name__, template_folder="templates")
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Index Page
#   Serves index.html to the client
@app.route("/")
def index():
  return render_template("index.html")


@app.route("/dollar-amount")
def dollarAmount():
  
  # Get the dollar Amount from the request
  dollarAmountString = request.args.get("dollarAmount")

  try:
    # Try to parse dollarAmountString to float
    dollarAmount = float(dollarAmountString)
  except InvalidDollarAmountRange as e:
    abort(400)
  except Exception as e:
    print(e)
    abort(500)
  
  # dollarAmount not found in request
  if dollarAmount is None:
    # Return error 400 for bad request
    return abort(400)
  
  # Use dollarAmount and get denominations from function
  denominations: DenominationsType = CalculateExactChange(dollarAmount)

  return render_template("denominations.html", 
    dollarAmount=dollarAmount,
    hundreds=denominations["hundreds"],
    fifites=denominations["fifities"],
    twenties=denominations["twenties"],
    tens=denominations["tens"],
    fives=denominations["fives"],
    ones=denominations["ones"],
    quarters=denominations["quarters"],
    dimes=denominations["dimes"],
    nickels=denominations["nickels"],
    pennies=denominations["pennies"]
  )

# Handle error 404 page not found.
@app.errorhandler(404)
def render404Page(error):
  return render_template("404.html"), 404

# Handle 400 code. Bad data
@app.errorhandler(400)
def display400Code(error):
  return render_template("index.html", code=400, message="Bad data...")

# Handle 500 code. Internal server error
@app.errorhandler(500)
def display500Code(error):
  print(error)
  return render_template("index.html", code=500, message="Internal Server Error...")


if __name__ == "__main__":
  serve(app, host=HOST, port=PORT)
