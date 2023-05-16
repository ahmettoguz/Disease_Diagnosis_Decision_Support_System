import numpy as np

# numpy.array(): Belirtilen liste veya demetleri numpy dizisine dönüştürür.

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array)


# numpy.zeros(): Belirtilen boyutta bir dizi oluşturur ve tüm elemanları sıfıra eşitler.

my_array = np.zeros((3, 4))
print(my_array)


# numpy.ones(): Belirtilen boyutta bir dizi oluşturur ve tüm elemanları bir yapar.

my_array = np.ones((2, 5))
print(my_array)


# numpy.linspace(): Belirli bir aralıkta belirtilen sayıda eşit aralıklı değerler oluşturur.

my_array = np.linspace(0, 10, num=5)
print(my_array)


#numpy.arange(): Belirli bir aralıkta belirtilen adımlarla değerler oluşturur.

my_array = np.arange(0, 10, step=2)
print(my_array)

# numpy.random.rand(): Belirtilen boyutta rastgele sayılardan oluşan bir dizi oluşturur.

my_array = np.random.rand(2, 3)
print(my_array)


# numpy.reshape(): Dizinin boyutlarını değiştirir.

my_array = np.array([[1, 2, 3], [4, 5, 6]])
new_array = np.reshape(my_array, (3, 2))
print(new_array)


# numpy.transpose(): Dizinin transpozunu alır.

my_array = np.array([[1, 2, 3], [4, 5, 6]])
new_array = np.transpose(my_array)
print(new_array)

# numpy.max(): Dizideki en büyük değeri döndürür.

my_array = np.array([5, 10, 15, 20, 25])
max_value = np.max(my_array)
print(max_value)

# numpy.mean(): Dizideki elemanların ortalamasını döndürür.

my_array = np.array([1, 2, 3, 4, 5])
mean_value = np.mean(my_array)
print(mean_value)



