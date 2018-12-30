game = [[0, 0, 0], # This is a list of lists. Or three lists within the list game.
        [0, 0, 0],
        [0, 0, 0]]

#this defines function 'game_board'.
#game_map is a temporary variable for the list game.
# this passes 'game' in for 'game_map' every time function is called essentially updating game status in function.
# This is necessary because game is imutable within the function.

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    print('\n   0  1  2') # terminal visual for columns.
     # this is passed when 'just_display' is false.
    if not just_display: # note: if no value is passed for just_display, then it assumes true.
        game_map[row][column] = player
        # When 'just_display' is False, game_map will be reset with 0s player's number (x or o).
        # Not passing player, row or column resets the 0 to column/row. I don't think we want this.
        print('False was passed')
    for count, row in enumerate(game_map): # prints numbers for each row in game board
        print(count, row) # the number for first row is printed, then the row (or each item in list)
    return game_map # this allows us to update the 'game' with a player's move. Game is then made equal to 'game_map'. Again, this is done because 'game' is not mutable in this function.


game = game_board(game, just_display=True)
game_board(game, player=2,row=0, column=0)

for row in game:
    print(row)

game_board(game, player=1,row=2, column=2)
game_board(game, player=1,row=2, column=2, just_display=True)
game_board(game, just_display=False)
print(game)
game_board(game)
print(game)
