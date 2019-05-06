# defines the game board, it's size and ships
import numpy as np

class BattleShip:

    def __init__(self, size, title):
        self.boardSize = size
        self.title = title
        self.board = np.zeros((size, size))
        self.ships = []
        self.hit_map = np.zeros((size, size))



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
            self.board[point[0], point[1]] = len( self.ships )+1
        self.ships.append(the_ship)

        return 0

    def print_board(self):
        """
        prints the game board in a nice format
        :return:
        """
        print("\033[32m--------------------------------------------")
        print("\033[32m   |", end=' ')
        for i in range( self.boardSize ):
            print("%0.0d |"%i, end=' ')
        print("\n\033[32m--------------------------------------------")

        for i in range(self.boardSize):
            print( "|\033[32m %0.0d|" %i , end=' ' )
            for j in range(self.boardSize):
                if self.hit_map[i,j] ==1 and self.board[i,j]!=0:
                    print("\033[31m%0.0d \033[32m|" % self.board[i][j] , end=' ')
                elif self.hit_map[i,j] !=1 and self.board[i,j]!=0:
                    print("\033[34m%0.0d \033[32m|" % self.board[i][j], end=' ')
                elif self.hit_map[i,j] ==1 and self.board[i,j]==0:
                    print("\033[37mX \033[32m|", end=' ')
                else :
                    print("  \033[32m|", end=" ")
            print("\n\033[32m--------------------------------------------")
        print("\033[0m")


    def make_move(self, location):
        end_of_game = False
        was_hit = False
        ship_sank = False

        self.hit_map[location[0], location[1]] = 1

        if np.sum(self.hit_map * self.board ) ==np.sum( self.board):
            end_of_game = True
        if self.board[location[0], location[1]] != 0:
            was_hit = True
            the_ship = np.where( self.board ==self.board[location[0], location[1]])

            ship_sank=True
            for x in range(len(the_ship[0])):
                if self.hit_map[the_ship[0][x],the_ship[1][x]] == 0:
                    ship_sank = False
                    break


        return end_of_game, was_hit,ship_sank
class Ship:
    """
    Defines ship objects
    """
    def __init__(self, start, length,orientation, title=None ):
        """

        :param start:
        :param length:
        :param orientation:
        :param title:
        """
        self.start = start
        self.length = length
        self.title = title
        self.orientation = orientation

    def get_points(self):
        """
        returns the set of point in which the ship is represented
        :return: list of points where ship is
        """
        points = []
        if self.orientation == 'h':
            for count in range(self.length):
                points.append([self.start[0], self.start[1]+count])
        elif self.orientation == 'v':
            for count in range(self.length):
                points.append([self.start[0]+count, self.start[1]])

        return points
