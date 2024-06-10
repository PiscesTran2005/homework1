import math  # Importing the math module for mathematical operations
import random  # Importing the random module to generate random numbers

# Function to check if a value can be converted to an integer (i.e., is a number)
def isnumeric(x):
    try:
        int(x)  # Try converting the value to an integer
        return True  # If successful, return True
    except ValueError:
        return False  # If conversion fails, return False

# Function to calculate Mean Absolute Error (MAE) for 'n' samples
def MAE_f(n):
    sum = 0
    for i in range(0, n):
        pred = random.uniform(0, 10)  # Generate a random prediction between 0 and 10
        target = random.uniform(0, 10)  # Generate a random target value between 0 and 10
        loss = abs(pred - target)  # Calculate the absolute error
        print(f"Loss name: MAE, sample: {i}, pred: {pred}, target: {target}, loss: {loss}")
        sum += loss  # Accumulate the loss
    print(f"final MAE: {sum / n}")  # Calculate and print the average loss (MAE)

# Function to calculate Mean Squared Error (MSE) for 'n' samples
def MSE_f(n):
    sum = 0
    for i in range(0, n):
        pred = random.uniform(0, 10)  # Generate a random prediction between 0 and 10
        target = random.uniform(0, 10)  # Generate a random target value between 0 and 10
        loss = pow(pred - target, 2)  # Calculate the squared error
        print(f"Loss name: MSE, sample: {i}, pred: {pred}, target: {target}, loss: {loss}")
        sum += loss  # Accumulate the loss
    print(f"final MSE : {sum / n}")  # Calculate and print the average loss (MSE)

# Function to calculate Root Mean Squared Error (RMSE) for 'n' samples
def RMSE_f(n):
    sum = 0
    for i in range(0, n):
        pred = random.uniform(0, 10)  # Generate a random prediction between 0 and 10
        target = random.uniform(0, 10)  # Generate a random target value between 0 and 10
        loss = pow(pred - target, 2)  # Calculate the squared error
        print(f"Loss name: RMSE, sample: {i}, pred: {pred}, target: {target}, loss: {loss}")
        sum += loss  # Accumulate the loss
    print(f"final RMSE: {math.sqrt(sum / n)}")  # Calculate and print the root mean squared error (RMSE)

# Main code execution
n = input("n = ")  # Prompt the user to input the number of samples
if isnumeric(n):  # Check if the input is a valid number
    n = int(n)  # Convert the input to an integer for mathematical operations
    loss_name = input("Input loss name (MAE / MSE / RMSE) : ")  # Prompt the user to choose a loss function
    if loss_name == "MAE":
        MAE_f(n)  # Call the MAE function if the user selects "MAE"
    elif loss_name == "MSE":
        MSE_f(n)  # Call the MSE function if the user selects "MSE"
    elif loss_name == "RMSE":
        RMSE_f(n)  # Call the RMSE function if the user selects "RMSE"