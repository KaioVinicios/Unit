import pkg.check as check
import pkg.choice as choice
import pkg.utils as utils


MATRIX = utils.make_matrix()

PLAYER_1 = "X"
PLAYER_2 = "O"


player_turn = "X"
while True:
    utils.show_score()
    utils.show_game(MATRIX)

    choice.player_choice(MATRIX, player_turn)
    player_turn = PLAYER_2 if player_turn == PLAYER_1 else PLAYER_1 
    
    finished, winner = check.check_finish_game(MATRIX)
    if finished:
        if winner in ["X", "O"]:
            utils.save_into_db(winner, MATRIX)
            
        MATRIX = utils.make_matrix() 
