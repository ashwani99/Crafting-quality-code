import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_empty_list(self):
        """
        Test stock_price_summary() with empty price_change list.
        """
        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_only_price_gain(self):
        """
        Test stock_price_summary() with price_change list having only price gain data.
        """

        actual = a1.stock_price_summary([0.05])
        expected = (0.05, 0)
        self.assertEqual(actual, expected)

    def test_only_price_loss(self):
        """
        Test stock_price_summary() with price_change list having only price loss data.
        """

        actual = a1.stock_price_summary([-0.02])
        expected = (0, -0.02)
        self.assertEqual(actual, expected)

    def test_mix_price_change(self):
        """
        Test stock_price_summary() with price_change list having mix of price gain and loss.
        """

        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
