# iterables = An object/collection that can return its elements one at a time allowing
#               it to be iterated over in a loop
import time
numbers = [1, 2, 3, 4, 5]

#for numeber in reversed(numbers):
#    print(numeber)
#    time.sleep(1)


# so here numeber is the iterable.
# set are not reversed 
# for dictionaries
my_dictionary = {
    "a": 1,
    "b":2,
    "c":3
}
# this only print  my keys.  for values use my_dictionary.values()
# But if you want both use item with both itrables for keys and values
# like for key, value in my_dictionary.items()

#for itr in my_dictionary:
#    print(itr)




# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set or dictionary)
#                        1. in
#                        2. not in

word = "APPLE"
if "A" in word:
    print("a is present")
else:
    print("a is not present")