"""
Summary ve Maps

"""

import pandas as pd

df = pd.DataFrame({
    'ad': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma', 'Ali', 'Veli', 'Hakan', 'Ece', 'Ece', 'Kemal'],
    'yas': [25, 19, 32, 22, 20, 23, 29, 31, 22, 26],
    'cinsiyet': ['E', 'E', 'K', 'K', 'E', 'E', 'E', 'K', 'K', 'E']
})



#1. Veri setinin boyutunu öğrenmek: `df.shape`
print( df.shape )

#2. Veri setindeki sütunların isimlerini öğrenmek: `df.columns`
print( df.columns )

#3. Veri setindeki sütunların veri tiplerini öğrenmek
print( df.dtypes )

#4. Veri setindeki sayısal sütunların temel istatistiksel özetlerini görmek: `df.describe()`
print( df.describe() )

#Sütunlar hakkında bilgi almak için:

df['ad'].value_counts()# Bir sütundaki her bir benzersiz değer için kaç adet olduğunu gösterir.


df['ad'].unique() #Bir sütundaki benzersiz değerleri gösterir.
df['ad'].nunique() #Bir sütundaki benzersiz değerlerin sayısını verir.
df['yas'].min() # diger df['sütun_adı'].max(): Bir sütundaki minimum veya maksimum değeri verir.
df['yas'].mean() # diger df['sütun_adı'].median(): Bir sütundaki ortalama veya medyan değeri verir.
df['yas'].std() # Bir sütundaki standart sapmayı verir.

####################################################
# MAPS
####################################################

import pandas as pd

df = pd.DataFrame({
    'ad': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma', 'Ali', 'Veli', 'Hakan', 'Ece', 'Nur', 'Kemal'],
    'yas': [25, 19, 32, 27, 20, 23, 29, 31, 22, 26],
    'cinsiyet': ['E', 'E', 'K', 'K', 'E', 'E', 'E', 'K', 'K', 'E']
})

orj = df.copy(deep=True)


#"yas" sütunundaki her yaş değerinin 2 katını alarak yeni bir sütun oluşturma:
df = orj
df['yas_2kat'] = df['yas'].map(lambda x: x*2)


#"ad" sütununda yer alan isimleri büyük harfe çevirme:
df = orj
df['ad_buyuk'] = df['ad'].map(lambda x: x.upper())

#"cinsiyet" sütununda yer alan "E" değerlerini "Erkek", "K" değerlerini ise "Kadın" olarak değiştirme:
df = orj
df['cinsiyet'] = df['cinsiyet'].map({'E': 'Erkek', 'K': 'Kadın'})

# "yas" sütunundaki yaş değerlerini 20 ile 30 arasında kalanlar "Genç", 30 ile 40 arasında kalanlar "Orta yaşlı", 40'tan büyük olanlar ise "Yaşlı" olarak etiketleme:
df['yas_grup'] = df['yas'].map(lambda x: 'Genç' if x < 30 else ('Orta yaşlı' if x < 40 else 'Yaşlı'))
