"""
File Operations - read / writing

"r"
"w"
"x"
"a"

"""

# read mode
# file1 = open("testing.txt", "r")
# content = file1.read()
# file1.close()
# print(content)

# read using with syntax


# with open("testing2.txt", "r") as file1:
#     content = file1.read()
#     print(content)

# filename = "testing1.txt"
# try:
#     with open(filename, "r") as file1:
#         content = file1.read()
#         print(content)
# except FileNotFoundError:
#     print(f"File {filename} not found")
# except Exception as e:
#     print(f"Error occured during file read operation: {e}")

# append mode
# with open("testing1.txt", "a") as file1:
#     file1.write("We are writing now in append mode\n")

#write mode This will overite everything in the file"
# with open("testing1.txt", "w") as file1:
#     file1.write("We are writing now in write mode")

# create mode, this will create a file and write on it assuming the file does not exist before
# with open("testing1.txt", "x") as file1:
#     file1.write("We are writing now in write mode")