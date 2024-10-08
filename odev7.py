import pandas as pd


sozluk = {"Kategori": ["Giyim","Giyim", "Ayakkabı","Aksesuar","Ayakkabı","Giyim","Aksesuar","Aksesuar","Ayakkabı","Giyim"],
          "Ürün" : ["Kazak","T-shirt","Sandalet","Küpe","Spor Ayakkabı","Pantolon","Kolye","Yüzük","Çizme","Ceket"],
        "Fiyat" : [300,180,450,50,700,400,150,80,850,900]}

# 1- Yukarıdaki sözlük DataFrame’e dönüştürülür. 
data = pd.DataFrame(sozluk)

# 2- Yukarıdaki DataFrame için 2.indexte bulunan kategori bulunur. (Sadece kategori bilgisi) 
#kategori_2_index = sozluk["Kategori"][2]

# 3- 2. indexte bulunan ürün bulunur. (Sadece ürün bilgisi)
# ürün_2_index = sozluk["Ürün"][2] 
# print(ürün_2_index)

# 4- 4.indexten 9.indexe kadar olan veriler bulunur. (Kategori,ürün,fiyat bilgisi beraber) 
# kategori_urun_fiyat = {
#     "Kategori": sozluk["Kategori"][4:10],
#     "Ürün": sozluk["Ürün"][4:10],
#     "Fiyat": sozluk["Fiyat"][4:10]
# }

# print(kategori_urun_fiyat)

# 5-  1.indexten 6.indexe kadar olan ürünler bulunur. (Sadece ürün bilgisi) 
# ürün_bilgi = sozluk["Ürün"][1:6]
# print(ürün_bilgi)

# 6- Giyim kategorisinde bulunan ürünler gösterilir. 
# giyim_urunleri = data[data["Kategori"] == "Giyim"][["Kategori", "Ürün"]]
# print(giyim_urunleri)

#7-Ayakkabı kategorisinde bulunan ürünler gösterilir. 
# ayak_urunleri = data[data["Kategori"] == "Ayakkabı"][["Kategori", "Ürün"]]
# print(ayak_urunleri)

# 8- Aksesuar kategorisinde bulunan ürünler gösterilir. 
# aksesuar_urunleri = data[data["Kategori"] == "Aksesuar"][["Kategori", "Ürün"]]
# print(aksesuar_urunleri)

# 9- Giyim kategorisinde fiyatı 300'den fazla olan ürünler gösterilir. 
# giyim = data[(data["Kategori"] == "Giyim") & (data["Fiyat"] > 300)][["Kategori", "Ürün", "Fiyat"]]
# print(giyim)

# 10-  Ayakkabı kategorisinde fiyatı 600'den az olan ürünler gösterilir. 
# ayakkabı = data[(data["Kategori"] == "Giyim") & (data["Fiyat"] < 600)][["Kategori","Ürün","Fiyat"]]
# print(ayakkabı)

# 11-Aksesuar kategorisinde fiyatı 100'den fazla olan aksesuar gösterilir.  
aksesuar = data[(data["Kategori"] == "Aksesuar") & (data["Fiyat"]< 100)][["Kategori","Fiyat","Ürün"]]
print(aksesuar)