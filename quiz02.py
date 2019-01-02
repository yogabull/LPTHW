#Corey Shafer's Python list to get a job coding in Python:

#List Comprehensions
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 #Give me each number in a list squared
squares = [num*num for num in my_list]
print(squares)

cubes = []


#FizzBuzz
for num in xrange(1, 101):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print ("Buzz")
    else:
        print (num)


#Fibonacci Number a, b = 0, 1
for i in xrange(0-10):
    print (a)
    a, b = b, a + b


Fibonacci Generator #"yields" is key word to know you are using a Generatorself.
def fib(num):
    a, b = 0,1
    for i in xrange(0, num):
        yield "{}: {}".format(i + 1, a)
        a, b = b, a + b

for item in fib(10):
    print(item)





Know Class Template

class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_identity(self):
        print ("My name is {}.".format(self.name)


class SuperHero(Person):
    def --__init__(self, name, hero_name):
        super(SuperHero,self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print("... and I am {}".format(self.hero_name))
