#Exercise 13b Parameters, Unpacking , Variables
#Writing additional code that uses input and argv.
#
# print('additional tests')

from sys import argv
fileName, first, second, third = argv

print('The script is called:', fileName, '\nThe first argv value is the name of this script.\n')
print('Your first variable is:', first, '\nThe second argument called is the first value after you type the script\'s name.\n')
print('Your second variable is:', second)
print('Your third variable is:', third)


name = input('What is your name? ')
print(f'{name}, you are running the script called', fileName)

#This version uses .format() to use the name input. It goes after the string.
# print('\n{} is running the script called'.format(name), script, '\n')


print('\n{}, your script is'.format(name), fileName, '\n')

#NOTE: the (.format) needs to come right after the sentence. Each element called needs separation by a comma.

# Note about Git. Work on a branch. If you push to Github while working on the master it will automatically merge with the online masterself.
# If you push a branch, it will prompt you to make duplicate the branch online.
# When you push from a branch it will ask you to type: git push --set-upstream origin work (work is the branch's name).
