# Banking Program
#1. Show Balance 2.Deposit 3.Withdraw

# Initialize balance as a global variable
account_balance = 0

def show_balance():
    print(f"Your balance is: ${account_balance}")
    
def deposit():
    dep = int(input("Enter the amount you want to deposit: $"))
    
    if dep < 0:
        print("That is invalid!\nPlease check once!!")
        return 0
    else:
        return dep
    
def withdraw():
    amt = int(input("Enter the amount you want to `Withdraw`: $ "))
    if amt > account_balance:
        print("Insufficient funds")
        return 0
    elif amt < 0:
        print("The amount must be more than zero")
        return 0
    else:
        return amt

while True:
    print("\nEnter the operation you want complete")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Your choice is: "))

    if choice == 1:
        show_balance()
    elif choice == 2:
        account_balance += deposit()
        print(f"Deposit successful! New balance: ${account_balance}")
    elif choice == 3:
        withdrawn_amount = withdraw()
        if withdrawn_amount > 0:
            account_balance -= withdrawn_amount
            print(f"Withdrawal successful! New balance: ${account_balance}")
    elif choice == 4:
        print("Thank you for using banking system!!")
        break
    else:
        print("You have entered the wrong choice!")
        print("Please enter the correct choice!!")
