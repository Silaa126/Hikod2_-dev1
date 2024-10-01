# Bir sözlük oluşturulur ve bu sözlükte öğrencilerin isimleri ve Matematik, Fizik, Kimya notları tutulur. 
# Kullanıcıdan isim ve ders ismi(Matematik, Fizik, Kimya) istenir ve bu bilgilere göre çıktı verilirnames

# Öğrenci bilgilerini içeren sözlük
ogrenci_notlari = {
    "Ahmet Uğur": {"Matematik": 95, "Fizik": 40, "Kimya": 18},
    "Aylin Sevinç": {"Matematik": 92, "Fizik": 88, "Kimya": 95},
    "Mehmet Koyuncu": {"Matematik": 78, "Fizik": 80, "Kimya": 20}
}

# Kullanıcıdan öğrenci ismi ve ders ismi alınır
ogrenci_ismi = input("Öğrenci ismi girin: ")
ders_ismi = input("Ders ismi girin (Matematik, Fizik, Kimya): ")

# Girilen öğrenci ve ders bilgilerine göre not görüntüleme
if ogrenci_ismi in ogrenci_notlari:
    if ders_ismi in ogrenci_notlari[ogrenci_ismi]:
        print(f"{ogrenci_ismi} isimli öğrencinin {ders_ismi} notu: {ogrenci_notlari[ogrenci_ismi][ders_ismi]}")
    else:
        print(f"{ders_ismi} dersi bulunamadı.")
else:
    print(f"{ogrenci_ismi} isimli öğrenci bulunamadı.")


# Sözlük üzerinde değerleri değiştirme, yeni değer ekleme, kullanıcıya ulaşmak istediği bilgileri 
# sorma gibi uygulamalar yapın.

# Öğrenci bilgilerini içeren sözlük
ogrenci_notlari = {
    "Ahmet": {"Matematik": 85, "Fizik": 90, "Kimya": 78},
    "Ayşe": {"Matematik": 92, "Fizik": 88, "Kimya": 95},
    "Mehmet": {"Matematik": 75, "Fizik": 82, "Kimya": 80}
}

# Kullanıcıya yapılacak işlemi soran fonksiyon
def menu_goster():
    print("\nSeçenekler:")
    print("1. Öğrenci notunu görüntüle")
    print("2. Öğrenci notunu güncelle")
    print("3. Yeni öğrenci ekle")
    print("4. Çıkış")
    return input("Bir seçenek girin (1-4): ")

# Öğrenci notunu görüntüleme fonksiyonu
def ogrenci_notu_goster(ogrenci_notlari):
    ogrenci_ismi = input("Öğrenci ismi girin: ")
    ders_ismi = input("Ders ismi girin (Matematik, Fizik, Kimya): ")

    if ogrenci_ismi in ogrenci_notlari:
        if ders_ismi in ogrenci_notlari[ogrenci_ismi]:
            print(f"{ogrenci_ismi} isimli öğrencinin {ders_ismi} notu: {ogrenci_notlari[ogrenci_ismi][ders_ismi]}")
        else:
            print(f"{ders_ismi} dersi bulunamadı.")
    else:
        print(f"{ogrenci_ismi} isimli öğrenci bulunamadı.")

# Öğrenci notunu güncelleme fonksiyonu
def ogrenci_notu_guncelle(ogrenci_notlari):
    ogrenci_ismi = input("Notunu güncellemek istediğiniz öğrenci ismini girin: ")
    ders_ismi = input("Ders ismi girin (Matematik, Fizik, Kimya): ")

    if ogrenci_ismi in ogrenci_notlari:
        if ders_ismi in ogrenci_notlari[ogrenci_ismi]:
            yeni_not = int(input(f"{ogrenci_ismi} için yeni {ders_ismi} notunu girin: "))
            ogrenci_notlari[ogrenci_ismi][ders_ismi] = yeni_not
            print(f"{ogrenci_ismi} isimli öğrencinin {ders_ismi} notu güncellendi: {yeni_not}")
        else:
            print(f"{ders_ismi} dersi bulunamadı.")
    else:
        print(f"{ogrenci_ismi} isimli öğrenci bulunamadı.")

# Yeni öğrenci ekleme fonksiyonu
def yeni_ogrenci_ekle(ogrenci_notlari):
    yeni_ogrenci = input("Yeni öğrencinin ismini girin: ")
    
    if yeni_ogrenci in ogrenci_notlari:
        print(f"{yeni_ogrenci} zaten kayıtlı.")
    else:
        matematik_notu = int(input(f"{yeni_ogrenci} için Matematik notunu girin: "))
        fizik_notu = int(input(f"{yeni_ogrenci} için Fizik notunu girin: "))
        kimya_notu = int(input(f"{yeni_ogrenci} için Kimya notunu girin: "))
        
        ogrenci_notlari[yeni_ogrenci] = {
            "Matematik": matematik_notu,
            "Fizik": fizik_notu,
            "Kimya": kimya_notu
        }
        print(f"{yeni_ogrenci} isimli öğrenci eklendi.")

# Ana döngü
while True:
    secim = menu_goster()

    if secim == '1':
        ogrenci_notu_goster(ogrenci_notlari)
    elif secim == '2':
        ogrenci_notu_guncelle(ogrenci_notlari)
    elif secim == '3':
        yeni_ogrenci_ekle(ogrenci_notlari)
    elif secim == '4':
        print("Programdan çıkılıyor.")
        break
    else:
        print("Geçersiz seçenek, lütfen tekrar deneyin.")
