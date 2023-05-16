import numpy as np

# dizi oluşturma
a = np.array([1, 2, 3])
print(a)

# matris oluşturma

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

# belirli aralıkta dizi oluşturma
c = np.arange(0, 10, 2)
print(c)

# zero ve ones matrisleri oluşturma
d = np.zeros((2, 3))
e = np.ones((2, 3))

print(d)
print(e)

# bir matrisin transposunu alma

f = np.array([[1, 2], [3, 4]])
g = np.transpose(f)

print(f)
print(g)

