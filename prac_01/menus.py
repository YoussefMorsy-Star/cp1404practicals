MENU = "\n(H)ello\n(G)oodbye\n(Q)uit"
name = input("What's your name? ")

print(MENU)
choice = input(">>> ").strip().upper()

while choice != "Q":
    if choice == "H":
        print(f"Hey there, {name}!")
    elif choice == "G":
        print(f"Catch you later, {name}.")
    else:
        print("That wasn't an option. Try again.")

    print(MENU)
    choice = input(">>> ").strip().upper()

print("See ya!")
