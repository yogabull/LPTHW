# ex7.py This Exercise 7 from "Learn Python the Hard Way"
print ("Exercise 7 - More Printing")

print ("Mary had a little lamb.")
print ("Its fleece was white as {}." .format ('snow'))
print ("And everywhere that Mary went.")
print ("." * 10) #what'd that do? It printed ten periods

end1 = "C"
end2 = "h"
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

#watch end = ' ' at the end. try removing it to see what happens
#This line concatonates the variables end 1-6 and then adds a space
print (end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
#This line concatonates end7 through end 12. It prints on the same line as the above line.
print (end7 + end8 + end9 + end10 + end11 + end12)
# next line is a note to see if this is merged on git later.
print ("this should be in the work branch")

# Note: ",end = ' '"
# prints a space between the words cheese burger. It keeps the second line from printing on the next line
