import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_k_val_zero(self):
        """
        Test k_swap() when value of k is equal to zero.
        """

        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 0)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6])

    def test_k_val_one(self):
        """
        Test k_swap() when value of k is equal to one.
        """

        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 1)
        self.assertEqual(nums, [6, 2, 3, 4, 5, 1])

    def test_k_val_between_0_and_half_length(self):
        """
        Test k_swap() when value of k is between 0 and len(L)//2 exclusive.
        """

        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 2)
        self.assertEqual(nums, [5, 6, 3, 4, 1, 2])

    def test_k_val_half_length(self):
        """
        Test k_swap() when value of k is equal to len(L)//2.
        """

        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 3)
        self.assertEqual(nums, [4, 5, 6, 1, 2, 3])


if __name__ == '__main__':
    unittest.main(exit=False)