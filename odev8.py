import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

print(df)

#Veri setinin ilk beş değerine ulaşırız
print(df.head())

#Veri setinin son beş değerine ulaşırız
print(df.tail())

#Veri setindeki sütunların isimlerini, boş olmayan değer sayılarını
#veri tipini gösterdik
print(df.info())

#Veri setindeki sayısal veriler üzerindeki istatiksel sonuçları döndürür
print(df.describe())

# Veri setindeki eksik değerler sayısını (NaN deerleri) buluyoruz
a = df.isnull().sum()
print(a)

# Veri setinde herhangi bir eksik değer olup olmadığını kontrol ediyoruz
# Sonuç True(eksik değer için döner) ya da False olarak dönecektir
b = df.isnull().any()
print(b)

# Sütundaki eşsiz değerleri döndürür
c = df["lunch"].unique()
print(c)

# Sütundaki her değerin kaç tane olduğunu bulalım
d = df["gender"].value_counts()
print(d)

#Veri setindeki verileri gruplayalım. (gender grubunun içinden )
e = df.groupby("gender").get_group("female")
print(e)

#Bu kodla, veri çerçevesini cinsiyete göre grupladınız ve her grup için "math score" 
#sütununun ortalama değerini hesapladınız.
f = df.groupby("gender")[["math score"]].mean().reset_index()
print(f)

#ortalama alıp küçükten büyüğe sıraladık
k = df.groupby("gender")[["math score"]].mean().reset_index().sort_values(by="math score",ascending=False)
print(k)

#veriyi görsele dökelim
group_category = df.groupby("gender")[["math score"]].mean().reset_index()

plt.figure(figsize=(18,5))
plt.bar(x = "race", height = "math score", data = df)
plt.xticks(rotation=90)
print(group_category)
plt.show

