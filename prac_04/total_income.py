def main():
    """Get incomes and display an income report."""
    number_of_months = int(input("How many months? "))
    incomes = get_incomes(number_of_months)
    display_income_report(incomes)

def get_incomes(number_of_months):
    """Prompt user to enter incomes for each month and return as a list."""
    incomes = []
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    return incomes

def display_income_report(incomes):
    """Display income report showing each month's income and cumulative total."""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, start=1):  # using enumerate here
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f}    Total: ${total:10.2f}")

main()
