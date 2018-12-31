#Ex 6 Strings and Text

#below defines the number of types_of_people
types_of_people = 10
#below is an f-string which which calls to insert the string types_of_people within the sentence.
x = f"There are {types_of_people} types of people."

# These next two lines assign strings to the varialbes 'binary' and 'do_not'
binary = "binary"
do_not = "don't"
#below uses an f-string to call the to string variables.
y = f"Those who know {binary} and those who {do_not}."
#below calls to print x and y which stands for "There are {types_of_people} types of people."
print (x)
print (y)

#below f-string calls for x and y to be aded to the sentencs.
print (f"I said: {x}")
print (f"Ialso said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny ?! {}"
print (joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = " a string with a right side."
# below concatonates the two strings above: w and e.
print (w+e)
