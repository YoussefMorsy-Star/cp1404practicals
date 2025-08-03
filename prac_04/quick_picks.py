import random

NUMBERS_PER_LINE = 6
MIN = 1
MAX = 45

def main():
    quick_picks = int(input("How many quick picks? "))
    for _ in range(quick_picks):
        pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in pick))

def generate_quick_pick():
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        number = random.randint(MIN, MAX)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers

main()
