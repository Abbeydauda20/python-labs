# Sets -- sets will only have unique values and they can not have duplicates

# []  - list
# () - tuple
# {} -- sets, dict

# a = {1,2,3}
# print(type(a))
# print(a)

# lst and tuple keep duplicates whereas sets get rid of duplicates
# a = {1,2,3,4,5,1,2,7,5,8,9,3}
# lst = [1,2,3,4,5,1,2,7,5,8,9,3]
# tuple1 = (1,2,3,4,5,1,2,7,5,8,9,3)
# print(a)
# print(lst)
# print(tuple1)

# we can have simple datatypes in set like string, int, float but we can not have list, dict, tuple, bool etc.
# True will be treated as 1 and False will be treated as 0 so depending on your elements it might give wrong results
# a = {1,2,3,4,'Ashish',True,1.5,False,True,200}
# print(type(a))
# print(a)

# a = {True,1,0,100,2,3,4,'Ashish',True,1.5,False,True,200}
# print(type(a))
# print(a)
#
# a = {True,False,True}
# print(a)

# b = {1,2,3,4,'Ashish',True,[1,2,3],(5,6,7),{1:'Ashish',2:'xyz'},['a','b','c']}
# print(type(b))
# print(b)

# empty set

# lst = []
# dct1 = {}
# set1 = set()
# print(type(lst))
# print(type(dct1))
# print(type(set1))

"""
dictionary - key value pair

key --> value


# name of people and which state they are from
dict1 = {
    "ashish": "GA",
    "john": "NY",
    "joseph": "CA"
}

set1 = {"GA", "NY", "CA"}

"""

# add

# set1 = {1,2,4,5,78,3,2,1,20}
# set1.add(100)
# set1.add(20)
# set1.add(30)
# print(set1)

# Update

# set1 = {1,2,3}
# set2 = {3,4,5,1,6}
# set1.update(set2)  # adding all element from set2 to set1
# print(set1)
# print(set2)

# set1 = {1,2,3}
# set2 = {3,4,5,1,6}
# set2.update(set1)  # adding all element from set1 to set2
# print(set1)
# print(set2)

# clear

# set1 = {1,2,3}
# print(set1)
# set1.clear()
# print(set1)

# Copy -- Deep Copy
# set1 = {1,2,3}
# print(set1)
# set2 = set1.copy()
# set1.add(20)
# set2.add(30)
# print(set1)
# print(set2)

# set1 = {1,2,3}
# set2 = set1  # pointer
# set1.add(20)
# set2.add(30)
# print(set1)
# print(set2)

# lst1 = [1,2,3]
# lst2 = lst1.copy()
# lst1.append(30)
# print(lst1)
# print(lst2)

# Pop

# lst1 = [1,2,3]
# print(lst1)
# lst1.pop()
# print(lst1)

# removing first element from sorted set
# set1 = {20,5,4,2,1}
# set1.pop()
# print(set1)

# Discard

# set1 = {20,5,4,2,1}
# print(set1)
# set1.discard(20)
# print(set1)

# set1 = {20,5,4,2,1}
# for item in set1:
#     print(item)


# set comprehensions

# set1 = {20, 5, 4, 2, 1,30,40,15,10,9,27}
# # we want only elements greater than 20 from this set
#
# set2 = set()
# for item in set1:
#     if item>20:
#         set2.add(item)
#
# print(set2)
#
# # Alternative method to do the same thing using set comprehensions
#
# set2 = {item for item in set1 if item>20}
# print(set2)

# Basic set operations - like Union, Intersection, -- Set Theory


set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union

# union_set_1st_method = set1.union(set2)
# union_set_2nd_method = set1 | set2
#
# print(set1)
# print(set2)
# print(union_set_1st_method)
# print(union_set_2nd_method)

# Intersection

# x = set1.intersection(set2)
# y = set1 & set2
#
# print(set1)
# print(set2)
# print(x)
# print(y)

# Minus / difference

# minus_set1_1st_method = set1.difference(set2)
# minus_set1_2nd_method = set1-set2
# minus_set2_1st_method = set2.difference(set1)
# minus_set2_2nd_method = set2 - set1
# print(minus_set1_1st_method)
# print(minus_set1_2nd_method)
# print(minus_set2_1st_method)
# print(minus_set2_2nd_method)

# Symetric Difference

# sym_diff_1 = set1.symmetric_difference(set2)
# sym_diff_2 = set1 ^ set2
# print(sym_diff_1)
# print(sym_diff_2)

#  == is supported for checking if two sets are same or not
# set1 = {1,2,3}
# set2 = {3,2,1,4}
#
# if set1 == set2:
#     print("Same")
# else:
#     print("Different")

