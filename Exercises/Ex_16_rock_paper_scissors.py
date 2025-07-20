# Rock Paper Scissors
import random
options = ("rock", "paper", "scissors")
is_running = True
choice = ""
computer = ""
user_score = 0
computer_score = 0

while is_running:
    choice = input("Choose rock, paper, or scissors (q to quit): ").lower()
    computer = random.choice(options)
    print(choice)
    
    if choice == "q":
        is_running = False
    elif choice == "rock" and computer == "rock" or choice == "paper" and computer == "paper" or choice == "scissors" and computer == "scissors":
            print(f"You both chose {choice}. Try again.")
    elif choice == "rock" and computer == "scissors" or choice == "scissors" and computer == "paper" or choice == "paper" and computer == "rock": 
        print(f"You chose {choice} - Computer chose {computer}. You win!")
        user_score += 1
    elif choice == "rock" and computer == "paper" or choice == "scissors" and computer == "rock" or choice == "paper" and computer == "scissors": 
        print(f"You chose {choice} - Computer chose {computer}. You lose...")
        computer_score += 1
    else:
        print("Invalid Choice.")
        continue

    print(f"Player: {user_score} - Computer: {computer_score}")
    
print()
print(f"----- FINAL SCORE -----")
print(f"Player: {user_score}")
print(f"Computer: {computer_score}")

if user_score > computer_score:
    print("YOU WIN!")
elif user_score < computer_score:
    print("YOU LOSE!")
else:
    print("IT'S A DRAW")