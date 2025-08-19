import random # Importing a module

#print(help(random))

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Random integery from a range of low number to high number
number = random.randint(low, high)
print(number)

# Random floating number between 0 and 1
number = random.random()
print(number)

# Random "choice" from a tuple
option = random.choice(options)
print(option)

# Shuffle sequence of cards
random.shuffle(cards)
print(cards)