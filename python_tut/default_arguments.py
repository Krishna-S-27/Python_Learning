# default argumments = a default value of a ceratin parameters.
# default is used when that argument is omitted amke your function more flexible , reduces 
# of arguments 1. positional  2. DEFAULT 3. keyword 4. arbitrary

# Example 
def net_price(list_price,discount=0,tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)
    
print(net_price(650))
print(net_price(650,0.1))

# count down timer 
import time

def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(5)# will only pass the end argument where start is a default argument.
