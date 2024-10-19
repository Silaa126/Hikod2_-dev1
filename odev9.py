import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("TheLongDark_ItemList - Clothing.csv")
print(df.head(10))


a = df["Warmth Bonus (°C)"].value_counts()
print(a)

#Çıktı, sütun adlarını, sütunlarda eksik veri olup olmadığını, 
# her bir sütunun veri tipini bulduk
b = df.info()
print(b)

#coloumn isimlerini görüntüleyelim
print(df.columns)

# Her sütundaki eksik değer sayısını kontrol et
print(df.isnull().sum())  

# İleri doldurma ile eksik verileri doldur
c = df.fillna(method='ffill', inplace=True) 
print(c)

# Eksik verileri içeren satırları sil
d = df.dropna(inplace=True)  
print(d)

# Sayısal sütunlar için temel istatistikleri görüntüle
print(df.describe())  

# Histogram ile veri dağılımını göster
sns.histplot(df['Total Bonus (°C)'], bins=15)  # Total Bonus (°C) sütununa ait histogram
plt.title('The Long Dark')  # Grafiğe başlık ekle
plt.xlabel('Item Name')  # X eksenine etiket ekle
plt.ylabel('Weight (kg)')  # Y eksenine etiket ekle
plt.show()  # Grafiği göster


sns.scatterplot(data=df, x='Total Bonus (°C)', y='Weight (kg)')  # İki sayısal değişken arasındaki ilişki
plt.title('Total Bonus (°C)  ve Weight (kg) Arasındaki İlişki')
plt.xlabel('Total Bonus (°C)')
plt.ylabel('Weight (kg)')
plt.show()
