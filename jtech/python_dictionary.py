""" Dict - Key:Value

'name':'ashish'

{
key1:value1,
key2:value2,
key3:value3
...
}"""

emp = {
    'id': 1,
    'name':'ashish',
    'country':'usa',
    'age':30
}

# print(emp)
# print(type(emp))

# how to get all the keys

# dict_keys = emp.keys()
# print(dict_keys)
# print(type(dict_keys))
# for key in dict_keys:
#     print(f"Key : {key}")

# how to get all the values

# dict_values = emp.values()
# print(dict_values)
# print(type(dict_values))
# for value in dict_values:
#     print(f"Value: {value}")

# how to access the values
# dict1[key] --> value

# print(emp['age'])
# print(emp.get('name'))

# if the key doesnt exist

# print(emp['city'])
# print(emp.get('city'))   # default is None
# print(emp.get('city','Not Found'))  # we are changing the default to 'Not Found'

# how to add to dict or how to change the value

# print(emp)
# emp['state'] = 'ga'  # creating a new key and assigning value
# print(emp)
# emp['age'] = 32      # its updating the value for the key
# print(emp)

# How to get length of dict

# print(len(emp))

# How to get keys and values together

# emp.keys() -- returns keys
# emp.values() -- returns values
# emp.items() -- returns tuples of key,value
# print(emp.items())
# t1,t2 = (1,2)  -- we can receive tuple values in two variables, we will do same for dict.items
# print(t1,t2)
# for key,value in emp.items():
#     print(f"Key: {key} | Value: {value}")
#     # print(key,value)

# update dict

# dict1 = {'id':1,'name':'ashish'}
# dict2 = {'country':'usa','state':'ga'}
# print(dict1)
# print(dict2)
# dict1.update(dict2)
# print(dict1)
# print(dict2)

# delete and clear

# dict1 = {'id':1,'name':'ashish','country':'usa','state':'ga'}
# print(dict1)
# del dict1['state']
# print(dict1)
# dict1.clear()
# print(dict1)

# pop -- pop returns the value on the key before deleting key:value pair

# dict1 = {'id':1,'name':'ashish','country':'usa','state':'ga'}
# print(dict1)
# x = dict1.pop('state')
# print(x)
# print(dict1)

# if the state is not in 'ny','nj','ct' then delete else dont delete
# 1st method
# records = [
# {'id':1,'name':'ashish','country':'usa','state':'ga'},
# {'id':1,'name':'ashish','country':'usa','state':'ga'},
# {'id':1,'name':'ashish','country':'usa','state':'ny'},
# {'id':1,'name':'ashish','country':'usa','state':'ga'}
# ]
#
# dict1 = {'id':1,'name':'ashish','country':'usa','state':'ga'}
# # state = dict1['state']
# # if state not in ['ny','nj','ct']:
# #     del dict1['state']
#
#
# # # 2nd method
# x = dict1.pop('state')  # -- pop state get the value in x
# if x in ['ny','nj','ct']:   # -- checking if x(which is what we just poped) is in ny,nj and ct and if yes we want to put it back, coz we wanted not to delete ny,nj,ct
#     dict1['state'] = x




