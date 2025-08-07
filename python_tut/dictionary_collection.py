# Dictionary is the collection of {key : value} pairs ordered and changeable
# this will do not have the duplicates
# To print the dictionary we would use get function iterate and print it
# You can update the value in the dic by using update function. like captials.update({"USA":"Denmark"})
# To remove you can use the function pop like captials.pop("Japan")
# To remove the latestItem pushed in dic you can use captials.popitem()
# To get only key you can use captials.key() function and for values you can do .values()
captials = {
    "India":"New Delhi",
    "USA": "Washington D.C",
    "China": "Beijing",
    "Japan": "Tokyo"
}

captials.update({"USA":"Denmark"})
print(captials.get("USA"))
captials.pop("Japan")
print(captials.get("Japan"))
print(captials)
#print(help(captials))

for i in captials.keys():
    print(i)
print()

for i in captials.values():
    print(i)

item = captials.items()

for i,j in item:
    print(f"{i}:{j}")