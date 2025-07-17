score = float(input("Enter your score (0-100): "))

if score < 0 or score > 100:
    print(" That's not a valid score.")
elif score >= 90:
    print(" Excellent!")
elif score >= 50:
    print(" Passable.")
else:
    print(" Bad score.")
