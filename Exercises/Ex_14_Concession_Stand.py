# Concession Stand Program

# dictionary {key: value}

menu = {"pizza": 4.99,
        "hot dog": 2.99,
        "hamburger": 4.99,
        "fries": 1.99,
        "chips": 0.99,
        "soda": 0.99, 
        "popcorn": 1.99,
        "nachos": 2.99,
        "pretzel": 2.49,
        "lemonade": 1.49
        }

cart = []
total = 0.00

print("####### MENU #######")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("####################")
print()

while True:
    food = input("Select an item to purchase (q to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None: # This basically says if the food item in menu doesn't return "none"
        cart.append(food)

print()
print("----- Your Order -----")
for food in cart:
    total += menu.get(food)
    print(food, end=", ")
    
print()
print(f"Total: ${total}")
print(f"Sales Tax: ${total * 0.065:.2f}")
print(f"Final Total: ${total * 1.065:.2f}")