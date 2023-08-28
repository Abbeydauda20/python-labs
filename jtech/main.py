
"""
numeric - int, float

string - str 

sequence - list, tuple, range 

mapping - dict 

boolean - bool 

set - set 
"""

"""
Now we are going to talk about data types

"""

# -- for single line comments in code

""" This for multi line comments """

# a = 10

# b = 15.5 

# name = 'Ashish'

# # type -- this returns the data type

# num_list = [1,2,3,4,5]
# name_list = ['John','Jack','Ashish']

#mixed_list = [1,2,3,4,5,'Jack','Ashish',True, False, 10.6]

# list -- python list is a mutable data type 
# List indexes from left to right start from 0,1,.. and so on
# List indexes from right to left start from -1,-2,.. and so on

#print(mixed_list[-2])
#print(mixed_list[2:])
# slicing a list 
"""
We can slice a list to get any number of elements we want using  start_index:end_index operator
both start and end index are optional
the start index gets included in the result but you will get end-1 i.e element before the end index
"""



# length of list 


#              0,1,2,3,4,   5,     6,       7,    8,     9
# mixed_list = [1,2,3,4,5,'Jack','Ashish',True, False, 10.6]

# length_of_list = len(mixed_list)  # 10

# print(mixed_list[2:length_of_list])
# print(len(mixed_list))

# print(mixed_list[2:10])


# in python a string is a list of characters 

# name = 'Ashish'  --> ['A','s','h','i','s','h']

#name = ('Ashish')

#print(name[2:])

"""
lst = [1,2,3,4]

for item in lst:
    print(item)

name = 'Ashish'

for c in name:
    print(c)
"""

# Operation on the list

# append

# lst = [1,2,3,4]

#print(lst)
# lst.append(5)
# print(lst)

#print(lst.pop())
# print(lst)
# print(lst.pop(-2))
# print(lst)

# lst = [1,2,3,4]

# lst.append(5)
# lst.append(6)
# lst.append(7)

# lst = [1,2,3,4]

# lst1 = [5,6,7,8,9,10]

# lst = lst + lst1

# Tuple -- immutable data type

# product = ('Microsoft','Xbox',699.99)

# print(product)
# print(type(product))
# print(product[0])
# print(product[1])


# from root_level_variables import aws_configuration
#
# print(aws_configuration[1])

# Implicit Conversion

# x = 10
# print(type(x))
# y = 20.5
# print(type(y))
# z = x+y
# print(z)
# print(type(z))


# Explicit Conversion
# x = 10.9
# y = int(x)  # type conversion
# print(x)
# print(y)
# print(type(x))
# print(type(y))

# x = "10"
# y = int(x) # conversion to int
# print(x)
# print(y)
# print(type(x))
# print(type(y))

# x = "Ashish"
# y = int(x) # conversion to int won't work
# print(x)
# print(y)
# print(type(x))
# print(type(y))

# age = 30
# statement = "Your Age is : "
# # string           string      string(int)-> string
# final_statement = statement + str(age)
# print(final_statement)

# f string formatting

# age = 30
# final_statement = f"Your age is : {age}"
# print(final_statement)

# age = 30
# street_no = 34535
# annual_income = 234235.35
# f_string = (f"My age is {age} and I live at {street_no} street and my annual income is {annual_income}")
# concat_string = "My age is " + str(age)+" and I live at " + str(street_no)+ " street and my annual income is "+ str(annual_income)
# format_string = "My age is {0} and I live at {1} street and my annual income is {2}".format(age,street_no,annual_income)
# print(f_string)
# print(concat_string)
# print(format_string)


# age = 30
# final_statement = f"Your age is : {age}"
# concat_statement = "Your age is : " + str(age)
# print(type(final_statement))
# print(final_statement)
# print("Your age is: ",age)

# s3 -- lambda --> read --> processing --> store --> back to s3 with todays timestamp
# abc.txt -----------------------------------------> abc_07302023.txt
#
# filename = "abc.txt" --> split --> "abc"
# current_datetime = 07302023
# newname = "abc" + "_" + str(07302023) + ".txt"


# Arithmetic Operations
"""
+  -- Addition
-  -- Subtraction
*  -- Multiplication
/  -- Division
// -- Floor Division
%  -- Modulo
** -- Power
"""

# Assignment

"""
=    --> a = 10
+=   -->   a+=1  --> a = a+1  --> 11
-=   -->   a-=1  --> a = a-1  --> 10
*=   -->   a*=10  --> a = a*10 --> 100

"""

