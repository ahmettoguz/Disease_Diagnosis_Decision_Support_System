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

#
print( df.groupby('yaş')['doğum yeri'].nunique() )


#Her doğum yerindeki erkek ve kadın sayısı:
print( df.groupby(['doğum yeri', 'cinsiyet']).size())


#Doğum yeri ve cinsiyete göre yaşın en büyüğü:
print( df.groupby(['doğum yeri', 'cinsiyet'])['yaş'].max())


#Doğum yeri ve cinsiyete göre yaşın en küçüğü:
print( df.groupby(['doğum yeri', 'cinsiyet'])['yaş'].min())


#Doğum yeri ve cinsiyete göre yaş ortalaması:
print( df.groupby(['doğum yeri', 'cinsiyet'])['yaş'].mean())
