import pandas as pd

df1 = pd.DataFrame({
    'ad': ['Ahmet', 'Ayşe', 'Mehmet', 'Fatma'],
    'yaş': [25, 30, 35, 40]
})

df2 = pd.DataFrame({
    'ad': ['Ahmet', 'Ayşe', 'Mehmet', 'Zeynep'],
    'doğum_tarihi': ['1995-01-01', '1990-02-02', '1985-03-03', '1980-04-04']
})

# left ve left outer join
df = pd.merge(df1, df2, on='ad', how='left')

print( df )