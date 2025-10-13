# copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

import time
# countdown timer excersise
# my_time = int(input("Enter the time in seconds:"))

# for x in range (0, my_time): # range(start, stop, step)
#     print(my_time - x) # to count down we do my_time - x
#     time.sleep(1)
# print("Time's up")

my_time = int(input("Enter the time in seconds:"))
for x in range (my_time, 0, -1):
    seconds = x % 60
    minutes = x // 60
    if seconds < 10:
        print(f"{minutes}:0{seconds}")
    else:    
        print(f"00:{minutes:02}:{seconds}")   
    time.sleep(1)
print("Time's up")