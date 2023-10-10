import utils
import time
from functions import play_game, play_again

print(utils.logo)
board = utils.board

# play game
play_game(board)

time.sleep(2)

while True:
    # query user to play again
    play_again()
