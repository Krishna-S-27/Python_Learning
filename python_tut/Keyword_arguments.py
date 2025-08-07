# Keyword arguments = an argument preceded by an identifier helps with readability 
# order of arguments does'nt matter
# 1.positional   2. default  3. KEYWORD  4.arbitrary

# we are fixing the key word for the values when we are sending the function.

def hello(greeting, title, first,last):
    print(f"{greeting} {title}{first} {last}")
hello("Hello","krishna","Mr.","Shalawadi")

#Keyword arguments 
hello(greeting="Hello",title="Mr.",first="Krishna",last="Shalawadi")