# format specifiers = {:flags} format a value based on what flags are inserted
# .(number)f        = round to the nearest .<n>f number of decimal places
# :(number)         = allocate that many spaces
# :03               = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center justify
# :+ = use a plus sign to indicate positive value
# := = place sign to the left most position
# :  = insert a space before positive values
# :, = use a comma separator

price1 = 3000.14159
price2 = -97987.65
price3 = 123456789.34

print(f"Price 1: ${price1:10}")  # Give each value 10 spaces to display output
print(f"Price 2: ${price2:10}")  # Give each value 10 spaces to display output
print(f"Price 3: ${price3:10}")  # Give each value 10 spaces to display output
print("")
print(f"Price 1: ${price1:.3f}")  # Round to 2 decimal places
print(f"Price 2: ${price2:.1f}")  # Round to 2 decimal places
print(f"Price 3: ${price3:.2f}")  # Round to 2 decimal places
print("")
print(f"Price 1: ${price1:010}")  # Give each value 10 spaces and zero pad to display output
print(f"Price 2: ${price2:010}")  # Give each value 10 spaces and zero pad to display output
print(f"Price 3: ${price3:010}")  # Give each value 10 spaces and zero pad to display output
print("")
print(f"Price 1: ${price1:<10}")  # left justify with 10 spaces
print(f"Price 2: ${price2:<10}")  # left justify with 10 spaces
print(f"Price 3: ${price3:<10}")  # left justify with 10 spaces
print("")
print(f"Price 1: ${price1:>10}")  # right justify with 10 spaces
print(f"Price 2: ${price2:>10}")  # right justify with 10 spaces
print(f"Price 3: ${price3:>10}")  # right justify with 10 spaces
print("")
print(f"Price 1: ${price1:^10}")  # center with 10 spaces
print(f"Price 2: ${price2:^10}")  # center with 10 spaces
print(f"Price 3: ${price3:^10}")  # center with 10 spaces
print("")
print(f"Price 1: ${price1:+}")  # Display a plus sign for positive values
print(f"Price 2: ${price2:+}")  # Display a plus sign for positive values
print(f"Price 3: ${price3:+}")  # Display a plus sign for positive values
print("")
print(f"Price 1: ${price1: }")  # Display a space sign for positive values
print(f"Price 2: ${price2: }")  # Display a space sign for positive values
print(f"Price 3: ${price3: }")  # Display a space sign for positive values
print("")
print(f"Price 1: ${price1:,}")  # Display a comma thousands separator
print(f"Price 2: ${price2:,}")  # Display a comma thousands separator
print(f"Price 3: ${price3:,}")  # Display a comma thousands separator
print("")

# Mix and match format specifiers
print(f"Price 1: ${price1:>30,.2f}")  # Display a right justification with 30 spaces and comma thousands separator and round to 2 decimal places
print(f"Price 2: ${price2:>30,.2f}")  # Display a right justification with 30 spaces and comma thousands separator and round to 2 decimal places
print(f"Price 3: ${price3:>30,.2f}")  # Display a right justification with 30 spaces and comma thousands separator and round to 2 decimal places
print("")