"""
Unit tests for pacman.py
Last Modified: April 29, 2019
"""

import os
import sys
import time
import unittest
from pacman import pacman

class AllTests(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(pacman("generic.txt"), (6, 1, 27))

    def test_edge(self):
        self.assertEqual(pacman("edge.txt"), (-1, -1, 0))

    def test_runtime(self):
        self.assertEqual(pacman("runtime.txt"), (2142, 147, 148))

    def test_invalid_wall(self):
        self.assertEqual(pacman("invalid_wall.txt"), (-1, -1, 0))

    def test_invalid_board(self):
        self.assertEqual(pacman("invalid_board.txt"), (-1, -1, 0))

    def test_small(self):
        self.assertEqual(pacman("small.txt"), (1, 4, 7))

    def test_uneven(self):
        self.assertEqual(pacman("uneven.txt"), (0, 2, 10))

if __name__ == '__main__':
    for testClass in [AllTests]:
        print('\n\nTest Class: {}\n'.format(testClass.__name__))
        suite = unittest.TestLoader().loadTestsFromTestCase(testClass)
        result = unittest.TextTestRunner(verbosity=0).run(suite)
