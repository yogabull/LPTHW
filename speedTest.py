#Facebook user group coding

#tuple / list speed compared

from time import time

start = time() #list version
lst = [n for n in range (1000000)] # 1e6 element list
for _ in range(100): 999999 in lst #100 look-ups
list_time = (time() - start)
print(time() -start, "secs -list look-up")
print (list_time)

start = time() #tuple version
tup = (n for n in range(1000000)) #1e6 element tuple
for _ in range(100): 999999 in tup # 100 look-ups
print(time() - start, "secs - tuple look-up")
tuple_time = (time() - start)
print(tuple_time)

print("Searching the tuple was",list_time / tuple_time, "times faster than the list.")


# Another test from FB group
y = ('a', 'b', 'c')
x = ['ab','cd']
for i in x:
    i.upper()
for i in y:
    i.upper()
print(x)
print(y)
