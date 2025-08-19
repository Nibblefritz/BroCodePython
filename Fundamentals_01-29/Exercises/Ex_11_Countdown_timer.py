# Timer countdown program
import time

#time.sleep(1) This line is used to pause the program for 1 second

timer = int(input("Enter the countdown time in seconds: "))

for x in range(timer, -1, -1):
    seconds = x % 60  # Calculate seconds
    minutes = int(x / 60) % 60  # Calculate minutes
    hours = int(x / 3600)  # Calculate hours
    print(f"Time left: {hours:02}:{minutes:02}:{seconds:02}", end='\r')  # Print the time left on the same line (end ='\r' means carriage return)
    time.sleep(1)  # Wait for 1 second
print("Time's up!")  # Notify when the countdown is complete

## Note Specifically, \r is a carriage return character. When used as the end parameter, it moves the cursor to the beginning of the current line, effectively overwriting the previous output on that line.