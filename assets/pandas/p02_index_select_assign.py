"""
    Pandas'ta Indexing, Selecting ve Assigning kavramları, DataFrame'lerde belirli verileri seçmek, filtrelemek ve değiştirmek için kullanılan temel yöntemlerdir.

    Indexing: Pandas DataFrame'lerinde, belirli satır ve sütunlara erişmek için indexleme yöntemleri kullanılır. Bu yöntemler arasında iloc[], loc[], at[], iat[] ve .ix[] bulunur.

    Selecting: Selecting, veri setinde belirli kriterlere göre filtreleme yapmak anlamına gelir. Bu işlem için pandas DataFrame'lerinde boolean indexing, query() metodu ve filter() metodu kullanılabilir.

    Assigning: Assigning, bir DataFrame'de belirli bir sütuna veya hücreye yeni bir değer atamak için kullanılır. Bu işlem için pandas DataFrame'lerinde at[], iat[], loc[] ve iloc[] yöntemleri kullanılabilir.
"""

import pandas as pd

############################################3
# INDEXING
############################################
students = pd.DataFrame({
    'ad': ['Ali', 'Burak', 'Can', 'Deniz', 'Elif'],
    'yas': [20, 21, 19, 22, 20]
})

students.set_index("ad",inplace=True)
print(students,end="\n***********************\n")


"""
bir DataFrame'deki belli bir sütunun tüm değerlerine erişmekle ilgilidir. Örneğin, bir "students" DataFrame'iniz varsa ve "grades" sütunuyla ilgileniyorsanız, şu şekilde bir indexing kullanabilirsiniz:
"""

yas = students['yas']
print(yas,end="\n***********************\n")

"""
loc belirli bir satırın tüm sütunlarına erişmekle ilgilidir. 
Örneğin, "students" DataFrame'inizde "Ali" adlı öğrencinin tüm sütun verilerine ihtiyacınız varsa, şu şekilde bir indexing kullanabilirsiniz:
"""
ali = students.loc['Ali']
print(ali,end="\n***********************\n")


"""
bu örnek, belirli bir aralıktaki satırlara ve sütunlara erişmekle ilgilidir. 
Örneğin, "students" DataFrame'inizdeki ilk 2 satırın ve ilk 2 sütunun verilerine ihtiyacınız varsa, şu şekilde bir indexing kullanabilirsiniz:
"""

subset = students.iloc[:2, :2]
print(subset,end="\n***********************\n")


"""
bir DataFrame'deki belirli koşulları karşılayan satırlara erişmekle ilgilidir. 
Örneğin, "students" DataFrame'inizde "yas" sütununda 20'den büyük kayıtlar için
"""
students = pd.DataFrame({
    'ad': ['Ali', 'Burak', 'Can', 'Deniz', 'Elif'],
    'yas': [20, 21, 19, 22, 20],
    "cinsiyet":["E","E","E","K","K"]
})

top_students = students[students['yas'] > 20]
print(top_students)


"""
"students" DataFrame'inizde "yas" sütununda 20'den büyük kadınlar"
"""
top_female_students = students[(students['yas'] > 20) & (students['cinsiyet'] == 'F')]
print(top_female_students ,end="\n***********************\n")
############################################3
# SELECTING
############################################

students = pd.DataFrame({
    'ad': ['Ali', 'Burak', 'Can', 'Deniz', 'Elif'],
    'yas': [20, 21, 19, 22, 20],
    "cinsiyet":["E","E","E","K","K"]
})


"""
Belirli bir sütunu seçmek:
"""

print(students['ad'], end="\n******************\n")

"""
Birden fazla sütunu seçmek:
"""

result = students[['ad', 'cinsiyet']]

print(result, end="\n******************\n")


"""
belirli bir satırı seçmek
"""

result = students.loc[2]
print(result, end="\n******************\n")

"""
Belirli bir satırda ve sütunda bulunan bir değeri seçmek
"""
result = students.at[2, 'ad']
print(result, end="\n******************\n")

"""
Belirli bir koşulu sağlayan satırları seçmek:
"""
result = students.loc[students['yas'] > 20]


#######################################
# ASSIGNING
#######################################

students = pd.DataFrame({
    'ad': ['Ali', 'Burak', 'Can', 'Deniz', 'Elif'],
    'yas': [20, 21, 19, 22, 20],
    "cinsiyet":["E","E","E","K","K"]
})

copy_df = students.copy(deep=True)

"""
Tüm öğrencilerin cinsiyetini "B" olarak değiştirme:
"""
copy_df["cinsiyet"] = "B"

print(copy_df, end="\n******************\n")

"""
"Deniz" adlı öğrencinin yaşını 23'e yükseltme
"""

copy_df = students.copy(deep=True)

copy_df.loc[3, "yas"] = 23
print(copy_df, end="\n******************\n")

"""
Yaşı 20'den büyük olan öğrencilerin cinsiyetini "K" olarak güncelleme:
"""
copy_df = students.copy(deep=True)
copy_df.loc[students["yas"] > 20, "cinsiyet"] = "K"
print(copy_df, end="\n******************\n")

"""
"Can" adlı öğrencinin cinsiyetini "E" olarak değiştirme:
"""
copy_df = students.copy(deep=True)
copy_df.at[2, "cinsiyet"] = "E"
print(copy_df, end="\n******************\n")

"""
"Ali" adlı öğrencinin tüm bilgilerini değiştirme
"""
copy_df = students.copy(deep=True)
copy_df.loc[students["ad"] == "Ali"] = ["Ahmet", 23, "E"]
print(copy_df, end="\n******************\n")



