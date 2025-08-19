import random

low = 1
high = 100
guess_count = 0
number = random.randint(low, high)
is_running = True

while is_running:
    guess = input(f"Guess a number between {low} and {high}: ")
    
    if guess.isdigit():
        guess = int(guess)
        guess_count += 1
        
        if guess < low or guess > high:
            print(f"Your guess must be within {low} and {high}")
        elif guess < number:
            print("Your guess is lower than the number")
        elif guess > number:
            print("Your guess is higher than the number.")
        else:
            print()
            print(f"Congratulations your guess of {guess} is correct: {number}")
            print(f"Guess attempts: {guess_count}")
            is_running = False
    else:
        print("Invalid guess. Must be a digit")