#ex5 More Variables and Printing

name ='John'
age = 47
height = 72 #inches
weight = 185 #lbs.
eyes = 'Blue'
teeth = 'White'
hair = 'Blonde'

print (f"Let's talk about {name}.")
print (f"He's {height} inches tall. Or he's {height * 2.54} centimeters tall.")
print (f"He's {weight} pounds heavy.")
print (f"He's {weight / 2.205} kilograms heavy.")
print ("Actually that's not oo heavy.")
print (f"He's got {eyes} eyes and {hair} hair.")
print (f"His teeth are usually {teeth} depending on the coffee.")

#this line is trick, try to get it exactly right
total = age + height + weight
print (f"If I add {age}, {height}, and {weight} I get {total}.")
print (".......")
