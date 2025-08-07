# 2D list is the collection of two list or list can be more.

#elxample

fruit = ["apple","pineapple", "orange","mango"]
vegetable = ["cereal","potato","cucumber","carrots","ladyfinger","spinach"]
meats = ["chicken","fish","turkey","lamb"]

groceries = [fruit,vegetable, meats]
print(groceries)# prints all list
print(groceries[0])# prints 0th index value like fruits
print(groceries[0][2])#prints an item in fruits works like co-ordinates

for i in groceries:
    for j in i:
        print(j, end=" ")
    print()