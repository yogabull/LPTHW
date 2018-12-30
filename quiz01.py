print('Quiz: Mutable code\n\n')

x = 1 #x is integer
def test(): #defined function called test.
    x = 2 # tries to change x, but can't because it is not mutable.
    print(id(x))
test() #called function test
print(x) #print x
print(1)
print()

x = 1 # x is integer
def test(): #defined funtion
    global x # made x a global object so it is mutable within a funtion.
    x = 2
test() # called function test
print(x)
print(2)
print()


x = [1] # x is a list
def test(): # defined function x
    x = [2] # A new object 'x' is created because x is not mutable within the function.
    print(id(x))
test()
print(x)
print(id(x))
print(1)
print()

x = [1]
def test():
    global x
    x = [2]
test()
print(x)
print(2)
print()

x = [1]
def test():
    x[0] = 2
test()
print(x)
print(2)
