#LIST
# zeros = [0]*5
# print(zeros)
#letters = ["a", "b", "c", "d", "e", "f"]
#combine = zeros + letters
#print(combine)
#print(letters[0:4])
#print(len(letters))
# #lst = [[0, 1], [2, 3]] #This is called Matrix

# numbers = list(range(20))
#print(numbers)

#chars = list("Hello world")
# print(chars)
# print(len(chars))

#numbers = list(range(20))
#print(numbers)
#print(numbers[::2])   #Skip every numbers
#print(numbers[::-2]) # In reverse order

# List unpacking
# numbers = [1, 2, 3, 4, 5, 6, 7]
# first, second, *others = numbers
# first, *others, last = numbers
# print(first, last)
# print(first)
# print(second)
# print(others)
# print(type(numbers))

#List unpacking
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# first, second, *other, last = numbers
# print(first)
# print(second)
# print(other)
# print(last)


#Enumerate list
#letters = ["a", "b", "c", "d", "e",]
#for i in letters:
#    print(i)
# for i in enumerate(letters):
#     print(i[1])
    
  #To apend or extend a list
  
# letters=  ["a", "b", "c", "d", "e", "f"] 
#letters.append("j")
# letters.insert(2, "m") #Inserts m in the index position 2
#letters.pop(2) #Removes the letter at a given index position 2
#letters.remove("b") # To remove an item you dont know its index number
#del letters[0:3] #del can remove a range of items but pop can only remove one item
#letters.pop() #Removes the last letter in the list
#letters.clear()  #To remove or delete all items in the list
#print(letters.index("d"))  #To find the index of a number

#To find is an item exists in the list
# if "e" in letters:
#   print(letters.index("e"))  #To find the index of a number
# print(letters)

################################################
#To sort items in a list

# Numbers = [1, 2, 4, 3, 6, 5, ]
# print(Numbers)
# print(sorted(Numbers))

# Letters = ["a", "b", "d", "c", "f", "e"]
# print(Letters)
# print(sorted(Letters))
# print(sorted(Letters, reverse=True)) #To sort items in reverse order

#Zip Function to pair items in different list groups
# list1 = [1, 2, 3, 4]
# list2 = [10, 20, 30, 40]
# print(list(zip(list1, list2)))
# print(list(zip("abcd", list1, list2)))

#STACKS: This explain a stacks of items piled together
#It makes us of LIFO which means: Last In First Out