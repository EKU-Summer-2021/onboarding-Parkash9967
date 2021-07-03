"""
read_data file
"""
import unittest


import pandas as pd

from src.read_data import read_data


class MyTestCase(unittest.TestCase):
    """
    read_data file
    """

    def test(self):
        dataframe = read_data(
            'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/CSP/CSP_360.csv')
        data = pd.DataFrame(dataframe)
        self.assertIsInstance(data, pd.DataFrame)
