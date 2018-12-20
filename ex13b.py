#Exercise 13b Parameters, Unpacking , Variables
#Writing additional code that uses input and argv.

print('\nExercise 13 Parameters, Unpacking , Variables; additional tests')

from sys import argv
script, = argv

name = input('What is your name? ')
# print(f'{name} is running the script called', script)

#This version uses .format() to use the name input. It goes after the string.
# print('\n{} is running the script called'.format(name), script, '\n')


print('\n{} is running the script called'.format(name), script, '\n')

#NOTE: the (.format) needs to come right after the sentence. Each element called needs separation by a comma.

# this push will be made with a comment after typing git push
