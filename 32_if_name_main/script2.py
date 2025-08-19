from script1 import *

# By just running this with the if main and main function removed from script 1 you'll see it will run script 1
def favorite_drink(drink):
    print(f"Your favorite drink is {drink}.")

def main():
    print("this is script 2")
    favorite_food("Sushi")
    favorite_drink("Milk")
    print("Goodbye")

if __name__ == '__main__':
    main()