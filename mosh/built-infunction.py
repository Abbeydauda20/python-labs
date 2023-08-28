# String built-in-methodology/functions
# This is used to change feature and style of characters .e.g capital letters, all upper case etc
# message = ("corona vaccines are ready to use, most of them are 90 % ready")
# print(message)
# print(message.capitalize())

#dir() function
#print(dir(message))
#print(dir(""))
#print(dir([]))  # list
#print(dir(()))  #Tuple
#print(dir({}))  #Dictionary

# with output all in upper case
#print(message.upper())

# # to check the type of character
#print(message.isupper())
#print(message.islower())
# # This finds the position where the word starts from
# print(message.find("ready"))
# # This returns -1 because the word can not be found in the statement
# print(message.find("parasite"))
# # This is used to find positions of letters in a word
# print(message[20:25])

###############################
# # Building function with JOIN
# # This is used to join all numbers together
# seq1 = ("192", "168", "40", "60",)
# print(".".join(seq1))
# print("/".join(seq1))

##############################
# # Building function with list, this is used to add to a list of existing items
#mountains = ["Everest", "k2", "kilimanjaro", "Himalaya", "Alps"]
#print(mountains)
# print(mountains.append("oregon mountain"))
# print(mountains)
# # Extend the existing list with new list of items
# print(mountains.extend(["Mount olivet", "Mount Zuma", "Mount rainer"] ))
# print(mountains)
# # Change position of item
# print(mountains.insert(2, "Mount olivet"))
# print(mountains)
# # To delete an item from the list us pop
# # This removes the last item
# print(mountains.pop())
# print(mountains)
# # This removes a certain item e.g. Alps
# print(mountains.pop(5))
# print(mountains)

#############################
# #Built-in-function for Dictionary
# # This helps returns both keys and values in Dictionary
# contract_staff1 = {"Name": "Santa", "Skill": "Blockchain", "Code": 12345}
# print(contract_staff1.keys())
# print(contract_staff1.values())
# # To clear everything, this gives an empty dictionary output
# print(contract_staff1.clear())
# print(contract_staff1)


