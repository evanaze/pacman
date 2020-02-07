import sys

"""
Write a module docstring here
"""

__author__ = "Evan Azevedo"

def read(input_file):
    with open(input_file, "r+") as input:
        lines = input.readlines()
    board_dimension = lines[0][:-1]
    initial_position = lines[1][:-1]
    movements = lines[2][:-1]
    walls = [wall[:-1] for wall in lines[3:]]
    return board_dimension, initial_position, movements, walls

def move(movement):
    return 0

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

    # return final_pos_x, final_pos_y, coins_collected

if __name__ == "__main__":
    input_file = sys.argv[1]
    print(read(input_file))
    #pacman(input_file)
