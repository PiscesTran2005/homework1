import math  # Importing the math module for mathematical operations

# Function to check if a value can be converted to an int (i.e., is a number)


def check(x):
    try:
        int(x)  # Try converting the value to an int
        return True  # If successful, return True
    except ValueError:
        return False  # If conversion fails, return False


# Get user input
tp = input("tp = ")
fp = input("fp = ")
fn = input("fn = ")

# Initialize an empty list to collect error messages
errors = []

# Check if tp, fp, and fn are integers
if not check(tp):
    errors.append("tp")  # Add 'tp' to errors list if it's not an int
if not check(fp):
    errors.append("fp")  # Add 'fp' to errors list if it's not an int
if not check(fn):
    errors.append("fn")  # Add 'fn' to errors list if it's not an int

# If there are any errors, print the corresponding message
if errors:
    print(f"{' and '.join(errors)} must be int")
else:
    # Convert input strings to integers
    tp = int(tp)
    fp = int(fp)
    fn = int(fn)

    # Check if tp, fp, and fn are greater than zero
    if tp > 0 and fp > 0 and fn > 0:
        # Calculate precision, recall, and f1-score
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        f1_score = 2 * (precision * recall) / (precision + recall)

        # Print the calculated values
        print(f"precision is {precision}")
        print(f"recall is {recall}")
        print(f"f1-score is {f1_score}")
    else:
        print("tp and fp and fn must be greater than zero")
