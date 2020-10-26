import a1
import unittest

class TestSwapK(unittest.TestCase):
    """
    Test class for function a1.swap_k.
    Test swap_k where swap the first k items with the last k items of L.
    """

    def test_swap_k_ex1(self):
        """ Test function swap_k with:
        L = [1, 2, 3, 4, 5, 6] and k = 2        
        """

        nums = [1, 2, 3, 4, 5, 6]
        nums_expected = [5, 6, 3, 4, 1, 2]

        a1.swap_k(nums, 2)

        self.assertEqual(nums, nums_expected)

    def test_swap_k_ex2(self):
        """ Test the function swap_k with:
        L = [1, 2, 3, 4, 5, 6] and k = 0
        """        

        nums = [1, 2, 3, 4, 5, 6]
        nums_expected = [1, 2, 3, 4, 5, 6]

        a1.swap_k(nums, 0)

        self.assertEqual(nums, nums_expected)

    def test_swap_k_ex3(self):
        """ Test the function swap_k with:
        L = [6, 7, 8, 9] and k = 1
        """
        
        nums = [6, 7, 8, 9]
        nums_expected = [9, 7, 8, 6]

        a1.swap_k(nums, 1)

        self.assertEqual(nums, nums_expected)
       

if __name__ == '__main__':
    unittest.main(exit=False)
