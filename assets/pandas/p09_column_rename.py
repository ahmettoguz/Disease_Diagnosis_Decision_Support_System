# KOLON İSMİ DEĞŞTİRME

import pandas as pd
import numpy as np

# örnek veri oluşturma
data = {'sütun1': [1, 2, np.nan, 4, 5],
        'sütun2': [6, np.nan, 8, np.nan, 10],
        'sütun3': ['a', 'b', np.nan, 'd', 'e']}

df = pd.DataFrame(data)

df_copy = df.copy()
# Tek tek kolon isimlerini değiştirmek için:
df_copy = df_copy.rename(columns={'sütun1': 'yeni_isim1', 'sütun2': 'yeni_isim2', 'sütun3': 'yeni_isim3'})

print( df_copy )

df_copy = df.copy()

#Tüm kolon isimlerinin büyük harfli hallerini kullanmak için:
df_copy.columns = map(str.upper, df_copy.columns)
print( df_copy )



df_copy = df.copy()
# Kolon isimlerinin bir kısmını değiştirmek için:
df_copy = df_copy.rename(columns=lambda x: x.replace('sütun', 'yeni_isim'))
print( df_copy )