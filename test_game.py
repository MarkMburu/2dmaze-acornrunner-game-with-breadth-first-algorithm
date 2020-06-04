import unittest

import game

class TestGame(unittest.TestCase):
    def test_game(self):
        """
        This test run tests on the number of moves that are made by 
        the breadth first algorithm by testing the valid function in
        game.py
        """
        self.assertEqual(game.valid(game.maze,[10]),True)


# def run_tests():
#     test_game()

if __name__ == '__main__':
    unittest.main()