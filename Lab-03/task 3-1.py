def calculate_electricity_bill(units_consumed, rate_per_unit):
    """
    Calculate the electricity bill based on units consumed and rate per unit.

    Parameters:
    units_consumed (float): Number of electricity units consumed.
    rate_per_unit (float): Cost per unit.

    Returns:
    float: Total electricity bill.
    """
    return units_consumed * rate_per_unit

# Example usage:
units = float(input("Enter the number of units consumed: "))
rate = float(input("Enter the rate per unit: "))
bill = calculate_electricity_bill(units, rate)
print(f"Total electricity bill: {bill:.2f}")
