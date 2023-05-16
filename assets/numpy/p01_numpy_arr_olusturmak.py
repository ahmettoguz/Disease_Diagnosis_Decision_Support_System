
import numpy as np


arr = np.array([1,2,3,4])
print( arr )

#Sıfırlardan oluşan 2x3 boyutlu bir numpy array:
zeros_array = np.zeros((2, 3))
print(zeros_array)


# Birlerden oluşan 3x3 boyutlu bir numpy array:
ones_array = np.ones((3, 3))
print(ones_array)


#Belirli bir aralıktaki sayılardan oluşan numpy array:
range_array = np.arange(10)
print(range_array)


# Belirli bir aralıktaki sayılardan oluşan 3x3 boyutlu bir numpy array:
range_array_2d = np.arange(9).reshape((3,3))
print(range_array_2d)


# Birim matris numpy array:
identity_matrix = np.eye(3)
print(identity_matrix)


# Rastgele sayılardan oluşan 2x3 boyutlu bir numpy array
random_array = np.random.rand(2, 3)
print(random_array)

# Belirli bir aralıktaki sayılardan oluşan, özel bir adım değeriyle numpy array:
step_array = np.arange(0, 10, 2)
print(step_array)


# Belirli bir aralıktaki sayıların eşit aralıklarla dağıtıldığı numpy array:
linspace_array = np.linspace(0, 10, 5)
print(linspace_array)