#PyBites code challenge about f=strings and simple if/else statements: https://codechalleng.es/bites/101/


min_driving_age = 16
name = input("Hi, what is your name?")
age = input("How old are you?")

if age < min_driving_age:
    print(f"{name}, you are not allowed to drive.")
else:
    print(f"{name}, you are allowed to drive.")
