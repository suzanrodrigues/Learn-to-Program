import a1
import unittest

class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses.
    Return de number of buses requires accoring the number of people.
    Each bus can hold 50 people.
    """

    def test_num_buses_example1(self):
        """Test num_buses with the argument 20"""

        actual = a1.num_buses(20)
        expected = 1
        self.assertEqual(expected, actual)

    def test_num_buses_example2(self):
        """Test num_buses with the argument 50"""

        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(expected, actual)

    def test_num_buses_example3(self):
        """Test num_buses with the argument 101"""

        actual = a1.num_buses(101)
        expected = 3
        self.assertEqual(expected, actual)

    def test_num_buses_example4(self):
        """Test num_buses with the argument 0"""

        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_num_buses_example5(self):
        """Test num_buses with the argument 200"""

        actual = a1.num_buses(200)
        expected = 4
        self.assertEqual(expected, actual)

        
if __name__ == '__main__':
    unittest.main(exit=False)
        
            

    
