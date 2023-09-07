"""

Python Functions -

def function_name(arguments) --> return type:
    # function body
    # return is optional

"""


# define a function that prints Hello
# def greet():
#     print("Hello")
#
# greet()

# pass name as argument
#
# def greet(name):
#     print(f"Hello {name}")
#
# greet("Ashish")

# create a function to add two integers and printing

# def add_numbers(num1, num2):
#     sum = num1 + num2
#     print(f"num1 : {num1}")
#     print(f"num2 : {num2}")
#     print(f"Sum : {sum}")
#
#
# a = 10
# b = 20
# add_numbers(a, b)


# create a function to add two integers and return the value back

# def add_numbers(num1, num2):
#     return num1 + num2
#
# a = 10
# b = 20
# c = add_numbers(a, b)
# print(c)

# create a function to return 5 times first number + 10 times second number

# def add_number_with_multiply(num1: int,num2: int) -> int:
#     return (5*num1)+(10*num2)
#
# a = 10
# b = 20
# # c = add_number_with_multiply(b, a)
# # print(c)
# c = add_number_with_multiply(num1=a, num2=b)
# print(c)
# c = add_number_with_multiply(num2=b, num1=a)
# print(c)

# default value of function arguments
# create a function which adds 1 to a sequence and returns the value
#
# def increment_sequence(num: int, step_size: int = 1) -> int:  # Type hint - we are taking one integer and returning one integer
#     return num + step_size

# without type hinting
# def increment_sequence(num, step_size=1):
#     return num + step_size

# seq = 1
# print(seq)
# next_seq = increment_sequence(seq)
# print(next_seq)
# next_seq = increment_sequence(next_seq,2)
# print(next_seq)
# next_seq = increment_sequence(next_seq,5)
# print(next_seq)


# seq = int(input('Enter the start of Sequence: '))
# step_size = int(input('Enter the Step Size: '))
# print(increment_sequence(seq,step_size))

# def does_something(a=1,b=1,c=1):
#     return a+b+c
#
# print(does_something())
# print(does_something(10))
# print(does_something(10,4))
# print(does_something(10,4,6))
# print(does_something(a=10))
# print(does_something(b=10,c=4))


# variable arguments

# I want to define a function to add numbers and return

# *args  --


# def add_numbers(*numbers):
#     sum = 0
#     for num in numbers:
#         sum = sum + num
#     print(f"Sum: {sum}")
#
#
# add_numbers(1,2)
# add_numbers(10,20,24,56)
# add_numbers(1,2,3,4,5,6,7)

# take name, id and age as input from user and create and return a dict object

# def create_dict(id: int, name: str, age: int, *others) -> dict:
#     dict1 = {'id': id, 'name': name, 'age': age}
#     print(others)
#     return dict1


# returned_dict = create_dict(1, 'ashish', 30, 'usa')  # positional arguments work
# print(returned_dict)

# returned_dict = create_dict(id=1, name='ashish', age=30, 'usa')  # named arguments dont work
# print(returned_dict)


# use variable auguments to create a dict on the fly

# ** -- dict, named auguments
# ** -- works with named arguments because it will use it to create key, value pair
# * - works with positional arguments
#
# def create_dict(**inputs):
#     return inputs


# returned_dict = create_dict(id=1, name='ashish', age=30)
# print(returned_dict)
# returned_dict = create_dict(id=1, name='ashish')
# print(returned_dict)
# returned_dict = create_dict(id=1, name='ashish', age=30, country='usa', state='ga')
# print(returned_dict)
#
# print(create_dict(x=1,y=20,name='ashish',a=10,b=40,c=10.5))


def just_for_the_sake_of_it(x,y,z,a,b,*yy,**zz):
    print(f"x: {x} | Type: {type(x)}")
    print(f"y: {y} | Type: {type(y)}")
    print(f"z: {z} | Type: {type(z)}")
    print(f"a: {a} | Type: {type(a)}")
    print(f"b: {b} | Type: {type(b)}")
    print(f"yy: {yy} | Type: {type(yy)}")
    print(f"zz: {zz} | Type: {type(zz)}")

# just_for_the_sake_of_it(10,'ashish',20,40,70,state='GA',country='USA',age=30,id=20)

just_for_the_sake_of_it(10,'ashish',20,40,70,1,2,3,4,'x','y',state='GA',country='USA',age=30,id=20)