import numpy as np


# python map fonksiyonuna benzer
arr = np.array([1, 2, 3, 4, 5])
squared = np.vectorize(lambda x: x**2)(arr)
print(squared)


# İki numpy dizisini eleman eleman toplayan bir vectorize fonksiyonu:
@np.vectorize
def add(x, y):
    return x + y

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = add(a, b)
print(result)  # çıktı: [5 7 9]

#Bir numpy dizisindeki her elemanın karekökünü alan bir vectorize fonksiyonu
@np.vectorize
def sqrt(x):
    return np.sqrt(x)

a = np.array([1, 4, 9, 16, 25])

result = sqrt(a)
print(result)  # çıktı: [1. 2. 3. 4. 5.]


