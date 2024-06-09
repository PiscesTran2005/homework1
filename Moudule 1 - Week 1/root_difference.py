import math  # Importing the math module for mathematical operations
import random  # Importing the random module to generate random numbers

# Prompting the user to input a float value for y
y = float(input("y = "))
# Prompting the user to input a float value for y_hat
y_hat = float(input("y_hat = "))
# Prompting the user to input an integer value for n
n = int(input("n = "))
# Prompting the user to input an integer value for p
p = int(input("p = "))

# Calculating the difference between the n-th root of y and the n-th root of y_hat
diff = y ** (1/n) - y_hat ** (1/n)
# Raising the absolute value of the difference to the power of p to compute the loss
loss = pow(diff, p)

# Printing the calculated loss
print(loss)