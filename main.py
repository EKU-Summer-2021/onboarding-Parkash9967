import numpy as np
from src import Polynomial
from src.read_data import read_data
if __name__ == '__main__':
    coeffs = np.array([1,0,0])
    polynom = Polynomial(coeffs)
    print(polynom.evaluate(3))
    print(polynom.roots())

print(read_data('https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/CSP/CSP_360.csv'))