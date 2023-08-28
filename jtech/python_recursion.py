
"""
calling function inside another function

"""

# write a function that adds and sub 2 numbers

# def add_and_sub(x: int, y:int):
#     return x+y, x-y
#
# x = 10
# y = 20
# a, b = add_and_sub(x,y)
# print(a)
# print(b)
# print(type(a))
# print(type(b))
#
# def add(x: int, y: int):
#     return x+y
#
# def sub(x: int, y: int):
#     return x-y
# #
# def add_and_sub(x: int, y:int):
#     a = add(x,y)
#     b = sub(x,y)
#     return a, b
# #
# x = 10
# y = 20
# a, b = add_and_sub(x,y)
# print(a)
# print(b)
# print(type(a))
# print(type(b))


# What if the function calls itself inside the function
# when a function calls itself its called recursion

# def recurse():
#     ..
#     recurse()


# Factorial

# Factorial using Loops
# function definition
# def fact(x: int):
#     output = 1
#     if x == 1:
#         return output
#     while(x>1):
#         output = output*x
#         x = x -1
#     return output

# function call
# y = fact(7)
# print(y)


# recursion

# def fact(x: int):
#     if x == 1:
#         return 1
#     else:
#         return (x * fact(x - 1))

#function call
# y = fact(3)
# print(y)
#
# fact(3)    # 1st call with 3
# 3 * fact(2)  # 2nd call with 2
# 3 * 2 * fact(1) # 3rd call with 1
# 3 * 2 * 1   # return from 3rd call as 1
# 3 * 2       # return from 2nd call we get 2x1 = 2
# 6           # return from 1st call we get 3*2 = 6
