"""
cutting_stock module with a simple CuttingStock example class.
"""
import sys
from urllib.error import HTTPError

import numpy as np
import pandas as pd


class CuttingStock:
    """
       Class for Cutting Stock representation
    """

    def __str__(self):
        return self.__class__.__name__

    def __init__(self, data_url, stock_size):
        """
          Constructor for Cutting Stock class
        """
        self.stock_size = stock_size
        try:
            self.__initial_data = pd.read_csv(data_url, names=['pieces', 'length'])
        except HTTPError:
            print('The given data URL is not valid!')
            sys.exit(1)
        self.count = 0
        for i in self.__initial_data.index:
            self.count += self.__initial_data.loc[i, 'pieces']
        self.__initial_position = np.zeros(self.count)
        counter = 0
        for i in self.__initial_data.index:
            for j in range(self.__initial_data.loc[i, 'pieces']):
                self.__initial_position[counter + j] = self.__initial_data.loc[i, 'length']
            counter += self.__initial_data.loc[i, 'pieces']
        if stock_size < np.max(self.__initial_position):
            print('there are longer pieces then stock size')
            sys.exit(1)

    def cutting_stock(self):
        """
           cutting_stock function for finding the cost
        """
        stock_number = 1
        sum_length = 0
        for piece_length in self.__initial_position:
            if sum_length + piece_length <= self.stock_size:
                sum_length += piece_length
            else:
                stock_number += 1
                sum_length = piece_length
        return stock_number
