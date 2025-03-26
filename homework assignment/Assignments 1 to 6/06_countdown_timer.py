#Project 6: Countdown Timer Python Project
import time
56
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r', flush=True)
        time.sleep(1)
        t -= 1
    
    print("Time's up!")

# Get user input for seconds
seconds = input("Enter time in seconds: ")

# Convert to integer
countdown(int(seconds))

