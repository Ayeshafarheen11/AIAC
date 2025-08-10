def fibonacci_sequence(n):
    """
    Returns the Fibonacci sequence up to n terms using a loop.
    """
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# User input
n = int(input("Enter the number of terms: "))
print("Fibonacci sequence:", fibonacci_sequence(n))

