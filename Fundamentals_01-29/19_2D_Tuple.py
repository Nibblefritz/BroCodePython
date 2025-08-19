num_pad = (("1", "2", "3"),
           ("4", "5", "6"),
           ("7", "8", "9"),
           ("*", "0", "#"))  # 2D tuple representing a numeric keypad

print("-------")
for row in num_pad:
    print("|", end='')
    for item in row:
        print(item, end='|')
    print()
    print("-------")  # New line after each row