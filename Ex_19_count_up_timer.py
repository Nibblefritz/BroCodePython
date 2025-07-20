import time

def count(end, start=0): # Non default arugments should precede default arguments so we reverse the order here
    if start > end:
        print("Start time must be less than or equal to end time.")
        return
    
    for i in range(start, end + 1): #Add 1 to include the end number, becuase it's exlcusive in range
        print(i)
        time.sleep(1)  # Wait for 1 second before printing the next number
    print("Done!")
    
count(10)  # Call the function to count from 1 to 10