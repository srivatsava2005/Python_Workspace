import re

def is_palindrome(s):
    """
    Check if a given string is a palindrome.
    Ignores case, spaces, and non-alphanumeric characters.
    """
    # Clean the string: remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Test cases
if __name__ == "__main__":
    test_strings = [
        "A man, a plan, a canal: Panama",  # True
        "race a car",  # False
        "Madam",  # True
        "12321",  # True
        "hello",  # False
        "",  # True (empty string is a palindrome)
        "a",  # True
        "ab",  # False
    ]

    for s in test_strings:
        result = is_palindrome(s)
        print(f"'{s}' is a palindrome: {result}")
