import unittest
import game 

class TestParser(unittest.TestCase):
    def test_parse(self):
        """
        This test tests the grid_parser function in game.py to make sure 
        that the maze/grid is properly rendered
        """
         self.assertEqual(game.grid_parser(game.maze),None)


# def run_tests():
#     test_parse()

if __name__ == '__main__':
    unittest.main()