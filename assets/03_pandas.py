"""

kısa tanım :) in memory excel. Dataframe üzerinde  işlem yapmak üzerine kurguludur.
pip install pandas
conda install pandas
"""

import pandas as pd
import numpy as np

# Pandas DataFrame oluşturma, verileri doğrudan sözlükten alarak:
data = {'name': ['Ali', 'Veli', 'Ahmet', 'Mehmet'],
        'age': [24, 25, 27, 29],
        'country': ['Turkey', 'USA', 'Germany', 'Japan']}

df = pd.DataFrame(data)
print(df)

# Pandas DataFrame oluşturma, verileri listelerden oluşan sözlüklerden alarak:

data = np.array([['Ali', 24, 'Turkey'],
                 ['Veli', 25, 'USA'],
                 ['Ahmet', 27, 'Germany'],
                 ['Mehmet', 29, 'Japan']])

df = pd.DataFrame(data, columns=['name', 'age', 'country'])
print(df)

data = [{'name': 'Ali', 'age': 24, 'country': 'Turkey'},
        {'name': 'Veli', 'age': 25, 'country': 'USA'},
        {'name': 'Ahmet', 'age': 27, 'country': 'Germany'},
        {'name': 'Mehmet', 'age': 29, 'country': 'Japan'}]

df = pd.DataFrame(data)
print(df)

# Pandas DataFrame oluşturma, verileri Numpy dizilerinden alarak:

