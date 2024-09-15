# Ödev-1: Değişkenlere atanmış değerlerin veri tipleri arasında dönüşüm yapılır.
# x = 3
# x = float(x)
# print(x)

# y = 9.7
# y = int(y)
# print(y)

# z = "2"
# z = int(z)
# print(z)

# t = "92"
# t = float(t)
# print(t)

# r = "78.5"
# r = int(r)
# print(r)

# Ödev-2: İsimlerden oluşan üç değişkene yaş değerleri atanır. Belirlenen üç değişken birbiriyle karşılaştırma operatörleri ile karşılaştırılır.
#  Bu karşılaştırmalara mantıksal operatörler de eklenir.

# YAŞLAR ATANIR
# age_ayşe = 31
# age_kemal = 39
# age_talha = 34

# OPERATÖRLER KARŞILAŞTIRILIR

#comparsion = (age_ayşe < age_kemal) and (age_kemal > age_talha)
#print(f' Ayşenin yaşı Kemalden küçük mü ve Kemalin yaşı Talhadan büyük mü? {comparsion}')

# FARKLI BİR KARŞILAŞTIRMA

# comparsion = (age_ayşe == age_kemal) or (age_kemal > age_talha)
# print(f'Ayşebin yaşı Kemale eşit mi ya da Kemalin yaşı Talhadan büyük mü? {comparsion}')


# Ödev-3: Kullanıcıdan iki değer girmesini istenir. Girilen değerlerin toplama, çıkarma, çarpma, bölme sonuçlarını yazdırılır.
# first_value = float(input('İlk sayıyı giriniz: '))
# second_value = float(input('İkinci sayıyı giriniz: '))

# işlem1 = first_value + second_value
# işlem2 = first_value - second_value
# işlem3 = first_value * second_value
# işlem4 = first_value / second_value

# print(f'Toplamları Sonucu: {işlem1}\n'
#       f'Çıkarma Sonucu: {işlem2}\n'
#       f'Çarpımları Sonucu: {işlem3}\n'
#       f'Bölümleri Sonucu: {işlem4}')


# Ödev-4: Kullanıcıdan isim, yaş, şehir ve meslek bilgilerini istenir ve cevaplarını yazdırılır.

# isim = input("İsminiz nedir? ")
# yaş = int(input("Yaşınız nedir?"))
# şehir = input("Yaşadığınız şehir neresidir? ")
# meslek = input("Mesleğiniz nedir? ")

# print(f'İsmim {isim}, yaşım {yaş}, {şehir} de yaşamaktayım ve {meslek} mezunuyum.')


# Ödev-5: "Hi-Kod Veri Bilimi Atölyesi" ifadesini bir değişkene tanımlanır.


#  İfadedeki her bir kelimeyi ("Hi-Kod", "Veri", "Bilimi", "Atölyesi") değişken içinden seçilir. 
#  İfadeyi hepsini büyük harf olacak hale çevrilir. ("HI-KOD VERİ BİLİMİ ATÖLYESİ") 
#  İfadeyi hepsini büyük harf olacak hale çevrilir.("hi-kod veri bilimi atölyesi") 

# "Hi-Kod Veri Bilimi Atölyesi" ifadesini bir değişkene tanımlıyoruz.
ifade = "Hi-Kod Veri Bilimi Atölyesi"

# 1. İfadedeki her bir kelimeyi ("Hi-Kod", "Veri", "Bilimi", "Atölyesi") ayırmak
kelimeler = ifade.split()
print("Kelime listesi:", kelimeler)

# 2. İfadeyi tümüyle büyük harfe çevirmek
bh_ifade = ifade.upper()
print("Büyük harfli ifade:",bh_ifade )

# 3. İfadeyi tümüyle küçük harfe çevirmek
kh_ifade = ifade.lower()
print("Küçük harfli ifade:", kh_ifade)



# "0123456789" ifadesindeki yalnızca çift sayıları ve yalnızca tek sayıları seçilir. ("02468", "13579")

# "0123456789" ifadesini bir değişkene tanımlıyoruz.
sayılar = "0123456789"

# 1. Yalnızca çift sayıları seçmek
çift_sayılar = sayılar[::2]  # 0'dan başlayıp her 2 adımda bir sayıyı seçer
print("Çift sayılar:", çift_sayılar)

# 2. Yalnızca tek sayıları seçmek
tek_sayılar = sayılar[1::2]  # 1'den başlayıp her 2 adımda bir sayıyı seçer
print("Tek sayılar:", tek_sayılar)
