from isolation import Board
from sample_players import RandomPlayer
from sample_players import GreedyPlayer
from game_agent import AlphaBetaPlayer
from game_agent import MinimaxPlayer
import timeit

# create an isolation board (by default 7x7)
time_limit = 150
time_millis = lambda: 1000 * timeit.default_timer()
move_start = time_millis()
time_left = lambda : time_limit - (time_millis() - move_start)

player2A = RandomPlayer()
player2B = RandomPlayer()
playerA = AlphaBetaPlayer()
playerB = MinimaxPlayer()

gameA = Board(playerA, player2A)
gameB = Board(playerB, player2B)

gameA.play()
gameB.play()

print(gameA.to_string())
print(gameB.to_string())

#print(playerA.get_move(gameA, time_left))
#print(playerB.get_move(gameB, time_left))
print("\n -----------------")
#gameA.apply_move((0,1))
#print(playerA.max_ab_value(gameA.forecast_move((0,1)),playerA.search_depth,float("-inf"),float("inf")))
##game.apply_move((6,3))
##game.apply_move((5,4))
##game.apply_move((5,5))

##game.apply_move((6,6))
##game.apply_move((3,6))
##game.apply_move((4,5))
##game.apply_move((2,4))
##game.apply_move((6,4))
##game.apply_move((3,2))
##game.apply_move((5,6))
##game.apply_move((5,3))
##game.apply_move((3,5))
##game.apply_move((6,5))
##game.apply_move((2,3))
##game.apply_move((4,6))
##game.apply_move((3,1))
##
##print(player1.search_depth)
##print(player1.get_move(game,150))
##print(game.to_string())

