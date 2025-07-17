total = 0
item_count = int(input("How many items are you buying? "))

while item_count < 0:
    print("That can't be right... Try again.")
    item_count = int(input("How many items are you buying? "))

for i in range(item_count):
    price = float(input(f"Price of item #{i + 1}: $"))
    total += price

if total > 100:
    total *= 0.9

print(f"\nTotal price for {item_count} items is ${total:.2f}")
