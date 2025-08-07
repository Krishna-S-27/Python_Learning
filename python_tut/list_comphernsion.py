# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# Traditional Loops
doubles = []
for x in  range(1,11):
    doubles.append(x*2)

print(doubles)

#list comprehesion
#     [expression for value in iterable if condition]
dou = [x * 2 for x in range(1,11)]
triples = [x*3 for x in range(1,11)]
print(dou)
print(triples)