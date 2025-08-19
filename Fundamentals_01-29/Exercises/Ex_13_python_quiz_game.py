# Python Quiz Game
# Need a tuple of questions
# Need a 2D tuple of options
# Need a tuple of answers (answers are set in stone)
# Need a list of guesses (we will be appending guesses to this list)
# Need a score variable
# Need a question number variable to track which question the user is on

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in the Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 113 elements", "B. 120 elements", "C. 118 elements", "D. 119 elements"),
           ("A. Ostrich", "B. Eagle", "C. Penguin", "D. Albatross"),
           ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"),
           ("A. 221 bones", "B. 201 bones", "C. 210 bones", "D. 206 bones"),
           ("A. Venus", "B. Mars", "C. Mercury", "D. Jupiter"))

answers = ("C", "A", "B", "C", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess = input("Enter your answer (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("Correct!")
        print()
        score += 1
    else:
        print(f"Incorrect! The correct answer was {answers[question_num]}.")
        print()
    
    question_num += 1
    
print("#################")
print("#### RESULTS ####")
print("#################")
print()
print(f"Your final score is {score}/{len(questions)}.")

