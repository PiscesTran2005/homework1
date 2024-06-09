import math  # Importing the math module for mathematical operations

# Function to check if a value can be converted to a float (i.e., is a number)
def is_number(x):
    try:
        float(x)  # Try converting the value to a float
        return True  # If successful, return True
    except ValueError:
        return False  # If conversion fails, return False

# Function to compute the ReLU activation function
def relu_f(x):
    if x <= 0:
        return 0  # If x is less than or equal to 0, return 0
    else:
        return x  # Otherwise, return x

# Function to compute the Sigmoid activation function
def sigmoid_f(x):
    return 1/(1+math.exp(-x))  # Calculatethe sigmoid of x

# Function to compute the ELU activation function
def elu_f(x):
    if x <= 0:
        return 0.01*(math.exp(x)-1)  # If x is less than or equal to 0, calculate the ELU of x
    else:
        return x# Otherwise, return x

# Main code execution starts here
x = input("x = ")  # Prompt the user to input a value for x

# Check if the input x is a number
if is_number(x) == True:
    x = float(x)  # Convert the input to a float for mathematical operations
    activation_function = input("sigmoid / relu / elu : ")  # Prompt the user to choose an activation function

    # Call the appropriate activation function based on user input
    if activation_function == "relu":
        print(f"f({x}) = {relu_f(x)}")
    elif activation_function == "sigmoid":
        print(f"f({x}) = {sigmoid_f(x)}")
    elif activation_function == "elu":
        print(f"f({x}) = {elu_f(x)}")
    else:
        print(f"{activation_function} is not supported")  # If the function is not recognized, print an error message
else:
    print("x must be a number")  # If the input x is not a number, print an error message