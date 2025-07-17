import random

def main():
    """Get user's score and display the result, then generate a random score and do the same."""
    score = float(input("Enter score: "))
    result = get_score_result(score)
    print(f"Your score is: {result}")

    random_score = random.uniform(0, 100)
    print(f"\nRandom score: {random_score:.2f}")
    print(f"Result: {get_score_result(random_score)}")

def get_score_result(score):
    """Return a result string based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
