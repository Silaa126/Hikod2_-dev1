# Ödev-1: Kullanıcıdan maaş bilgisini istenir ve bu bilgiye göre maaşından ne kadar vergi kesileceğini hesaplanır. 
# Kullanıcının geliri;


# 1- 10000 ve altındaysa maaşından %5 kesinti olur. 
# 2-25000 ve altındaysa maaşından %10 kesinti olur. 
# 3- 45000 ve altındaysa maaşından %25 kesinti olur. 
# 4- Diğer koşullarda %30 kesinti olur. 

# Bu durumlara göre kullanıcının yeni maaşı yazdırılır.

# Kullanıcıdan maaş bilgisi alalım
# maas = float(input("Maaşınızı girin: "))

# # Vergi oranını belirleyelim
# if maas <= 10000:
#     vergi_orani = 0.05  # %5 vergi
# elif maas <= 25000:
#     vergi_orani = 0.10  # %10 vergi
# elif maas <= 45000:
#     vergi_orani = 0.25  # %25 vergi
# else:
#     vergi_orani = 0.30  # %30 vergi

# # Vergi miktarını ve net maaşı hesaplayalım
# vergi_miktari = maas * vergi_orani
# net_maas = maas - vergi_miktari

# # Sonuçları yazdıralım
# print(f"Vergi kesintisi: {vergi_miktari:.2f} TL")
# print(f"Net maaş: {net_maas:.2f} TL")



# Ödev-2: Kullanıcıdan kullanıcı adı ve şifre oluşturmasını istenir.
#  Şifrenin uzunluğu altı haneye ulaşmışsa hesabınız oluşturuldu mesajı alınır, 
#  altı haneden azsa altı haneli şifre oluşturması gerektiğinin mesajı alınır. (Sadece koşul kullanılması yeterli.)

# kullanıcı_adı = input("Lütfen kullanıcı adınızı giriniz: ")
# şifre = input("Lütfen şifrenizi giriniz: ")

# if len(şifre) == 6:
#     print(f"Hesabınız başarıyla oluşturuldu:)")
# elif len(şifre) < 6 :
#     print(f"Lütfen şifrenizi 6 haneli olacak şekilde tekrar giriniz!!")


# Ödev-3: Bir önceki örnek geliştirilir.


#  Kullanıcı girdiği şifre 5 ve 10 hane arasında olmak zorunda. 
#  Eğer bu koşula uyuyorsa "Hesabınız oluşturuldu." mesajı alır. 
#  Koşulu sağlamıyorsa "Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!" uyarısı alır. 
#  Bunu oluştururken kullanıcı istediğimiz şartlarda şifre oluşturana kadar sormaya devam eder 


# # Kullanıcıdan kullanıcı adı isteyelim
# kullanıcı_adı = input("Lütfen kullanıcı adınızı giriniz: ")

# # İlk şifre isteği
# şifre = input("Lütfen şifrenizi giriniz: ")

# # Şifre 5 ile 10 karakter arasında olmadığı sürece döngü devam edecek
# while len(şifre) < 5 or len(şifre) > 10:
#     print("Lütfen girdiğiniz şifre 5 haneden az, 10 haneden fazla olmasın!")
#     şifre = input("Lütfen şifrenizi tekrar giriniz: ")

# # Koşul sağlandığında şifre kabul edilecek
# print("Hesabınız oluşturuldu.")

# Ödev-4: Kullanıcıdan isim ve şifre isteyeceğiz ve şifre girişi için üç hak verilir.


#  Eğer önceden tanımlı şifre ile kullanıcıdan gelen şifre aynıysa "Giriş yapıldı." yazar. 
#  Şifre girişi yanlışsa "Yanlış şifre girildi!" uyarısı verilsin ve üç yanlış denemede program biter. 
#  Tercihe göre kalan hak bilgisi verilir. 

# Doğru şifreyi belirleyelim
dogru_sifre = "12345"
deneme_hakki = 3  # Kullanıcının giriş hakkı

while deneme_hakki > 0:
    # Kullanıcıdan şifre isteyelim
    sifre = input("Lütfen şifrenizi giriniz: ")

    # Girilen şifreyi kontrol edelim
    if sifre == dogru_sifre:
        print("Giriş başarılı!")
        break  # Doğru şifre girildiyse döngüden çık
    else:
        deneme_hakki -= 1  # Yanlış şifre girildiğinde deneme hakkını azalt
        print(f"Yanlış şifre! Kalan deneme hakkı: {deneme_hakki}")

# Giriş hakkı kalmadığında mesaj verelim
if deneme_hakki == 0:
    print("Giriş hakkınız kalmadı. Lütfen daha sonra tekrar deneyin.")


