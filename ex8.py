#Exercise 8
print ("Exercise 8: Printing, Printing")

formatter = "{} {} {} {}"

print (formatter.format (1,2,3,4))
print (formatter.format("one", "two", "three", "four"))
print (formatter.format(True, False, False, True))
print (formatter.format(formatter, formatter, formatter, formatter))
print (formatter.format(
    "Try your",
    "Own text here.",
    "Maybe a poem",
    "Or a song about fear"
))
print ("\n")


print ("NOTE VERSION")

#below is a variable called formatter. It can take four arguements within {}.
formatter = "{} {} {} {}"

# this line uses the format function to pass four arguements into the formatter variable.
print (formatter.format (1,2,3,4))
#the format function passes four strings as arguements.
print (formatter.format("one", "two", "three", "four"))
#the format function passes four key words that become strings if encompassed within quotes.
print (formatter.format(True, False, False, True))
#the variable "formatter" is passed through itself which prints four sets of 4-{}s.
print (formatter.format(formatter, formatter, formatter, formatter))
#the format function passes four strings as arguements which makes a sentence on one line.
print (formatter.format(
    "Try your",
    "Own text here.",
    "Maybe a poem",
    "Or a song about fear"
))
#this prints a new line. Note it uses a backslash.
print ("\n")
