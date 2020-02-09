import sys

from collections import namedtuple

import numpy as np

"""Pacman player developed in Python.

This module includes the solution to the C3.ai FDSE Technical Challenge.
This code has been written and tested in Python 3.7.6.

For manual testing on a test file 'test.txt', run the script from the command line as:
    $ python3 submission.py ./test.txt

Third party libraries used in this script are Numpy and collections.

The code includes a helper method parse_coord() which uses the namedtuple method from collections to simplify
locating points on the board.
All other aspects of creating and playing the game are in the Game class, including reading the file, creating the board, and executing the moves.
This Game object is created within the overall pacman method and is executed by the objects main method, play().

Error handling is done by exiting the parent function, and returning (-1, -1, 0).
"""

__author__ = "Evan Azevedo"

Coordinate = namedtuple("Coordinate", ['x', 'y'])

def parse_coord(position):
    position = position.split(' ')
    coord = Coordinate(int(position[0]), int(position[1]))
    return coord

class Game:
    """This class creates the pacman game, and is executed to play with the play() method."""
    def __init__(self, input_file):
        self.input_file = input_file

    def read(self):
        """Reads in the input text file."""
        with open(self.input_file, "r+") as input:
            lines = input.readlines()
        self.board_dimension = parse_coord(lines[0][:-1])
        self.player = parse_coord(lines[1][:-1])
        self.movements = list(lines[2][:-1])
        self.walls = [parse_coord(wall[:-1]) for wall in lines[3:]]

    def init_board(self):
        """Creates the board.

        This method is the main source for error handling.
        The three errors we addressed were invalid starting locations, invalid board sizes, or invalid walls.
        The board is initialized surrounded by walls.
        Walls are symbolized by an asterix (*), coins a lower case C (c), and empty spaces by (0).
        """
        self.board = np.full((self.board_dimension.x, self.board_dimension.y), 'c')
        for wall in self.walls:
            # error handling for bad walls outside of the board
            try:
                self.board[wall.x, wall.y] = '*'
            except Exception:
                raise
        try:
            if self.board[self.player.x, self.player.y] == '*':
                # erorr handling for bad player initialization, on a wall or off the board
                raise Exception
            self.board[self.player.x, self.player.y] = 0
        except Exception:
            raise

    def test_move(self):
        """Tests whether the next move is valid"""
        self.valid_move = False
        if self.next_move.x >= self.board_dimension.x or self.next_move.y >= self.board_dimension.y:
            # tests if we are trying to move outside of the board
            return
        # tests if trying to move towards a wall
        if self.board[self.next_move.x, self.next_move.y] != '*':
            self.valid_move = True

    def move(self):
        """Parses the input move command, executes the test_move() method, then moves the player."""
        if self.direction == "N":
            self.next_move = Coordinate(self.player.x, self.player.y + 1)
        if self.direction == "S":
            self.next_move = Coordinate(self.player.x, self.player.y - 1)
        if self.direction == "E":
            self.next_move = Coordinate(self.player.x + 1, self.player.y)
        if self.direction == "W":
            self.next_move = Coordinate(self.player.x - 1, self.player.y)
        self.test_move() # make sure the next move is valid
        if self.valid_move:
            # moves the player if the test_move is positive, and collects a coin if possible
            self.player = self.next_move
            if self.board[self.player.x, self.player.y] == 'c':
                self.coins_collected += 1
                self.board[self.player.x, self.player.y] = 0

    def print_move(self):
        """Prints the move for debugging purposes."""
        print(self.player, self.direction, self.coins_collected)

    def play(self):
        """The main function for the Game class.

        Initializes the board and iterates through movements, finally returning the result of the playthrough.
        """
        self.read()
        self.init_board()
        self.coins_collected = 0
        while self.movements:
            self.direction = self.movements.pop(0)
            self.move()
        return self.player.x, self.player.y, self.coins_collected


def pacman(input_file):
    """ Use this function to format your input/output arguments. Be sure not to change the order of the output arguments.
    Remember that code organization is very important to us, so we encourage the use of helper fuctions and classes as you see fit.

    Input:
        1. input_file (String) = contains the name of a text file you need to read that is in the same directory, includes the ".txt" extension
           (ie. "input.txt")
    Outputs:
        1. final_pos_x (int) = final x location of Pacman
        2. final_pos_y (int) = final y location of Pacman
        3. coins_collected (int) = the number of coins that have been collected by Pacman across all movements
    """
    try:
        final_pos_x, final_pos_y, coins_collected = Game(input_file).play()
    except Exception:
        return (-1, -1, 0)

    return final_pos_x, final_pos_y, coins_collected

if __name__ == "__main__":
    input_file = sys.argv[1]
    print(pacman(input_file))
