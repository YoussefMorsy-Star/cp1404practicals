def main():
    """Run the menu-based score program."""
    score = get_valid_score()
    choice = ""
    while choice != "Q":
        print_menu()
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(get_score_result(score))
        elif choice == "S":
            print("*" * int(score))
        elif choice != "Q":
            print("Invalid choice")
    print("Goodbye!")


def print_menu():
    """Display the menu."""
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    """Prompt the user for a valid score (0–100 inclusive)."""
    score = float(input("Enter score (0–100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score (0–100): "))
    return score


def get_score_result(score):
    """Return a result string based on the score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
