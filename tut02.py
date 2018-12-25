class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
    def eat(self,food):
        if (food == 'apple'):
            self.health -= 100
        else: (food == 'ham')
        self.health += 20

Bob = Hero('Bob')
print (Bob.name)
print (Bob.health)
Bob.eat('apple')
print (Bob.health)

print ('\n')

#New __init__ Tutorial
class Tuna:
    def __init__(self): #init functions are looked at first.
        print('Blrbrrbrer') #and this print statement is run first.

    #normal or basic funciton below:
    def swim(self):
        print('I am swimming')

#Object access stuff in a class. The object below is flipper..
#This object is created from the 'Tuna' class
# and then code within the class is run first.
# so 'Blrbrrbrer' is printed first before flipper.swim is run on the next line..
flipper = Tuna()
flipper.swim()
