# Keep asking until a valid integer is entered
finished = False
result = 0
while not finished:
    try:
        number = int(input("Please enter an integer: "))
        result = number ** 2
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print(f"Valid result is: {result}")
