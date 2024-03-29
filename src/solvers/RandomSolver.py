import random
from src.battleship_board.gameboard import BattleShip
from src.solvers.Solver import  Solver
from timeit import default_timer as timer

class RandomSolver(Solver):
    """
    an instance of the solver
    """
    def __init__(self, board: BattleShip):
        self.board_to_solve = board
        self.board_size = board.boardSize
        self.moves = 0
        self.time_to_solve=0

    def solve(self):
        """
        creates a naive always runnig loop until the game is solved
        :return:
        """
        start = timer()
        while True:
            x = random.randint(0,self.board_size - 1)
            y = random.randint(0, self.board_size - 1)
            self.moves += 1
            if self.board_to_solve.make_move([x, y])[0]:
                break
        end = timer()
        self.time_to_solve = end-start

    def stats(self):
        return self.moves, self.time_to_solve
