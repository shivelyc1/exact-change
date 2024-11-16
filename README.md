# Exact Change

## Overview

The goal of this program is to calculate the dollars and coins (denominations) of a dollar amount. The program will then display the different denominations and the amounts to equal the dollar amount given. The website will visually show the denominations and collect user input. The server will handle the calculations and return it back to the client to be displayed.

## Requirements

Python 13.6

## Dependencies

Main dependencies in the project.

- [Flask](https://flask.palletsprojects.com/en/stable/) - used to host html templates with python
- [waitress](https://flask.palletsprojects.com/en/stable/deploying/waitress/) - Used to run a production version of the server

## How to start the project?

### Easy Development Server

1. Clone the project onto your system.
2. Open a terminal and cd into the directory of the files.
3. run `pip install -r requirements.txt`
4. To start the server, run `flask --app server run`
5. The terminal should display an IP address to access the website. Paste this IP into your browser.

### Production Server

1. Clone the project onto your system.
2. OPen a terminal and cd into the directory of the files.
3. run `pip install -r requirements.txt`
4. To start the server, run `python server.py`
5. The terminal should display an IP address to acces the website. Paste this IP into your browser.

You can change the host and port of the server in the **server.py** file.

All set!

## Running Tests

The tests are set up using the `unittest` library built in to python.

To run a specific test, you can run a command like this in the terminal.
`python -m unittest tests/test_something.py`

Change the file path to the specific test file you want to test.

**exact_change_tests.py**
`python -m unittest tests/exact_change_test.py`

## server.py

**server.py** is using flask to host the website. This creates and app using the `Flask` class which holds endpoints to `/` and `/dollar-amount`.

`/` is the index of the website where the form for user input is displayed and where the denominations are displayed. You can enter a dollar amount in the input field and click submit to calculate the denominations.

`/dollar-amount` is the endpoint used to send a request to the server to calculate the denominations. Its payload contains the dollarAmount which should be validated to be only two decimal places. If this requirement isn't met, the methods that calculate the denominations will round up to the second decimal place. The endpoint will return a dictionary of the different denominations and the dollarAmount.

The server is set up to handle error codes and render those accordingly.

## exact_change.py

**exact_change.py** is responsible for calculating the denomination quantities for a specific dollar amount. This holds helper functions to organize the code.

`def CalcDenominationQuantity(dollarAmountInCents: int, denominationValue: DenominationValue) -> int`

This function is used to calculate the quantity of the denomination contained in the dollarAmountInCents.

`def isValidDollarAmount(dollarAmount: float) -> bool`

This function checks if the dollarAmount >= 0 before converting to cents

`def CalculateExactChange(dollarAmount: int) -> DenominationsType raises InvalidDollarAmountRange`

This function will calculate each denominations and return a dictionary of DenominationsType. If dollarAmount is < 0, InvalidDollarAmountRange is raised. dollarAmount will be rounded up to the hundredth and then convert the dollarAmount to cents.

## denomination_values.py

**denomination_values.py** has an enum holding the values for each denomination and its value in USD.

```
class DenominationValues(Enum):

  HUNDRED = 10000
  FIFTY = 5000
  TWENTY = 2000
  TEN = 1000
  FIVE = 500
  ONE = 100
  QUARTER = 25
  DIME = 10
  NICKEL = 5
  PENNY = 1
```

## denominations_type.py

**denominations_type.py** has a TypedDict for the return type of **CalculateExactChange()**.

```
class DenominationsType(TypedDict):

  hundreds: int
  fifties: int
  twenties: int
  tens: int
  fives: int
  ones: int
  quarters: int
  dimes: int
  nickels: int
  pennies: int
```

## exact_change_test.py

**exact_change_test.py** hold all the TestCases for the method in **exact_change.py** file.

## templates

This folder is used for html templates for **Flask** to use. This currently has **index.html** which is sent to the client with endpoint `/`

## static

This folder is used for javascript, css, images, etc. **Flask** will use this if the templates are linking to files. For example,

`<link href="{{ url_for('static', filename='styles/style.css')}}" rel="stylesheet" />`

**Flask** can reference static files in the html templates using url_for().
