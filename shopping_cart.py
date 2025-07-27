# Shopping cart program example

chats = []
prices = []
total = 0

while True:
    chat = input("Enter the chat you want to buy(q to quit): ")
    if chat.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price for {chat}: $"))
        chats.append(chat)
        prices.append(price)
print("----------------Your CheckBook--------------------")
print("The food your buying are:")
for chat in chats:
    print(chat, end = " ")
print()
for price in prices:
    total = total + price

print(f"Your Total Price is:{total}")