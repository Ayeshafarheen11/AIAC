def factorial(n):
    """
    Calculates the factorial of a number.
    Returns 'Not defined' for negative inputs.
    Handles 0! correctly (returns 1).
    """
    if n < 0:
        return "Not defined"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
print(factorial(0))
print(factorial(5))
print(factorial(-1))