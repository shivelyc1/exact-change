from flask import Flask, render_template, request, abort;
from exact_change import CalculateExactChange
from return_types.denominations_type import DenominationsType

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
def dollarAmount(value=None):
  
  # Get the dollar Amount from the request
  dollarAmountString = request.args.get("dollarAmount")

  try:
    dollarAmount = float(dollarAmountString)
  except Exception as e:
    print(e)
    abort(400)
  
  # dollarAmount not found in request
  if dollarAmount is None:
    # Return error 400 for bad request
    return abort(400)
  

  # Use dollarAmount and get denominations from function
  denominations: DenominationsType = CalculateExactChange(dollarAmount)

  print(denominations)

  return render_template("denominations.html", 
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

# # Handle error 404 page not found.
# app.errorhandler(404)
# def render404Page():
#   return render_template("404.html"), 404


app.run(debug=True)
