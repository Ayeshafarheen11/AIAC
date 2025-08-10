def is_palindrome(s: str) -> bool:
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Example usage:
if __name__ == "__main__":
    test_str = "A man, a plan, a canal: Panama"
    print(is_palindrome(test_str))  # Output: True