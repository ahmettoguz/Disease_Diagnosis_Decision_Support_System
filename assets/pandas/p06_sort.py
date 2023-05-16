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


# Yaşa göre sıralama:
print(  df.sort_values(by='yaş') )


#Doğum yeri alfabetik sıralama:
print(  df.sort_values(by='doğum yeri') )


#Ad ve yaşa göre sıralama:
print(  df.sort_values(by=['ad', 'yaş']) )

#Cinsiyete göre ters sıralama
print(  df.sort_values(by='cinsiyet', ascending=False) )

