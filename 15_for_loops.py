# For loops loop through a sequence a set amount of times, such as a list, tuple, or string.

for x in range(0,30,2):
    print(x, end=' ')
print()

for x in reversed(range(1,11)):
    print(x, end=' ')
print("Happy New Year!')")

credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x, end=' ')
print()

for x in range(1, 21):
    if x == 13:
        continue # skip this iteration and continue with the next one
    elif x == 20:
        break # exit the loop
    else:
        print(x, end=' ')
print()