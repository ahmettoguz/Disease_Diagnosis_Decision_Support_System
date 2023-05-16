"""
Pandas'da kullanılan bazı veri tipleri şunlardır:

    object: En geniş veri tipidir ve çeşitli Python nesnelerini (ör. stringler, listeler, sözlükler) içerebilir.
    int64: Tam sayılar için kullanılır. Bellekte 64 bit (8 byte) alan kaplar.
    float64: Ondalık sayılar için kullanılır. Bellekte 64 bit (8 byte) alan kaplar.
    bool: Boolean değerler (True veya False) için kullanılır. Bellekte 8 bit (1 byte) alan kaplar.
    datetime64: Tarih ve saat değerleri için kullanılır. Bellekte 64 bit (8 byte) alan kaplar.
    timedelta: Zaman farkı verileri için kullanılır. Pandas bu veri tipini, iki datetime64 veri tipi arasındaki farkları hesaplamak için kullanır.
    category: Sınıflandırma değişkenleri için kullanılır.
    str: metin tipler için kullanılır
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'object': pd.Series(['a', 'b', 'c']),
    'int64': pd.Series(np.arange(3, dtype=np.int64)),
    'float64': pd.Series(np.random.randn(3)),
    'bool': pd.Series([True, False, True]),
    'datetime64': pd.date_range('2022-01-01', periods=3),
    'category': pd.Series(['cat', 'dog', 'bird']).astype('category')
})

print(df.dtypes)

print(df)

# tip donusumu
df["bool"] = df["bool"].astype(int)

print( df.dtypes)
print( df)

