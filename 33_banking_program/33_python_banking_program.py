# Python Banking Program

def show_balance(balance):
    print("****************************")
    print(f"Your current balance is: ${balance:.2f}")
    print("****************************")
    print()
    
def deposit():
    print("****************************")
    amount = float(input("Enter the amount to deposit: $"))
    print()
    
    if amount < 0:
        print("That's not a valid amount.")
        return 0
    else:
        print(f"You have deposited: ${amount:.2f}")
        return amount

def withdraw(balance):
    print("****************************")
    amount = float(input("Enter the amount to withdraw: $"))
    print()
    if amount > balance:
        print("Insufficient funds.")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0.")
        return 0
    else:
        print(f"You have withdrawn: ${amount:.2f}")
        return amount
def main():   
    balance = 0.0
    is_running = True

    while is_running:
        print("Welcome to the Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using the Banking Program!")

if __name__ == '__main__':
    main()