# defines the game board, it's size and ships
import numpy as np

class BattleShip:

    def __init__(self, size, title):
        self.boardSize = size
        self.title = title
        self.board = np.zeros((size, size))
        self.ships = []



    def add_ship(self, the_ship):
        """
        Adds a ship to the board after validating it
        :param the_ship: ship object to be placed on the board
        :return: 0 is ship is placed on the board, 1 for out of bound ship and 2 for ship croosing another ship
        """
        if the_ship.start[0] >= self.boardSize or the_ship.start[1] >= self.boardSize:
            return 1  # out of bounds!

        # validate ship to bounderies and other ships

        for point in the_ship.get_points():
            if point[0] >= self.boardSize or point[1] >= self.boardSize:
                return 1  # ship out of bound
            if self.board[point[0], point[1]] != 0:
                return 2  # ship crossing each other

        # place the ship on the board
        for point in the_ship.get_points():
            self.board[point[0], point[1]] = 1
        self.ships.append(the_ship)

        return 0

    def print_board(self):
        print(self.board)

class Ship:
    def __init__(self, start, length,orientation, title=None ):
        self.start = start
        self.length = length
        self.title = title
        self.orientation = orientation

    def get_points(self):
        points = []
        if self.orientation == 'h':
            for count in range(self.length):
                points.append([self.start[0], self.start[1]+count])
        elif self.orientation == 'v':
            for count in range(self.length):
                points.append([self.start[0]+count, self.start[1]])

        return points
