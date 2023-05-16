import pandas as pd

data = {'name': ['Ali', 'Veli', 'Ahmet', 'Mehmet'],
        'age': [24, 25, 27, 29],
        'country': ['Turkey', 'USA', 'Germany', 'Japan']}

df = pd.DataFrame(data)

# 'age' sütununda 25 yaşından büyük olanları filtreleme
result = df.query('age > 25')

print(result)