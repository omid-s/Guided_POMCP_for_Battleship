
from battleship_board.gameboard import *

sh1 = Ship( [1,1],2,'h' )
bt = BattleShip(10,"test")
bt.add_ship(sh1)
bt.print_board()