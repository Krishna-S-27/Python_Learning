'''
Collection = single "variable" used to store multiple values
there are 3 types of collections List, Set, Tuple
List = [ ] ordered and changeable. Duplicates OK
Set = { } unordered and immutable, but Add/Remove OK. No duplicates
Tuple = ( ) ordered and unchangeable. Duplicates OK. FASTER
if you know [start: end: step]
'''
# List
fruits = ["apple", "oranges","banana","coconut"] # Duplicates are vaild.
print(fruits)
print(fruits[2])

for i in fruits:
    print(i,end="\n")
#print(help(fruits))
print(len(fruits))
print("apple" in fruits)

# fruits.append("mango") this add item to the end of the list
# print(fruits)

fruits.remove("apple") # removes an element in the list
print(fruits)

fruits.insert(0,"apple") # insert any element at a position
print(fruits)

fruits.sort() # sorts the element in a,b,c order
print(fruits)

fruits.reverse() # reverses the list
print(fruits)
# there are other function like count, clear, copy, extend, index ,pop,
print(fruits.count("apple"))

'''
Set = { "apple","orange","mango" }
for a set we cannot do indexing as set object is not subscriptable
we can use add method
we can use remove method
pop , clear, etc. note we cannot have  duplicates int it.
every element in the Set is a unique element
'''

'''
Tuple = ("apple","orange","mango" )
its the fastest.
ordered 
unchangeable 
In tuple we can have duplicates elements.
we have only 2 method we have access to  .index("apple") and .count("mango")
'''

# Note every thing are iterable and there is one more collection dictionaries that we will be doing seperate.