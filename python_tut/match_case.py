# match-case statement (just like a switch case in java):
# it an alternative to using 'elif' statement
# Execute some code if value matches a "case"
# Benfits = cleaner and syntax is more readable


#example


def day_of_week(day):
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wenseday"
        case 5:
            return "Thrusday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _:
            return "Invalid option is selected"
        
# print(day_of_week(5))


# module = file containing in a code that you want to include in a program
# use "import" to include a module (built-in or your own) like os, pikles, math etc
# useful to break up a large program reusable separate files

import math # here math is a module 

# print(math.sqrt(4))

# print(help("modules"))


# Variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global ->Built-in


# example of variable scope..
def func1(): # function will only see variable or other in its own function but not in others.
    a= 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()

# for scope resolution
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # 'local' is printed
    inner()

outer()

# When Python encounters a variable, it looks for it in a specific order known as LEGB, which stands for Local, Enclosing, Global, and Built-in.
# Local scope refers to variables defined inside a function. These are the first ones Python checks.
# If it doesn't find the variable locally, Python checks the Enclosing scope, which applies to functions nested inside other functions. Variables in the outer function (but not global) are considered enclosing.
# If still not found, Python checks the Global scope. These are variables defined at the top level of the script or module.
# Lastly, if all else fails, Python checks the Built-in scope, which includes predefined functions and exceptions like len(), int(), and NameError.



## if __name__ == __main__: (this script can be imported OR run standalone)
# function and classes in this module can be reused
# without the main block of code executing

def main():
    # Example usage
    print(day_of_week(5))

if __name__ == "__main__":
    main()