import math  # Importing the math module for mathematical operations
import random  # Importing the random module to generate random numbers

# Function to check if a value can be converted to a float


def isfloat(x):
    try:
        float(x)  # Try converting the value to a float
        return True  # If successful, return True
    except ValueError:
        return False  # If conversion fails, return False

# Function to check if a value can be converted to an integer


def isint(n):
    try:
        int(n)  # Try converting the value to an integer
        return True  # If successful, return True
    except ValueError:
        return False  # If conversion fails, return False

# Function to calculate the factorial of a number


def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i  # Multiply fac by each number up to n
    return fac

# Function to calculate the sine of x using a series expansion


def sin_f(x, n):
    result = 0
    for i in range(0, n + 1):
        result += pow(-1, i) * pow(x, 2 * i + 1) / \
            factorial(2 * i + 1)  # Add each term of the series
    print(result)  # Print the result

# Function to calculate the cosine of x using a series expansion


def cos_f(x, n):
    result = 0
    for i in range(0, n + 1):
        result += pow(-1, i) * pow(x, 2 * i) / \
            factorial(2 * i)  # Add each term of the series
    print(result)  # Print the result

# Function to calculate the hyperbolic sine of x using a series expansion


def sinh_f(x, n):
    result = 0
    for i in range(0, n + 1):
        # Add each term of the series
        result += pow(x, 2 * i + 1) / factorial(2 * i + 1)
    print(result)  # Print the result

# Function to calculate the hyperbolic cosine of x using a series expansion


def cosh_f(x, n):
    result = 0
    for i in range(0, n + 1):
        # Add each term of the series
        result += pow(x, 2 * i) / factorial(2 * i)
    print(result)  # Print the result


# Main code execution
x = input("x = ")  # Get user input for x
n = input("n = ")  # Get user input for n
if isint(n) and isfloat(x):  # Check if the inputs are valid numbers
    x = float(x)  # Convert x to float
    n = int(n)  # Convert n to int
    # Get the function name from user
    func_name = input("Input function (sin / cos / sinh / cosh): ")
    # Call the corresponding function based on user input
    if func_name == "sin":
        sin_f(x, n)
    elif func_name == "cos":
        cos_f(x, n)
    elif func_name == "sinh":
        sinh_f(x, n)
    elif func_name == "cosh":
        cosh_f(x, n)
