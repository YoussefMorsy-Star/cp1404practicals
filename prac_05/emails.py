"""
Emails
"""

def main():
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").lower()
        if confirm not in ["", "y"]:
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract name from email."""
    name_part = email.split('@')[0]
    parts = name_part.replace('.', ' ').replace('_', ' ').split()
    name = ' '.join(part.capitalize() for part in parts)
    return name


if __name__ == '__main__':
    main()
