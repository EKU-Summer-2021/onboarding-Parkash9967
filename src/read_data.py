import pandas as pd


def read_data():
    df = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/CSP/CSP_360.csv')
    print(df.describe())


read_data()


def read_data1():
    df = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/CSP/CSP_53000.csv')
    print(df.describe())


read_data1()


def read_data2():
    df = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/CSP/CSP_6200.csv.csv')
    print(df.describe())


read_data2()
