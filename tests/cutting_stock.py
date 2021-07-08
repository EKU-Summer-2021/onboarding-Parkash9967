"""
 module of  unit test of cutting_stock
"""

import unittest
from src.cutting_stock import CuttingStock


class MyTestCase(unittest.TestCase):
    """
     class of  unit test of cutting_stock
    """

    def test(self):
        """
            function for testing the actual and expected values
        """
        csp = CuttingStock('https://raw.githubusercontent.com/'
                                'EKU-Summer-2021/intelligent_system_data/'
                                'main/Intelligent%20System%20Data/CSP/CSP_360.csv', 60)
        actual = csp.cutting_stock()
        expected = 9
        self.assertEqual(actual, expected)
