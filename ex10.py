print ("Exercise 10: What Was That?")
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#Noted Version below with escape sequences.
#The \ (backslash) character encodes difficult-to-type characters into a string.
#variable with a Horizontal Tab
tabby_cat = "\tI'm tabbed in."
#variable with an encoded line break.
persian_cat = "I'm split\non a line."
#variable encoded with a \ (backslash) to let an actual \ (backslash) print.
backslash_cat = "I'm \\ a \\ cat."

#a fourth varible with tabbed bulleted list.
#The encoding adds tabs (\t) and a line break (\n)
#The whole list is contained within tripple quotes so you can contain muliple lines within in one print function.
fat_cat = '''
I'll do a list:
\t* \tCat food
\t* \tFishies
\t* \tCatnip\n\t*\tGrass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


#DO BEFORE COMPLETE: write down all Escape Sequences (page 35).
#here's a start:
print ('''
Here is a list of Escapte Sequences:
\\\\        Backslash (\\)
\\'         Single-quote(\')
\\"         Double-quote (\")
\\a         ASCII bell (BEL)
\\b         ASCII backspace (BS)
\\f         ASCII formfeed (FF)
\\n         ASCII linefeed (LF)
\\N{name}   Character named name in the Unicode database (Unicode only)
\\r         Carriage return (CR)
\\t         Horizontal tab (TAB)
\\Uxxxx     Chracter with 16-bit hex value xxxx
\\Uxxxxxxx  Character with 32-bit hex value xxxxxxxx
\\v         ASCII vertical tab (VT)
\\000        Character with octal value 000
\\xhh        Character with hex value hh
    ''')

# the (\a) makes an alert (bell) sound. Not sure what \b does, but \f adds a line space.
print("here is a test: \a \b \f")

# Not sure what this does: \N{name}
print("here is a second test: \n \r \t Let\'s see the test")
