try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
except ValueError:
    # A ValueError happens when the user enters something that's not an integer
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    # A ZeroDivisionError happens when the denominator is 0
    print("Cannot divide by zero!")
else:
    print(f"The result is: {result}")
print("Finished.")

# Questions:

# When will a ValueError occur?
# If the user types something that's not a number, like letters or symbols.

# When will a ZeroDivisionError occur?
# If the user enters 0 as the denominator.

# Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes, by checking if the denominator is zero before attempting the division.
