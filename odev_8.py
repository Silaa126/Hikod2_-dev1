import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

#Kadın erkek sayısına bakalım
print(df.head())

# Kadın-Erkek sayılarına bakalım
a = df["gender"].value_counts()
print(a)

# Kadın- erkek sayısına histogram grafiğine bakalım
b = sns.histplot(x="gender", data=df)
print(b)
# plt.show()

# race/ethnicity sütununda kaç tane farklı grup olduğuna bakalım
c = df["race/ethnicity"].value_counts() #ikinci yöntem: df["race/ethnicity"].unique()
print(c)

# Yukarıda bulduğumuzu görselleştirelim
# print(sns.barplot(x=race.index, y=race.values))
# print(plt.title("Count of students by race"))
# print(plt.xlabel("Race"))
# print(plt.ylabel("Count"))
# plt.show()

# Parental level of education sütunundaki eşsiz değerleri bulalım
d = df["parental level of education"].unique()
print(d)

# lunch sütunundaki eşsiz değerleri bulalım
e = df["lunch"].unique()
print(e)

# lunch türlerinde kaçar kişi olduğunu bulalım
f = df["lunch"].value_counts()
print(f)

#gender sütunundaki değerler için ortalama math score,
# reading score, writing score değerlerini bulalım
g = df.groupby("gender")[["math score","reading score","writing score"]].mean().reset_index()
print(g)

#race/ethnicity sütunundaki değerler için  ortalama math score,
# reading score, writing score değerlerini bulalım
t = df.groupby("race/ethnicity")[["math score","reading score","writing score"]].mean().reset_index()
print(t)


#parental level of education sütunundaki değerler için  ortalama math score,
# reading score, writing score değerlerini bulalım
x = df.groupby("parental level of education")[["math score","reading score","writing score"]].mean().reset_index()
print(x)

#lunch sütunundaki değerler için  ortalama math score,
# reading score, writing score değerlerini bulalım
o = df.groupby("lunch")[["math score","reading score","writing score"]].mean().reset_index()
print(o)

#test preparation courses sütunundaki değerler için  ortalama math score,
# reading score, writing score değerlerini bulalım
m = df.groupby("test preparation course")[["math score","reading score","writing score"]].mean().reset_index()
print(m)