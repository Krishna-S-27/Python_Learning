# for loops  = executes a block of code a fixed number of times. you can iterate over range , String, Sequence etc


#for i in range(1,11):
#   print(i)

#for i in reversed(range(1,11)):  # if you want to count 2's  (1, 11, 2)
#    print(i)
#print("Happy New Year")

#credit_card = "1324-5678-9101"
#for i in credit_card:
#    print(i)

# Create a count-down timer
import time
timer  = int(input("Enter the time in seconds:"))
for i in reversed(range(0,timer)):  # for normal range(0,timer)  or range(timer,0,-1)
    seconds = i % 60
    minutes = int(i/60) % 60
    hours = int(i/3600)  # if you have days in the print statement the for hours you can add % 24 in hours
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time is UP!!!")