# 1 boyutlu bir numpy array'in ilk 5 elemanını seçme:

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sliced_arr = arr[:5]
print(sliced_arr) # [1 2 3 4 5]


# 2 boyutlu bir numpy array'in ilk 2 satırını seçme:

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
sliced_arr = arr[:2, :]
print(sliced_arr)
# [[1 2 3]
#  [4 5 6]]


# 2 boyutlu bir numpy array'in ilk sütununu seçme:
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
sliced_arr = arr[:, 0]
print(sliced_arr) # [ 1  4  7 10]

# 2 boyutlu bir numpy array'in 2. ve 3. sütununu seçme:
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
sliced_arr = arr[:, 1:3]
print(sliced_arr)
# [[ 2  3]
#  [ 5  6]
#  [ 8  9]
#  [11 12]]


# 3 boyutlu bir numpy array'in ilk 2 katmanını seçme:
arr = np.array(    [[[1, 2], [3, 4]],
                    [[5, 6], [7, 8]]])
sliced_arr = arr[:2, :, :]
print(sliced_arr)
# [[[1 2]
#   [3 4]]

#  [[5 6]
#   [7 8]]]


# 3 boyutlu bir numpy array'in son katmanını seçme:
arr = np.array([[[1, 2], [3, 4]],
                [[5, 6], [7, 8]]   ])
sliced_arr = arr[:, :, -1]
print(sliced_arr)
# [[2 4]
#  [6 8]]

# 1 boyutlu bir numpy array'in 2. elemandan sonraki elemanlarını seçme:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sliced_arr = arr[2:]
print(sliced_arr) # [3 4 5 6 7 8 9 10]

# 1 boyutlu bir numpy array'in son 3 elemanını seçme:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sliced_arr = arr[-3:]
print(sliced_arr) # [ 8  9 10]