LOW_THRESHOLD = 1000
LOW_RATE = 0.10
HIGH_RATE = 0.15

print(" Welcome to the Bonus Calculator!")
sales = float(input("Enter your sales amount (or negative to exit): $"))

while sales >= 0:
    if sales < LOW_THRESHOLD:
        bonus = sales * LOW_RATE
    else:
        bonus = sales * HIGH_RATE

    print(f" Your bonus is: ${bonus:.2f}")
    sales = float(input("Enter your sales amount (or negative to exit): $"))

print(" Done! Thanks for using the calculator.")
