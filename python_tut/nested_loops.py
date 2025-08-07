#nested loops = A loop within a loop
#               outer loop:
#                   inner loop:

for i in range(3):
    for j in range(1,10):
        print(j, end="")
    print()

rows = int(input("Enter the rows required: "))
columns = int(input("Enter the columns required: "))
symbols = input("Enter the symbol you want to print")

for i in range(rows):
    for j in range(columns):
        print(symbols, end=" ")
    print()
