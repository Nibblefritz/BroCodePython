import random

dice_art = {
    1: (
        "-------\n"
        "|     |\n"
        "|  *  |\n"
        "|     |\n"
        "-------\n"
    ),
    2: (
        "-------\n"
        "|*    |\n"
        "|     |\n"
        "|    *|\n"
        "-------\n"
    ),
    3: (
        "-------\n"
        "|*    |\n"
        "|  *  |\n"
        "|    *|\n"
        "-------\n"
    ),
    4: (
        "-------\n"
        "|*   *|\n"
        "|     |\n"
        "|*   *|\n"
        "-------\n"
    ),
    5: (
        "-------\n"
        "|*   *|\n"
        "|  *  |\n"
        "|*   *|\n"
        "-------\n"
    ),
    6: (
        "-------\n"
        "|*   *|\n"
        "|*   *|\n"
        "|*   *|\n"
        "-------\n"
    )   
}

while True:
    roll = input("Press Enter to roll the dice (q to quit): ").lower()
    
    if roll == 'q':
        print("Thanks for playing!")
        break
    
    dice_value_1 = random.randint(1, 6)
    dice_value_2 = random.randint(1, 6)
    
    print(f"You rolled a {dice_value_1 + dice_value_2}:\n{dice_art[dice_value_1]}{dice_art[dice_value_2]}")
    print()  # Print a newline for better readability