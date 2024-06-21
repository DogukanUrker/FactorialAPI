# Importing necessary functions and classes from sys, math, and flask modules
from sys import (
    set_int_max_str_digits,
)  # Function to set the maximum number of digits for integer conversion from string
from math import factorial  # Function to calculate the factorial of a number
from flask import (
    Flask,
    jsonify,
)  # Flask class for creating the web application and jsonify for JSON responses

# Setting the maximum number of digits for integer conversion to prevent excessively large inputs
set_int_max_str_digits(0)

# Initializing a Flask application
app = Flask(__name__)


# Defining a route that will trigger the factorial calculation
# This route will match "/calculate/<number>", "/factorial/<number>", and "/<number>"
@app.route("/calculate/<number>")
@app.route("/factorial/<number>")
@app.route("/<number>")
def factorial_route(number):
    # Checking if the input is a numeric string
    if not number.isnumeric():
        return jsonify(
            {"error": "Please enter a valid number"}
        )  # Returning an error response if input is not numeric

    # Converting the input string to an integer
    number = int(number)
    # Checking if the number is negative
    if number < 0:
        return jsonify(
            {"error": "Please enter a positive number"}
        )  # Returning an error response if the number is negative

    # Calculating the factorial of the number and returning it in a JSON response
    return jsonify({"result": factorial(number)})


# Defining an error handler for 404 errors (page not found)
@app.errorhandler(404)
def page_not_found(e):
    return (
        jsonify({"error": "Please enter a valid number"}),
        404,
    )  # Returning an error response for invalid routes


# Running the Flask application in debug mode when this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
