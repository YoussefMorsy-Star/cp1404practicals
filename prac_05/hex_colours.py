"""
CP1404 Practical
Hex colour lookup program
"""

COLOUR_NAME_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "black": "#000000",
    "blue": "#0000ff",
    "blueviolet": "#8a2be2",
    "brown": "#a52a2a"
}


def main():
    print("Colour name to hex code lookup (type blank to quit):")
    while True:
        colour_name = input("Enter colour name: ").lower()
        if not colour_name:
            break
        try:
            print(f"The hex code for {colour_name} is {COLOUR_NAME_TO_HEX[colour_name]}")
        except KeyError:
            print("Invalid colour name")


if __name__ == "__main__":
    main()
