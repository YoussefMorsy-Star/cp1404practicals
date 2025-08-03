"""
CP1404/CP5632 - Practical 03
Files - Reading and Writing
"""

# 1. Ask the user for their name and write it to name.txt
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2. Read the name from name.txt and greet the user
in_file = open("name.txt", "r")
name = in_file.read().strip()
print(f"Hi {name}!")
in_file.close()

# 3. Read the first two numbers from numbers.txt and print their sum
with open("numbers.txt", "r") as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
    print(f"The sum of the first two numbers is: {first_number + second_number}")

# 4. Read all numbers from numbers.txt and print their total
with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        total += int(line)
    print(f"The total of all numbers is: {total}")
