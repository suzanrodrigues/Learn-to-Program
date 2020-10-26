import a1
import unittest

class TestStockPriceSummary(unittest.TestCase):
    """
    Test class for function a1.stock_price_summary. 
    The parameter is a list of stock price changes. Return a tuple with 2 items,
    where the first is the sum of gains in praice_changes and the second is the
    the sum of losses in price_changes.
    """

    def test_stock_price_summary_ex1(self):
        """Test the function with stock_price_summary"""         

        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_ex2(self):
        """Test stock_price_summary with new arguments"""

        actual = a1.stock_price_summary([0.05, 0.08, -0.03, -0.14, 0.1, 0.6, 0])
        expected = (0.83, -0.17)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_ex3(self):
        """Test stock_price_summary with empty list"""

        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_ex4(self):
        """Test stock_price_summary with one positive argument"""

        actual = a1.stock_price_summary([0.07])
        expected = (0.07, 0)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_ex5(self):
        """Test stock_price_summary with one negative argument"""

        actual = a1.stock_price_summary([-0.06])
        expected = (0, -0.06)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_ex6(self):
        """Test stock_price_summary with zero arguments"""

        actual = a1.stock_price_summary([0, 0])
        expected = (0, 0)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)

        
                                           
