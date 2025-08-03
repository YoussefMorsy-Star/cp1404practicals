"""
CP1404 Practical
State names program using a dictionary
"""

STATE_ABBREVIATIONS_TO_NAMES = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "WA": "Western Australia",
    "SA": "South Australia",
    "NT": "Northern Territory",
    "ACT": "Australian Capital Territory"
}


def main():
    print("Welcome to the Australian State Lookup!")
    user_input = input("Enter short state (e.g. QLD): ").upper()
    try:
        print(f"{user_input} is {STATE_ABBREVIATIONS_TO_NAMES[user_input]}")
    except KeyError:
        print("Invalid short state")

    print("\nAll states:")
    for abbreviation, name in STATE_ABBREVIATIONS_TO_NAMES.items():
        print(f"{abbreviation:>3} is {name}")


if __name__ == "__main__":
    main()
