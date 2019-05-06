from battleship_board.gameboard import *

sh1 = Ship( [1,1],2,'h' )
bt = BattleShip(10,"test")
bt.add_ship(sh1)
sh2 = Ship( [2,1],3,'v' )
bt.add_ship(sh2)
bt.print_board()

assert bt.make_move([1, 1]) == (False, True, False)
assert bt.make_move([1, 2]) == (False, True, True)
assert bt.make_move([1, 4]) == (False, False, False)
assert bt.make_move([2, 1]) == (False, True, False)
assert bt.make_move([3, 1]) == (False, True, False)
assert bt.make_move([4, 1]) == (True, True, True)

bt.print_board()