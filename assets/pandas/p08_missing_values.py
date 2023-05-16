import pandas as pd
import numpy as np

# Örnek veri oluşturma
data = {'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, np.nan, 8],
        'C': [9, 10, 11, 12]}
df = pd.DataFrame(data)

# eksik verili df i yazdirma
print( df )

# Eksik değerleri içeren satırları kaldırma
df.dropna(inplace=True)

# Sonucu yazdırma
print(df)