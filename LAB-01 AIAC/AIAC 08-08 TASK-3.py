def reverse_string(s):
    """
    Reverses the input string.

    Args:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    return s[::-1]

# Example usage
input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print("Original:", input_str)
print("Reversed:", reversed_str)