def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def display_menu():
    """Show menu options."""
    print("\nTEMPERATURE CONVERTER")
    print("C - Celsius to Fahrenheit")
    print("F - Fahrenheit to Celsius")
    print("Q - Quit")

def main():
    """Main program function."""
    display_menu()
    choice = input("Choose an option: ").strip().upper()
    while choice != "Q":
        if choice == "C":
            c = float(input("Enter temp in Celsius: "))
            f = celsius_to_fahrenheit(c)
            print(f"{c}°C = {f:.2f}°F")
        elif choice == "F":
            f = float(input("Enter temp in Fahrenheit: "))
            c = fahrenheit_to_celsius(f)
            print(f"{f}°F = {c:.2f}°C")
        else:
            print("Oops! Invalid choice. Try again.")
        display_menu()
        choice = input("Choose an option: ").strip().upper()
    print("Thanks for using the converter. Stay warm... or cool ")

main()