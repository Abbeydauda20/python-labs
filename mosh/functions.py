# def greet(fist_name, last_name):
#     print(f"Hello {fist_name}, {last_name}" )
#     print("welcome aboard")

# greet("Abbey", "Dauda")
# greet("John", "Smith")


# Type of functions
# 1. Function that performs a task example below
# def greet(fist_name, last_name):
#     print(f"Hello {fist_name}, {last_name}" )
#     print("welcome aboard")
# greet("Abbey", "Dauda")
# greet("John", "Smith")


# 2. Function that returns a value
# def increment(number, by):
#     return number + by
# print(increment(number=2, by=1))
# print(increment(number=5, by=5))

def increment(number, by):
    return number + by
print(increment(2, 5))
print(increment(5, 5))

# def increment(number, by=1):
#     return number + by
# print(increment(2))
# print(increment(5))

# def multiply(*numbers):
# return(numbers)
# print(2, 3, 4, 5, 6, 10)


# def multiply(*numbers):
#     total = 2
#     for i in numbers:
#         total *= i
#     return total


# print(multiply(2, 3, 4, 5))

'''Explanation of the above:
Initialize total to 2: total = 2
First iteration: total *= 2, total = 2 * 2 = 4
Second iteration: total *= 3, total = 4 * 3 = 12
Third iteration: total *= 4, total = 12 * 4 = 48
Fourth iteration: total *= 5, total = 48 * 5 = 240   
'''

# using multiple asterisk python can package multiple values for us
# def save_user(**user):
#     print(user["age"])
# save_user(id=2, name="John", age=22)

#Global vs Local variable
# message = "c"


# def greet(name):
#     message1 = "b"


# greet("Mosh")
# print(message)



