"""
Scope of variables

1. Local Variables - if we define any variables inside a function those are local variables and we can only access them inside the function
2. Global Variables - we can define global variables outside the function that can be accessed inside the function but the preference
will be to local variables first if found.
"""

# fuction definition
# def add(y: int, x: int):
#     print(f"inside function value of x : {x}")
#     print(f"inside function value of y : {y}")
#     s = x + y
#     return s


# function call
# x = 10
# y = 20
# print(add(10,20))
# print(s)
# print(f"outside function value of x : {x}")
# print(f"outside function value of y : {y}")

# Global
# msg = "Hello"
#
#
# def greet():
#     # msg = "Bye"
#     print(f"Local message {msg}")
#
#
# greet()


# c = 1 # global variable
#
# def add():
#     print(c)
#
# add() # this will print 1 and works fine accessing global variable
#


c = 1 # global variable

def add():
    # increment c by 1
    global c
    c = c + 1
    print(c)

print(c)
add()
print(c)


