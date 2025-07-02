#2d List is a list made of lists, useful as a grid or table structure.

"""
fruit =      ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
vegetables = ["Asparagus", "Broccoli", "Carrot", "Onion", "Eggplant"]
meat =       ["Chicken", "Beef", "Pork", "Lamb", "Turkey"]
"""
 
groceries = [["Apple", "Banana", "Cherry", "Date", "Elderberry"], 
             ["Asparagus", "Broccoli", "Carrot", "Onion", "Eggplant"], 
             ["Chicken", "Beef", "Pork", "Lamb", "Turkey"]] #2D list containing 3 lists 

#Could also do list of touples or list of sets, but lists are more common for 2D lists.
"""
groceries = [("Apple", "Banana", "Cherry", "Date", "Elderberry"), 
             ("Asparagus", "Broccoli", "Carrot", "Onion", "Eggplant"), 
             ("Chicken", "Beef", "Pork", "Lamb", "Turkey")] #2D list containing 3 tuples 
"""

print(groceries[0])  # Output: ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
print(groceries[1])  # Output: ['Asparagus', 'Broccoli', 'Carrot', 'Onion', 'Eggplant']
print(groceries[2])  # Output: ['Chicken', 'Beef', 'Pork', 'Lamb', 'Turkey']

print(groceries[0][0])  # Output: Apple (first item in the first list)
print(groceries[1][2])  # Output: Carrot (third item in the second list)
print(groceries[2][4])  # Output: Turkey (fifth item in the third list)

groceries[0][3] = "Blueberry"  # Change 'Date' to 'Blueberry'
print(groceries[0])  # Output: ['Apple', 'Banana', 'Cherry', 'Blueberry', 'Elderberry']

for collection in groceries:
    for item in collection:
        print(item, end=' ')
    print()  # New line after each collection
    
