# 1- Sayılardan oluşan bir boyutlu array oluşturulur. Arrayi oluştururken sayıların veri tipini 
# integer olarak belirtilir. Oluşturulan arrayin boyut, eleman sayısı bilgilerine bakılır. 
import numpy as np

# arr = np.array([3,5,8,9,1,6])

# print(len(arr))
# print(arr.ndim)



# 2- İki ve üç boyutlu arrayler oluşturulur. Bu arraylerin boyut, eleman sayısı, satır, 
# sütun bilgilerine ulaşılır. Arrayler üzerinde indexleme ve dilimleme(slicing) işlemi yapılır. 


# NumPy array'leri olarak tanımlama
matrix_one = np.array([[1, 5, 8], [9, 3, 7]])
matrix_two = np.array([
    [[9, 8], [7, 6], [5, 4]],  
    [[3, 2], [1, 0], [9, 8]]  
])

# Array'lerin boyutlarına (shape) bakma
print("matrix_one Array'in boyutu (shape):", matrix_one.shape)
print("matrix_two Array'in boyutu (shape):", matrix_two.shape)

# Boyut sayısı (kaç boyutlu)
print("3D Array'in boyut sayısı (ndim):", matrix_one.ndim)
print("3D Array'in boyut sayısı (ndim):", matrix_two.ndim)


# Eleman sayısı (size)
print("3D Array'in eleman sayısı (size):", matrix_one.size)
print("3D Array'in eleman sayısı (size):", matrix_two.size)

# Katman sayısı (ilk boyut), satır sayısı ve sütun sayısı
print("Matrix_one katman sayısı:", matrix_one.shape[0])
print("Matrix_one satır sayısı:", matrix_one.shape[1])


print("Matrix_two katman sayısı:", matrix_two.shape[0])
print("Matrix_two satır sayısı:", matrix_two.shape[1])
print("Matrix_two sütun sayısı:",matrix_two.shape[2])

# İki boyutlu array'den bir elemana erişim (örneğin 1)
print("İki boyutlu array'deki 1 sayısı:", matrix_one[1, 1])

# Üç boyutlu array'den bir elemana erişim (örneğin 5)
print("Üç boyutlu array'deki 5 sayısı:", matrix_two[0, 2, 0])


# matrix_one için dilimleme
first_row = matrix_one[0]
print("matrix_one'un ilk satırı:", first_row)

first_two_columns = matrix_one[:, :2]
print("matrix_one'un ilk iki sütunu:\n", first_two_columns)

# matrix_two için dilimleme
first_layer = matrix_two[0]
print("matrix_two'nun ilk katmanı:\n", first_layer)

second_layer_row = matrix_two[1, 1]
print("matrix_two'nun ikinci katmanındaki 1. satır:\n", second_layer_row)

second_column = matrix_two[:, :, 1]
print("matrix_two'nun tüm katmanlardan 1. sütunu:\n", second_column)


# 3- Numpy fonksiyonu kullanarak bir, iki ve üç boyutlu arrayler oluşturulur. 
# Arrayler üzerinde indexleme ve dilimleme(slicing) işlemi yapılır 

# 1. Bir boyutlu array
array_1d = np.array([10, 20, 30, 40, 50])
print("Bir boyutlu array:\n", array_1d)

# 2. İki boyutlu array
array_2d = np.array([[1, 2, 3], 
                     [4, 5, 6]])
print("İki boyutlu array:\n", array_2d)

# 3. Üç boyutlu array
array_3d = np.array([[[1, 2], [3, 4]], 
                      [[5, 6], [7, 8]]])
print("Üç boyutlu array:\n", array_3d)

# 4. Bir boyutlu array'den belirli bir elemanı alma
element_1d = array_1d[2]  # 3. eleman
print("Bir boyutlu array'in 3. elemanı:", element_1d)

# 5. İki boyutlu array'den 1. satır
first_row = array_2d[0]
print("İki boyutlu array'in 1. satırı:", first_row)

# 6. İki boyutlu array'den 2. sütun
second_column = array_2d[:, 1]
print("İki boyutlu array'in 2. sütunu:", second_column)

# 7. İki boyutlu array'den 1. satır ve 2. sütundaki elemanı alma
element_2d = array_2d[0, 1]  # 1. satır, 2. sütun
print("İki boyutlu array'in 1. satır ve 2. sütunundaki eleman:", element_2d)

# 8. Üç boyutlu array'den 1. katman
first_layer = array_3d[0]
print("Üç boyutlu array'in 1. katmanı:\n", first_layer)

# 9. Üç boyutlu array'den 2. katmandaki 1. satır ve 2. sütun
element_3d = array_3d[1, 0, 1]  # 2. katman, 1. satır, 2. sütun
print("Üç boyutlu array'in 2. katmanındaki 1. satır ve 2. sütundaki eleman:", element_3d)



# 4-Sıfırlardan oluşan ve birlerden oluşan iki tane iki boyutlu array oluşturulur.
# Bu arrayler satır ve sütun bazında birleştirilir.

# 1. Sıfırlardan oluşan iki boyutlu array (2 satır, 3 sütun)
zeros_array = np.zeros((2, 3))
print("Sıfırlardan oluşan iki boyutlu array:\n", zeros_array)

# 2. Birlerden oluşan iki boyutlu array (2 satır, 3 sütun)
ones_array = np.ones((2, 3))
print("Birlerden oluşan iki boyutlu array:\n", ones_array)

# 3. Satır bazında birleştirme
row_concatenated = np.vstack((zeros_array, ones_array))
print("Satır bazında birleştirilmiş array:\n", row_concatenated)

# 4. Sütun bazında birleştirme
column_concatenated = np.hstack((zeros_array, ones_array))
print("Sütun bazında birleştirilmiş array:\n", column_concatenated)

