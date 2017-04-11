import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_people_count_zero(self):
        """
        Test num_buses() with zero or no people. 
        """

        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_people_count_less_than_50(self):
        """
        Test num_buses() with zero or no people. 
        """

        actual = a1.num_buses(28)
        expected = 1
        self.assertEqual(actual, expected)

    def test_people_count_50(self):
        """
        Test num_buses() with 50 people.
        """

        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(actual, expected)

    def test_people_count_non_multiple_50(self):
        """
        Test num_buses() with number of people which is not divisible by 50.
        """

        number_of_people = 51
        actual = a1.num_buses(number_of_people)
        expected = 2
        self.assertEqual(actual, expected)

    def test_people_count_greater_than_50(self):
        """
        Test num_buses() with people more than 50.
        """

        actual = a1.num_buses(75)
        expected = 2
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)