# Dictionary to store transactions
transactions = {
    "income": [],
    "expenses": []
}


from datetime import datetime

# Function to add an income
def add_income():
    amount = float(input("Enter income amount: "))
    category = input("Enter income category (e.g., Salary, Bonus): ")
    description = input("Enter income description: ")
    date = datetime.today().strftime('%Y-%m-%d')  # Get today's date
    transactions["income"].append((amount, category, description, date))
    print(f"✅ Income of {amount} added successfully!\n")

# Function to add an expense
def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category (e.g., Rent, Food, Transport): ")
    description = input("Enter expense description: ")
    date = datetime.today().strftime('%Y-%m-%d')
    transactions["expenses"].append((amount, category, description, date))
    print(f"❌ Expense of {amount} recorded successfully!\n")


# Function to display financial summary
def view_summary():
    total_income = sum([entry[0] for entry in transactions["income"]])
    total_expense = sum([entry[0] for entry in transactions["expenses"]])
    balance = total_income - total_expense
    
    print("\n💰 Financial Summary 💰")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Current Balance: ${balance:.2f}\n")


import csv

# Function to save transactions to a CSV file
def save_to_csv():
    with open("finance_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Amount", "Category", "Description", "Date"])
        
        for entry in transactions["income"]:
            writer.writerow(["Income", *entry])
        
        for entry in transactions["expenses"]:
            writer.writerow(["Expense", *entry])

    print("📂 Data saved to finance_data.csv successfully!\n")


def load_from_csv():
    try:
        with open("finance_data.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                entry_type, amount, category, description, date = row
                amount = float(amount)
                if entry_type == "Income":
                    transactions["income"].append((amount, category, description, date))
                else:
                    transactions["expenses"].append((amount, category, description, date))
        print("📂 Previous data loaded successfully!\n")
    except FileNotFoundError:
        print("⚠ No previous data found. Starting fresh.\n")



def main():
    while True:
        print("\n📊 Personal Finance Tracker")
        print("1️⃣ Add Income")
        print("2️⃣ Add Expense")
        print("3️⃣ View Summary")
        print("4️⃣ Save & Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            save_to_csv()
            print("🔒 Exiting program. Data saved!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Run the program
main()
