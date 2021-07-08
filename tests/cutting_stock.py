"""
 module of  unit test of cutting_stock
"""

import unittest
from src.cutting_stock import CuttingStock


class MyTestCase(unittest.TestCase):
    """
     class of  unit test of cutting_stock
    """

    def setUp(self):
        """
            function for getting the data
        """
        self.csp = CuttingStock('https://raw.githubusercontent.com/'
                                'EKU-Summer-2021/intelligent_system_data/'
                                'main/Intelligent%20System%20Data/CSP/CSP_360.csv', 60)

    def test(self):
        """
            function for testing the actual and expected values
        """
        # given
        expected_stock_size = 60
        expected_piece_count = 9
        # when
        actual_stock_size = self.csp.stock_size
        actual_piece_count = self.csp.count

        # then
        self.assertEqual(expected_stock_size, actual_stock_size)
        self.assertEqual(expected_piece_count, actual_piece_count)
