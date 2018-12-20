#Exercise 13 Parameters, Unpacking , Variables

print('\nExercise 13 Parameters, Unpacking , Variables')

#original code from exercise.
    # from sys import argv
    # # read the WYSS section for how to run this
    # script, first, second, third = argv

    # from sys import argv
    # # read the WYSS section for how to run this
    # script, first, second, third, fourth = argv

    #Here is another input method to pass variables.
    #this line imports the module 'argv' which stands for _argument variable_
from sys import argv

    #This line sets the number of arguments needed to run the code/script
    #In this case the script is calling six arguments including the file's name (ex13.py).
    # this line unpacks the module and assigns variable names to each argument.
script, first, second, third, fourth, fifth = argv

print('The script is called:', script)
print('Your first variable is:', first)
print('Your second variable is:', second)
print('Your third variables is:', third)
print('Your fourth variable is:', fourth)
print('Your fifth variable is:', fifth)

#Note: when you run the script from the terminal, you are actually passing the file name (i.e. ex13.py) as an argument.
print('This exercise demonstrates how to import modules (additional features), and pass arguments when running a script that imports the module.')
