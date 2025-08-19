# Compound Interest Calculator Exercise

# What the balance will be after accruing interest for a certain number of years.

principal = 0
rate = 0 
time =0

# while principal <= 0:
#     principal = float(input("Enter the principal amount (greater than 0): "))
#     if principal <= 0:
#         print("Principal must be greater than 0. Please try again.")
        
# while rate <= 0:
#     rate = float(input("Enter the interest rate (greater than 0): "))
#     if rate <= 0:
#         print("Interest rate must be greater than 0. Please try again.")
        
# while time <= 0:
#     time = float(input("Enter the time in years (greater than 0): "))
#     if time <= 0:
#         print("Time in years must be greater than 0. Please try again.")

while True:
    principal = float(input("Enter the principal amount (greater than 0): "))
    if principal < 0:
        print("Principal must be greater than 0. Please try again.")
    else:
        break
        
while True:
    rate = float(input("Enter the interest rate (greater than 0): "))
    if rate < 0:
        print("Interest rate must be greater than 0. Please try again.")
    else:
        break
     
while True:   
    time = float(input("Enter the time in years (greater than 0): "))
    if time < 0:
        print("Time in years must be greater than 0. Please try again.")
    else:
        break

total = principal * pow((1 + rate / 100), time) # Calculating compound interest
print(f"The balance after {time} years will be: ${total:,.2f}")
