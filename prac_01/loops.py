print("Odd numbers from 1 to 20:")
for number in range(1, 21, 2):
    print(number, end=' ')
print("\n")

print("Counting by 10s up to 100:")
for number in range(0, 101, 10):
    print(number, end=' ')
print("\n")

print("Counting backwards from 20:")
for number in range(20, 0, -1):
    print(number, end=' ')
print("\n")

stars = int(input("How many stars? "))
print("Here's your star line:")
for _ in range(stars):
    print("*", end='')
print()

print("Now let's build a star triangle!")
for i in range(1, stars + 1):
    print("*" * i)
