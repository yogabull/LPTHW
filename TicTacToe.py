# sentdex Python tutorial of a Tic Tac Toe game.

def addition(x, y):
    return x + y

game = [[0, 0, 0], #here is a list of three lists.
        [0, 0, 0],
        [0, 0, 0],]

# functions are lower-case and use underscores to be pep8 compliant. # Class get title-case.
# defines function: game_board
def game_board(player=0, row=0, column=0, just_display=False): #defaults to zero.
    print("\n   a  b  c")
    if not just_display:
        game[row][column] = player # this designates a cell and changes it to the player's number.
    for count, row in enumerate(game):
        print(count, row)

game_board(just_display=True) # this changes just_display to true so pass the if-not statement above
game_board(player=1, row=2, column=1)


# game[0][1] = 1 # print (game) # print (type(game))

# game_board() #calling the function.
#         #Just writing game_board points to function and does not run it.






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
'''
