#Exerciase 15: Reading files
print('Exercise 15: Reading files')
#sys is a package.
#the statement below says get the 'argv' feature from the 'sys' package.
from sys import argv

script, filename = argv
#here the parameter 'filename' is OPENED and assigned to the variable 'txt'
txt = open(filename)

print(f"Here's your file using 'argv': {filename}")
#Here we call a function (read) on the variable 'txt'
print(txt.read())
print(' ')

print("Type the filename again:")
file_again = input()

print('Here is the test text file retrieved from a user input:')
txt_again = open(file_again)

print(txt_again.read())
