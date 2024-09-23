# • Kullanıcıdan pi değeri ve yarıçap bilgisi alarak dairenin alanını hesaplayan bir fonksiyon 
# oluşturulur.

# def daire_alani(yaricap):
#     alan = pi * yaricap ** 2
#     return alan

# # Kullanıcıdan yarıçapı al
# yaricap = float(input("Dairenin yarıçapını girin: "))
# pi = float(input("Lütfen pi değerini giriniz: "))
# alan = daire_alani(yaricap)

# print(f"Yarıçapı {yaricap} olan dairenin alanı: {alan}")


# • Faktöriyel adında fonksiyon oluşturulur. Döngü kullanarak parametre olarak girilen 
# sayının faktöriyeli hesaplanır. Format metodunu kullanılarak ekrana yazdırılır.

# def faktoriyel(sayi):
#     sonuc = 1
#     for i in range(1, sayi + 1):
#         sonuc *= i
#     return sonuc

# # Kullanıcıdan sayı al
# sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))

# # Faktöriyel hesapla
# faktoriyel_sonuc = faktoriyel(sayi)

# # Sonucu format metodu ile ekrana yazdır
# print("Girilen sayının faktöriyeli: {}".format(faktoriyel_sonuc))


# • Kişinin fonksiyona doğum yılını vererek kaç yaşında olduğunu hesaplayan bir
#  fonksiyon oluşturun. 

# def yas(dogum_yili):
#     yil = 2024
#     yas_hesapla = yil - dogum_yili
#     return yas_hesapla

# dogum_yili = float(input("Lütfen doğum yılınızı giriniz: "))
# yasiniz = yas(dogum_yili)

# print(f"Yaşınız: {yasiniz}")



# • Doğum yılı ve isim bilgisi verilen fonksiyon kişinin emekli olup olmadığını söylesin.
# (Kişi 65 yaşında ise emekli olur.) Burada yaş hesabını yukarıdaki örnekteki fonksiyonu kullanarak
# yapsın.(Yani fonksiyon içinde fonksiyon kullanmanızı istiyorum :)) Kişi 65 yaşında ya da daha
# fazlaysa "Emekli oldunuz" yanıtını, 65 yaşından küçükse emekliliğine kaç yıl kaldığını da 
# hesaplayarak "(isim) emekliliğine (yıl) kaldı." yanıtını versin.


def yas(dogum_yili):
    yil = 2024
    yas_hesapla = yil - dogum_yili
    return yas_hesapla


# Emeklilik durumunu kontrol eden fonksiyon
def emeklilik_durumu(dogum_yili, isim):
    mevcut_yas = yas(dogum_yili)  # Yaşı hesaplamak için yas() fonksiyonunu kullanıyoruz
    
    if mevcut_yas >= 65:
        return f"{isim}, emekli oldunuz."
    else:
        kalan_yil = 65 - mevcut_yas
        return f"{isim}, emekliliğine {kalan_yil} yıl kaldı."

dogum_yili = 1999
isim = "Leyla"

# Emeklilik durumunu hesapla ve ekrana yazdır
sonuc = emeklilik_durumu(dogum_yili, isim)
print(sonuc)
