# create unit tests for the rock, paper, scissors game
# Path: test.py 
import unittest
from app import *
from app import get_winner

class TestGame(unittest.TestCase):
    def test_rock(self):
        self.assertEqual(get_winner('R', 'R'), None)
        self.assertEqual(get_winner('R', 'P'), 'P')
        self.assertEqual(get_winner('R', 'S'), 'R')

    def test_paper(self):
        self.assertEqual(get_winner('P', 'R'), 'P')
        self.assertEqual(get_winner('P', 'P'), None)
        self.assertEqual(get_winner('P', 'S'), 'S')

    def test_scissors(self):
        self.assertEqual(get_winner('S', 'R'), 'R')
        self.assertEqual(get_winner('S', 'P'), 'S')
        self.assertEqual(get_winner('S', 'S'), None)

if __name__ == '__main__':
    unittest.main()

## The code above is a simple rock, paper, scissors game. I am trying to create a unit test for it. I am not sure how to do this. I have tried to do it myself, but I am not sure if I am doing it correctly. I am new to unit testing and I am not sure how to do it. I have tried to look up examples, but I am still confused. Can someone please show me how to do this?
    