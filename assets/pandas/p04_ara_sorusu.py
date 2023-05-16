import numpy as np
import pandas as pd

# Örnek veri oluşturma
d_yeri = np.random.choice(['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Adana'], size=30)
ad = np.random.choice(['Ali', 'Ayşe', 'Ahmet', 'Mehmet', 'Fatma', 'Mustafa'], size=30)
yas = np.random.randint(18, 40, size=30)
cinsiyet = np.random.choice(['E', 'K'], size=30)

# DataFrame oluşturma
df = pd.DataFrame({
    'doğum yeri': d_yeri,
    'ad': ad,
    'yaş': yas,
    'cinsiyet': cinsiyet
})

# DataFrame'i ekrana yazdırma
print(df)

"""
Veri setinde kaç satır var?
Veri setinde kaç sütun var?
Veri setindeki sütunların isimleri nelerdir?
Veri setindeki 'doğum yeri' sütununda kaç farklı değer var?
Veri setindeki 'doğum yeri' sütunundaki değerler nelerdir?
Veri setindeki 'yaş' sütununun ortalama değeri nedir?
Veri setindeki 'yaş' sütununun standart sapması nedir?
Veri setindeki 'ad' sütununda en sık geçen isim nedir?
Veri setindeki 'cinsiyet' sütununda kaç erkek, kaç kadın var?
Veri setindeki en yaşlı kişi kimdir?
Veri setindeki en genç kişi kimdir?
Veri setindeki en yaşlı kadın kimdir?
Veri setindeki en yaşlı erkek kimdir?
Veri setindeki en genç kadın kimdir?
Veri setindeki en genç erkek kimdir?
Veri setindeki 'doğum yeri' sütunundaki her bir farklı değerin sayısı nedir?
Veri setindeki 'doğum yeri' sütunundaki her bir farklı değer kaç kez geçiyor?
Veri setindeki 'ad' sütunundaki her bir farklı ismin sayısı nedir?
Veri setindeki 'ad' sütunundaki her bir farklı isim kaç kez geçiyor?
Veri setindeki 'cinsiyet' sütunundaki her bir farklı değerin sayısı nedir?
Veri setindeki 'cinsiyet' sütunundaki her bir farklı değer kaç kez geçiyor?
Veri setindeki 'yaş' sütununda kaç tane 25 yaşında kişi var?
Veri setindeki 'yaş' sütununda kaç tane 30 yaşında kadın var?
Veri setindeki 'ad' sütunundaki her bir ismin ilk harfi nedir?
Veri setindeki 'ad' sütunundaki her bir isim kaç harfli?
Veri setindeki her bir kişinin adını büyük harflere çevirme nasıl yapılır?
Veri setindeki her bir kişinin adını küçük harflere çevirme nasıl yapılır?
Veri setindeki 'ad' sütununda yer alan isimleri alfabetik olarak sıralama nasıl yapılır?
Veri setindeki 'doğum yeri' sütunundaki 'İstanbul' değerlerini 'İSTANBUL' şeklinde büyük harflerle değiştirme nasıl yapılır?

"""