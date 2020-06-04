import unittest
import game

class TestGrid(unittest.TestCase):
    def test_grid(self):
        """
        This test checks whether the grid/maze that is drawn 
        is a list of nine rows.It does this by checking the Grid
        function that draws the grid has a column length of 9
         """
        self.assertEqual(len(game.Grid()),9)

    # def run_tests():
    #     test_grid()
if __name__ == '__main__':
    unittest.main()