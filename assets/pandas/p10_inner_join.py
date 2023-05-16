"""
INNER JOIN
"""

import pandas as pd

# ad ve yaş kolonlarından oluşan dataframe'i oluşturma
df1 = pd.DataFrame({
    'ad': ['Ahmet', 'Ayşe', 'Mehmet', 'Fatma'],
    'yaş': [25, 30, 35, 40]
})

# ad ve doğum_tarihi kolonlarından oluşan dataframe'i oluşturma
df2 = pd.DataFrame({
    'ad': ['Ahmet', 'Ayşe', 'Mehmet', 'Zeynep'],
    'doğum_tarihi': ['1995-01-01', '1990-02-02', '1985-03-03', '1980-04-04']
})

# INNER JOIN işlemi ile iki dataframe'i birleştirme
df = pd.merge(df1, df2, on='ad', how='inner')

print( df )

# birleştirilmiş dataframe'i yazdırma
print(df)
