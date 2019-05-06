from src.battleship_board.gameboard import BattleShip

class Solver:
    """
    definnes the abstract class for solvers
    """
    def __init__(self, board: BattleShip):
        self.bord_to_solve = board
        self.board_size = board.boardSize

    def solve(self):
        """
        this method should be implemented in other solvers

        :return:
        """
        return None

    def stats(self):
        """
        retuirns the stats for the game :
        1- the number of moves
        2- time it took to solve
        This method has to be implemented in each solver
        :return:
        """
        return None, None, None

    def solved_board(self):
        """
        returns the list of hits
        :return:
        """
        return self.bord_to_solve.hit_map
