def main():
    """Get and validate a password, then print asterisks equal to its length."""
    MIN_LENGTH = 6
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(min_length):
    """Prompt user for password until it's valid (meets minimum length)."""
    password = input("Enter a password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters.")
        password = input("Enter a password: ")
    return password


def print_asterisks(password):
    """Print asterisks equal to the length of the password."""
    print("*" * len(password))


main()
