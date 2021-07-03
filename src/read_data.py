"""
read_data file
"""
import pandas as pd


def read_data(path):
    """
    reading csv data
    """
    dframe = pd.read_csv(path)
    return dframe
