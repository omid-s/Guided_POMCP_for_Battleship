from battleship_board.gameboard import *
from src.solvers.RandomSolver import RandomSolver
from src.solvers.SmartRandomSolver import SmartRandomSolver
sh1 = Ship( [1,1],2,'h' )
bt = BattleShip(10,"test")
bt.add_ship(sh1)
sh2 = Ship( [2,1],3,'v' )

assert bt.add_ship(sh2)==0
assert bt.add_ship(sh2)!=0

bt.print_board()

assert bt.make_move([1, 1]) == (False, True, False)
assert bt.make_move([1, 2]) == (False, True, True)
assert bt.make_move([1, 4]) == (False, False, False)
assert bt.make_move([2, 1]) == (False, True, False)
assert bt.make_move([3, 1]) == (False, True, False)
assert bt.make_move([4, 1]) == (True, True, True)

bt.print_board()

bt2 = BattleShip(10,"test")

bt2.generate_random([2,3,3,4,5])
bt2.print_board()

slv  = RandomSolver( bt2 )
slv.solve()
print( slv.stats() )

bt2 = BattleShip(10,"test")

bt2.generate_random([2,3,3,4,5])
bt2.print_board()

slv  = SmartRandomSolver( bt2 )
slv.solve()
print( slv.stats() )
bt2.print_board()