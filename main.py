"""
   main class
"""
from src.cutting_stock import CuttingStock

print('Cutting Stock Problem solution ')
ct_stock = CuttingStock('https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/'
                             'main/Intelligent%20System%20Data/CSP/CSP_360.csv', 60)


print(ct_stock.cutting_stock())
