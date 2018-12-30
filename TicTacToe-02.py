game = 'I want to play a game'
print(id(game), game)

def game_board(player=0, row=0, column=0, just_display=False):
    global game
    game = "A game"
    print(id(game), game, '\n')

game_board()
print(game, id(game))
