def calculate_electricity_bill(units):
    """
    Calculates the total electricity bill based on units consumed.
    Slab rates:
    - For first 100 units: Rs. 5 per unit
    - For next 100 units (101-200): Rs. 7 per unit
    - For units above 200: Rs. 10 per unit
    """
    if units < 0:
        raise ValueError("Units consumed cannot be negative.")
    bill = 0
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)
    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    return bill

if __name__ == "__main__":
    try:
        units = int(input("Enter the number of electricity units consumed: "))
        total_bill = calculate_electricity_bill(units)
        print(f"Total electricity bill: Rs. {total_bill}")
    except ValueError as e:
        print(f"Error: {e}")
