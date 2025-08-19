# Exercise 2 Shopping Cart Program

item = input("What item do you want to buy? ")
price = float(input("What is the price of the item? "))
quantity = int(input("How many do you want? "))
total = price * quantity

print(f"You have added {quantity} {item}(s) to your cart at ${price:.2f} each.")
print(f"The total cost is ${total:.2f}.")