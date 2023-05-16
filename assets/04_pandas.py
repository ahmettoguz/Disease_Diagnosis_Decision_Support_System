import pandas as pd

data = {'name': ['Ali', 'Veli', 'Ahmet', 'Mehmet'],
        'age': [24, 25, 27, 29],
        'country': ['Turkey', 'USA', 'Germany', 'Japan']}

df = pd.DataFrame(data)

# 'name' sütununu seçme
names = df[['name']]
print(names)

print("**" * 10)


data = {'name': ['Ali', 'Veli', 'Ahmet', 'Mehmet'],
        'age': [24, 25, 27, 29],
        'country': ['Turkey', 'USA', 'Germany', 'Japan']}

df = pd.DataFrame(data)

# 'name' sütununu seçme
name_country = df[['name','country']]
print(name_country)
