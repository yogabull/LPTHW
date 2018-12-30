game = [1, 2, 3]
print(id(game))

def game_board(player=0, row=0, column=0, just_display=False):
    print(game)
    # game = 'a game'
    game[1] = 99
    # print(id(game))
    print(game)

game_board()
print(game)
print(id(game))
