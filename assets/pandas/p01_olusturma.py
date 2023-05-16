import pandas as pd
# pandas kütüphanesi ile farklı şekillerde dataframe'ler oluşturabilirsiniz

#Liste ile oluşturma:

my_list = [1, 2, 3, 4, 5]
df = pd.DataFrame(my_list, columns=['Column1'])


# Numpy Array ile oluşturma:
import pandas as pd
import numpy as np
my_array = np.array([[1, 2, 3], [4, 5, 6]])
df = pd.DataFrame(my_array, columns=['Column1', 'Column2', 'Column3'])


# Sözlük ile oluşturma:
my_dict = {'Column1': [1, 2, 3, 4, 5], 'Column2': ['a', 'b', 'c', 'd', 'e']}
df = pd.DataFrame(my_dict)


# Dosya okuyarak oluşturma

df = pd.read_csv('my_data.csv')


# Veritabanı sorgusu sonucu oluşturma
# SQLite hafif bir ilişkisel veri tabanıdır. Sunucu içermez doğrudan dosya üzerinde işlem yapar.
import sqlite3
conn = sqlite3.connect('my_db.db')
df = pd.read_sql_query('SELECT * FROM my_table', conn)


