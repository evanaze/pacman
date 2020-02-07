import sys

from collections import namedtuple

import numpy as np

"""
Write a module docstring here
"""

__author__ = "Evan Azevedo"

Coordinate = namedtuple("Coordinate", ['x', 'y'])

def parse_coord(position):
    position = position.split(' ')
    coord = Coordinate(int(position[0]), int(position[1]))
    return coord

class Game:
    def __init__(self, input_file):
        self.input_file = input_file
        self.read()

    def read(self):
        with open(self.input_file, "r+") as input:
            lines = input.readlines()
        self.board_dimension = parse_coord(lines[0][:-1])
        self.player = parse_coord(lines[1][:-1])
        self.movements = list(lines[2][:-1])
        self.walls = [parse_coord(wall[:-1]) for wall in lines[3:]]

    def initBoard(self):
        self.board = np.full((self.board_dimension.x + 1, self.board_dimension.y + 1), 'c')
        self.board[0] = 1
        self.board[-1] = 1
        self.board[:,0] = 1
        self.board[:,-1] = 1
        for wall in self.walls:
            self.board[wall.x, wall.y] = 1
        try:
            if self.board[self.player.x, self.player.y] == 1:
                sys.exit("Error: Invalid starting location")
            self.board[self.player.x, self.player.y] = 0
        except IndexError:
            sys.exit("Error: Invalid starting location")

    def test_move(self):
        if self.board[self.next_move.x, self.next_move.y] != 1:
            self.player = self.next_move
            if self.board[self.player.x, self.player.y] == 'c':
                self.coins_collected += 1
                self.board[self.player.x, self.player.y] = 0


    def move(self):
        if self.direction == "N":
            self.next_move = Coordinate(self.player.x, self.player.y + 1)
            self.test_move()
        if self.direction == "S":
            self.next_move = Coordinate(self.player.x, self.player.y - 1)
            self.test_move()
        if self.direction == "E":
            self.next_move = Coordinate(self.player.x + 1, self.player.y)
            self.test_move()
        if self.direction == "W":
            self.next_move = Coordinate(self.player.x - 1, self.player.y)
            self.test_move()

    def play(self):
        self.initBoard()
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

    final_pos_x, final_pos_y, coins_collected = Game(input_file).play()

    return final_pos_x, final_pos_y, coins_collected

if __name__ == "__main__":
    input_file = sys.argv[1]
    print(pacman(input_file))
