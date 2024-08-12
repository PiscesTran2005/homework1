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


def mae_f(n):
    loss_sum = 0
    for i in range(0, n):
        # Generate a random prediction between 0 and 10
        pred = random.uniform(0, 10)
        # Generate a random target value between 0 and 10
        target = random.uniform(0, 10)
        loss = abs(pred - target)  # Calculate the absolute error
        print(f"Loss name: MAE, sample: {i}, pred: {
              pred}, target: {target}, loss: {loss}")
        loss_sum += loss  # Accumulate the loss
    # Calculate and print the average loss (MAE)
    print(f"final MAE: {loss_sum / n}")

# Function to calculate Mean Squared Error (MSE) for 'n' samples


def mse_f(n):
    loss_sum = 0
    for i in range(0, n):
        # Generate a random prediction between 0 and 10
        pred = random.uniform(0, 10)
        # Generate a random target value between 0 and 10
        target = random.uniform(0, 10)
        loss = pow(pred - target, 2)  # Calculate the squared error
        print(f"Loss name: MSE, sample: {i}, pred: {
              pred}, target: {target}, loss: {loss}")
        loss_sum += loss  # Accumulate the loss
    # Calculate and print the average loss (MSE)
    print(f"final MSE : {loss_sum / n}")

# Function to calculate Root Mean Squared Error (RMSE) for 'n' samples


def rmse_f(n):
    loss_sum = 0
    for i in range(0, n):
        # Generate a random prediction between 0 and 10
        pred = random.uniform(0, 10)
        # Generate a random target value between 0 and 10
        target = random.uniform(0, 10)
        loss = pow(pred - target, 2)  # Calculate the squared error
        print(f"Loss name: RMSE, sample: {i}, pred: {
              pred}, target: {target}, loss: {loss}")
        loss_sum += loss  # Accumulate the loss
    # Calculate and print the root mean squared error (RMSE)
    print(f"final RMSE: {math.sqrt(loss_sum / n)}")


# Main code execution
n = input("n = ")  # Prompt the user to input the number of samples
if isnumeric(n):  # Check if the input is a valid number
    n = int(n)  # Convert the input to an integer for mathematical operations
    # Prompt the user to choose a loss function
    loss_name = input("Input loss name (MAE / MSE / RMSE) : ")
    if loss_name == "MAE":
        mae_f(n)  # Call the MAE function if the user selects "MAE"
    elif loss_name == "MSE":
        mse_f(n)  # Call the MSE function if the user selects "MSE"
    elif loss_name == "RMSE":
        rmse_f(n)  # Call the RMSE function if the user selects "RMSE"
