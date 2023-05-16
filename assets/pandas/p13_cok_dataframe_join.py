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

df3 = pd.DataFrame({
    'id': [2, 4, 5, 6],
    'city': ['New York', 'Chicago', 'San Francisco', 'Houston']
})


# pandas merge
df = pd.merge(df1, pd.merge(df2, df3, on='id'), on='id')
print( df )


#dataframeler üzerinden
#df = df1.merge(df2.merge(df3, on='id'), on='id')
