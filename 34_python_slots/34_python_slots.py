# Python Slot Machine
import random

def spin_row():
    symbols = ["🍒", "🔔", "🍋", "🍉", "⭐️"]

    return [random.choice(symbols) for _ in range(3)] # List comprehension

def print_row(row):
    print("************")
    print(" | ".join(row))
    print("************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:  # All symbols match
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐️":
            return bet * 20
    elif row[0] == row[1] or row[1] == row[2] or row[0] == row[2]:
        return bet * 2
    return 0

def main():
    balance = 100
    
    print("***********************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🔔 🍋 🍉 ⭐️")
    print("***********************")
    
    while balance > 0:
        print(f"Your current balance is: ${balance}")

        bet = input("Enter your bet amount (or 0 to exit): ")
        
        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)
        
        if bet > balance:
            print("You cannot bet more than your current balance.")
            continue
        
        if bet <= 0:
            print("Bet must be greater than 0.")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)
        print()

        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"You win ${payout}!")
            balance += payout

        if balance != 0:
            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() != "y":
                    break

    print()
    print(f"Thank you for playing! Your final balance is ${balance}.")
    print()
    
if __name__ == "__main__":
    main()