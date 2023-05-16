import pandas as pd

df1 = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['John', 'Alice', 'Bob', 'Dave', 'Eve'],
    'age': [25, 30, 35, 40, 45]
})

df2 = pd.DataFrame({
    'id': [1, 2, 3, 6, 7],
    'gender': ['M', 'F', 'M', 'F', 'M']
})


df = pd.merge(df1, df2, on='id', how='outer')

print( df )