# Hangman in Python
import random
from wordslist import words

# dictionary of key:()
hangman_art = {0: ("   ",
                   "   ",
                   "   "), 
               1: (" o ",
                   "   ",
                   "   "), 
               2: (" o ",
                   " | ",
                   "   "), 
               3: (" o ",
                   "/| ",
                   "   "), 
               4: (" o ",
                   "/|\\",
                   "   "), 
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_guesses):
    print("*************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*************")

def display_hint(hint):
    print("Hint: ", " ".join(hint))

def display_answer(answer):
    print("Answer: ", " ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        print()
        guess = input("Guess a letter: ").lower()
    
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print(f"Wrong guess! You have {6 - wrong_guesses} attempts left.")

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN! You've guessed the word!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            print("YOU LOSE!")
            print(f"The word was: {answer}")
            is_running = False
            
if __name__ == "__main__":
    main()