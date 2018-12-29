# sentdex Python tutorial of a Tic Tac Toe game.

def addition(x, y):
    return x + y

z = (addition(5,3))
print(z)


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

game[0][1] = 1 # print (game) # print (type(game))

# functions are lower-case and use underscores to be pep8 compliant. # Class get title-case.
def game_board():
    print("\n   a  b  c")
    for count, row in enumerate(game):
        print(count, row)






# x = game_board this is a way to call the game_board function quickly.

# game_board() #calling the function.
#         #Just writing game_board just points to function and does not run it.

game[0][1] = 1 # this places a one in a cell.






'''work on slicing the list.

print(l[2:4])
print(l[-3]) # this references three.
print(l[-1]) #this references the five.
print(l[1]) # references two.

print (l)
l[1] = 99 # this made the two into 99
print (l)
'''

'''reproducing this code by making a function so display game-map after each move.
#repetition means use a function.
print("\n   a  b  c")
for count, row in enumerate(game):
    print(count, row)
'''
