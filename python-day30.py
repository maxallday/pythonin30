#🐍 Day 30: Capstone Project: Track Your Pennies 🐍
import json
'''
What Your Expense Tracker Should Do:
Track Expenses: Add and categorize expenses.
Store Data: Save and read data from a file.
Summary: Display a summary of expenses.
'''
#code 
# Sample expense dictionary
'''budget = {
    'Food': 1500,
    'Transport': 2200,
    'Utilities': 600,
    'Entertainment': 250,
    'Clothes':250,
}

def add_expense(category, amount):
    if category in budget:
        budget[category] += amount
    else:
        budget[category] = amount

# Now you can add an expense like so
print("Enter food, Utilities & enterntaiment expense")
#budget = input()
f, t, u, e, c = input("Enter 3 inputs: ").split()

print(f"\nFood input: {f}")
print(f"Transport:  {t}")
print(f"Utilities input: {u}")
print(f"Entertainment input: {e}")
print(f"Clothes: {c}")
'''


#Expense manager app




# Function to load budget from file or create default if file doesn't exist
def load_budget():
    try:
        with open('budget.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            'Food': 1500,
            'Transport': 2200,
            'Utilities': 600,
            'Entertainment': 250,
            'Clothes': 250,
        }

# Function to save budget to file
def save_budget(budget):
    with open('budget.txt', 'w') as file:
        json.dump(budget, file)
    print("Budget saved successfully.")

# Function to add an expense, checking if it's within budget
def add_expense(budget, expenses, category, amount):
    if category in budget:
        if expenses[category] + amount <= budget[category]:
            expenses[category] += amount
            return True
        else:
            print(f"Error: Adding {amount} to {category} would exceed the budget.")
            return False
    else:
        print(f"Error: {category} is not a valid budget category.")
        return False

# Function to display current budget status
def display_budget_status(budget, expenses):
    print("\nCurrent Budget Status:")
    for category in budget:
        spent = expenses[category]
        remaining = budget[category] - spent
        print(f"{category}: Budget {budget[category]}, Spent {spent}, Remaining {remaining}")

# Main function to run the expense manager
def main():
    # Load budget and initialize expenses
    budget = load_budget()
    expenses = {category: 0 for category in budget}

    # Main loop for expense entry
    while True:
        print("\nEnter expenses (or 'q' to quit):")
        user_input = input("Category Amount: ").split()
        
        # Check for quit command
        if user_input[0].lower() == 'q':
            break
        
        # Validate input
        if len(user_input) != 2:
            print("Invalid input. Please enter a category and an amount.")
            continue
        
        # Process expense
        category, amount = user_input[0], float(user_input[1])
        if add_expense(budget, expenses, category, amount):
            print(f"Added {amount} to {category}")
        
        # Display updated budget status
        display_budget_status(budget, expenses)
    
    # Save budget and exit
    save_budget(budget)
    print("Thank you for using the expense manager!")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