# comparision Operators

"""
== 
!=
>
<
>=
<=
"""

# a = 10
# b = 20
# c = a == b
# print(c)

# Logical Operators
"""
and 
or 
not

True and True  -- True
True and False -- False
True or True   -- True
True or False  -- True
not True and False -- False
True and not False -- True
"""

#
# a = 7
# b = 2
# print(a//b)

# -- round --> int
#
# a = 3.5  --> 4
#     3.4  --> 3

# round this to 2 decimal places

# a = 3.416  -- .006 -- .010   --> 3.42  --> 3.4  --> 3
# b = 3.464  -- .004 -- .000   --> 3.46  --> 3.5  --> 4

"""
is
is not
"""
#
# x = 5
# y = 10
# print(x is not y)
# print(x != y)

"""
Membership Operators
in
not in
"""

# x = 10
# y = [2,5,7,8,9,10]
# 
# print(x not in y)

# x = {1:'Ashish',2:"xyz"}
# y = 1
# if y in x:
#     print(y)

# you have a dict, you want to get value for a key
# x = {1:"Ashish",2:"xyz"}
# y = 3
# print(x.get(y))  # None
# print(x.get(y,"Not Found"))  # custom value

# Conditional Statements

"""if condition:
    # do this
    
    """

# a = 10
# if a == 10:
#     print("Ten")




# if age < 18 then Minor
# if age > 18 then Adult

# age = 17
# if age<18:
#     print("Minor")
# else:
#     print("Adult")
#
#
movie_rating = 6.5

# if rating < 5 then bad
# if rating >=5 and <6 then okay
# if rating >=6 and <7 then Good
# if rating>=7 Very Good

#
# if movie_rating<5:
#     print("Bad")
# elif 5<= movie_rating< 6:
#     print("Okay")
# elif movie_rating >=6 and movie_rating<7:   
#     print("Good")
#OR   
# elif 6 <= movie_rating <7:
#     print("Good")
# else:
#     print("Very Good")

# Nested Conditions

"""
# outer condition

if condition1:
    # do this

    # inner condition
    if condition2:
        # do this
        
"""

# pass a number and print if its positive, negative or zero
# num = 0

# if num>=0:
#     if num==0:
#         print('zero')
#     else:
#         print("positive")
# else:
#     print("negative")
#
#
# if num==0:
#     print("zero")
# elif num>0:
#     print("positive")
# else:
#     print("negative")

# for loop

# lst = [1,2,3,4,5]
# # #
# for element in lst:
#     print(element)

# print(lst[2:5])

# 'Ashish' --> ['A','s','h','i','s','h']  --> string is stored as list of characters
# for i in 'Ashish':
#     print(i)

# a = 'Ashish'
# print(a[2:-1])

# range

# print all even numbers between 1 and 100

# num = int(input('Enter the number: '))
# print(num)
# print(type(num))

# calculator
# where you will take input from user -- you will keep adding all the numbers that you get unless we get 0

# initialization
# total = 0
# num = int(input('Enter the number: '))
#
# while num !=0:
#     total += num  # total = total + num
#     num = int(input('Enter the number: '))
#
# print(f"Total Sum is : {total}")

# print numbers from 1 to 5

# initialization
# i = 1
# n = 5
#
# while i<=5:
#     print(i)
#     i = i + 1
#
# for i in range(1,6):
#     print(i)

# When you know how many iterations are going to happen use for loop otherwise use while loop

# dict1 = {1:"Ashish",2:"John",3:"Joseph"}
#
# for key,value in dict1.items():
#     print(f"Key : {key}")
#     print(f"Value : {value}")

# print(dict1.items())

# range

# for i in range(2,101,2):
#     print(i)

# for year in range(1901,2024):
#     for month in range(1,13):
#         print(f"year: {year}, month: {month}")

# for i in range(1,11):
#     if i == 5:
#         break
#     print(i)
# else:
#     print("done with the loop")
# print("Statement After the loop")
#
#
# for i in range(1,11):
#     if i == 5:
#         break
#     print(i)
# print("done with the loop")
# print("Statement After the loop")


# list of files -- upload all of them to s3 one by one

# for file in list_of_files:
#     s3.upload(file)
# else:
#     print("all files uploaded to s3")
#
# for file in list_of_files:
#     s3.upload(file)
# print("all files uploaded to s3")