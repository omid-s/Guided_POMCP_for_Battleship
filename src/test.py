
from battleship_board.gameboard import *

sh1 = Ship( [1,1],2,'h' )
bt = BattleShip(10,"test")
bt.add_ship(sh1)
sh2 = Ship( [2,1],3,'v' )
bt.add_ship(sh2)
bt.print_board()