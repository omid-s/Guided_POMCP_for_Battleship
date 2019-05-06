import random
from src.battleship_board.gameboard import BattleShip
from src.solvers.Solver import  Solver
from timeit import default_timer as timer

class POMCPSolver(Solver):
    """
    POMCP based solver for game of battleship
    initial beliefs can be set by either an even distribution
    or by a sampling method.
    if sampling method is selected, solver will look fora saved file
    if not found will regenerate the initial beliefs
    """
    def __init__(self, board: BattleShip):
        self.board_to_solve = board
        self.board_size = board.boardSize
        self.moves = 0
        self.time_to_solve=0

    def solve(self):
        """

        :return:
        """
        start = timer()
        # TODO : create the POMCP slever
        end = timer()
        self.time_to_solve = end-start

    def stats(self):
        return self.moves, self.time_to_solve

    