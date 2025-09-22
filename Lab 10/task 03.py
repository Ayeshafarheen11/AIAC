# Define a function to calculate the percentage of a given amount
def calculate_percentage(amount, percent):
    # Multiply the amount by the percent and divide by 100 to get the result
    return amount * percent / 100

# Set the amount and percent values
amount = 200
percent = 15

# Call the function and store the result
result = calculate_percentage(amount, percent)

# Print a descriptive message with the calculated percentage
print(f"{percent}% of {amount} is {result}")