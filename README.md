# Exact Change

## Overview

The goal of this program is to calculate the dollars and coins (denominations) of a dollar amount. The program will then display the different denominations and the amounts to equal the dollar amount given. The website will visually show the denominations and collect user input. The server will handle the calculations and return it back to the client to be displayed.

## Requirements

Python 13.6

## How to start the project?

1. Clone the project onto your system.
2. Open a terminal and cd into the directory of the files.
3. run `pip install -r requirements.txt`
4. To start the server, run `flask --app server run`
5. The terminal should display an IP address to access the website. Paste this IP into your browser.

All set!

## server.py

**server.py** is using flask to host the website. This creates and app using the `Flask` class which holds endpoints to `/` and `/dollar-amount`.

`/` is the index of the website where the form for user input is displayed and where the denominations are displayed. You can enter a dollar amount in the input field and click submit to calculate the denominations.

`/dollar-amount` is the endpoint used to send a request to the server to calculate the denominations. Its payload contains the dollarAmount which should be validated to be only two decimal places. If this requirement isn't met, the methods that calculate the denominations will round up to the second decimal place. The endpoint will return a dictionary of the different denominations

## exact_change.py

## denomination_values.py

## templates

This folder is used for html templates for **Flask** to use. This currently has **index.html** which is sent to the client with endpoint `/`

## static

This folder is used for javascript, css, images, etc. **Flask** will use this if the templates are linking to files. For example,

`<link href="{{ url_for('static', filename='styles/style.css')}}" rel="stylesheet" />`

**Flask** can reference static files in the html templates using url_for().
