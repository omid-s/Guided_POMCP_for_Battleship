import os
import numpy as np
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
        self.time_to_solve = 0
        self.initial_beliefs = None
        self.init_sampelingConst = 50000

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


    def generate_initial_beliefs_by_sampling(self):
        """
        if belief file is present  it will read the file as the initial beleifs
        other wise the system will generate the beliefs

        :return:
        """
        if os.path.isfile("beleifs.npy"):
            self.initial_beliefs = np.load("beleifs.npy")
            return

        freq_meter = np.zeros((self.board_to_solve.boardSize, self.board_to_solve.boardSize))
        ship_sizes  = []
        for ship in self.board_to_solve.ships:
            ship_sizes.append(ship.length)

        for i in range(self.init_sampelingConst):
            bt = BattleShip(self.board_to_solve.boardSize,"")
            bt.generate_random(ship_sizes)
            bt.board[bt.board>0] = 1
            freq_meter+= bt.board

        freq_meter /= self.init_sampelingConst # convert frequency to probability

        np.save("beleifs.npy",freq_meter)


