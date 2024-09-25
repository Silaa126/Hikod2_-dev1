# ödev1-Aşağıdaki işlemleri indexing ve slicing kullanarak liste üzerinde uygulayın. -

liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]

# a) "3" değerine ulaşmak için indexleme yapın.
print(liste[3])

# b) "Hi-Kod" değerine ulaşmak için indexleme yapın.

print(liste[5])

# c) 4.7 değerine ulaşmak için indexleme yapın.

print(liste[-1])

# d) 9,"3",8.4,"Hi-Kod" değerlerine ulaşmak için slicing yapın.

print(liste[2:6])

# e) 8.4,"Hi-Kod","False",4.7 değerlerine ulaşmak için slicing yapın.

print(liste[4:8])


# ödev2- Verilen listede bulunan string veri tipindeki öğeleri yeni_liste isimli listeye eklenir.

liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]

yeni_liste = []

for eleman in liste:
    if isinstance(eleman, str):
        yeni_liste.append(eleman)

print(yeni_liste)




# ödev3 - Enumerate methodunu araştırın ve aşağıdaki örneği enumerate methodu ile yapın.

# for index in range(len(meyveler)):

#     print("{}. indexte bulunan meyve: {}".format(index,meyveler[index])

meyveler = ["elma", "armut", "muz", "çilek"]

# enumerate() ile liste elemanları ve indekslerine aynı anda erişim
for index, meyve in enumerate(meyveler):
    print("{}. indexte bulunan meyve: {}".format(index, meyve))
