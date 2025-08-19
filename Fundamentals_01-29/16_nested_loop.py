# A nested loop is a loop inside another loop.
# The inner loop will be executed for each iteration of the outer loop.
# This is useful for iterating over multi-dimensional data structures like lists of lists.
# For example, if you have a list of lists, you can use a nested loop to iterate over each element in the inner lists.

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end='')
    print()