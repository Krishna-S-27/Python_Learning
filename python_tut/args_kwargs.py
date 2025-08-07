# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple Keyword-arguments
#   * is a unpacking operator
#   1.positonal 2.default  3.keyword  4.ARBITRARY


# examples in *args

def display_name(*args):
    for arg in args:
        print(args, end=" ")

#display_name("Dr.","Spongebob","Harold", "Squarepants", "III")

def print_address(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_address(street = "123 Fake St.",
              apt = 100,
              city = "Detroit",
              state = "MI",
              zip = "54321")
