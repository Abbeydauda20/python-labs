# List is mutable, Tuple is immutable - once you create them you cant change them - tuple will always have more than one element

# lst = [1,2,3,4]
#
# print(lst)
#
# lst.append(5)
#
# print(lst)

# first_tuple = (1,2,3,4)
# print(type(first_tuple))
# print(first_tuple)
#
# from root_level_variables import aws_configuration
# print(aws_configuration)

# lst = [1,2,3,4,['x','y','z'],[1,2,3],[True,False],(1,4,7)]
# print(lst)
# first_tuple = (1,2,3,4,'Ashish',True,[1,2,3],(3,4))
# print(first_tuple)

# lets change the tuple inside the list
# lst = [1,2,3,4,['x','y','z'],[1,2,3],[True,False],(1,4,7)]
# print(lst)
# lst[-1] = (900,800,500)
# lst[0] = 'x'
# lst[4] = True
# lst[5] = ['x','y','z']
# lst[6] = 1
# lst[7] = [1,2,33,567567,554]
# print(lst)

# first_tuple = (1,2,3,4,'Ashish',True,[1,2,3],(3,4))
#
# first_tuple[0] = 2  # doesnt work, tuples cant be changed

#append to list inside a list

# lst = [1,2,3,4,['x','y','z'],[1,2,3],[True,False],(1,4,7)]
# print(lst)
# lst[4].append('ashish')
# lst[5].append(4)
# lst[5].append(5)
# lst[5].append(6)
# print(lst)
# print(type(lst))
# print(type(lst[0]))
# print(type(lst[1]))
# print(type(lst[2]))
# print(type(lst[3]))
# print(type(lst[4]))
# print(type(lst[5]))
# print(type(lst[6]))
# print(type(lst[7]))


# my_tuple = (1,2,3)
# print(my_tuple[0:2])

# print(my_tuple(0:2))
#
# variable_name[start_index:end_index]
#
# variable_name -- datatype doesnt matter -- this can be list, can be tuple


# a = my_tuple[0]
# b = my_tuple[1]
# c = my_tuple[2]
# print(f"a = {a}")
# print(f"b = {b}")
# print(f"c = {c}")

# a,b,c = my_tuple
# print(f"a = {a}")
# print(f"b = {b}")
# print(f"c = {c}")
#
# a, b = [20,100]
# print(a)
# print(b)

# x = '1','2','3'
# print(type(x))
# print(type(x[0]))
# print(type(x[1]))
# print(type(x[2]))
# print(type(x))
# x = (1,3,5,6)

# in tuple you need to have more than one elements
# x = (1)
# print(type(x))  # int
# x = ("Ashish","xyz")
# print(type(x))

#
# x = [1]
# print(type(x))  # list

# my_tuple = (1,2,3,4,5,6,7,8,9,10,1,1,1)
# #
# # for item in my_tuple:
# #     print(item)
# #
# # # in
# # print(11 in my_tuple)
#
# print(my_tuple.count(1))
# print(my_tuple.index(10))  # returning index of that item

# dict1 = {1:"Ashish",2:"John",3:"Joseph"}
#
# for key,value in dict1.items():
#     print(f"Key : {key}")
#     print(f"Value : {value}")




