#Beyzanur GENÇTÜRK
#GİTHUB hesabımın linki : https://github.com/beyzanurGencturk
from Admin import Admin
from Okuyucu import Okuyucu


# kullanıcı verileri
kullanicilar = [{'eposta': 'admin', 'sifre': 'admin123', 'yetki': 'admin'},
                {'eposta': 'okuyucu1', 'sifre': 'sifre1', 'yetki': 'okuyucu'},
                {'eposta': 'okuyucu2', 'sifre': 'sifre2', 'yetki': 'okuyucu'}]

# üye ol fonksiyonu
def uye_ol():
    print("Sisteme Üye Ol\n")
    eposta = input("E-posta adresinizi girin: ")
    sifre = input("Şifrenizi girin: ")
    kullanici = {'eposta': eposta, 'sifre': sifre, 'yetki': 'okuyucu'}
    kullanicilar.append(kullanici)
    print("Kaydınız başarıyla oluşturuldu!\n")

# giriş yap fonksiyonu
def giris_yap():
    print("Sisteme Giriş Yap\n")
    eposta = input("E-posta adresinizi girin: ")
    sifre = input("Şifrenizi girin: ")
    for kullanici in kullanicilar:
        if kullanici['eposta'] == eposta and kullanici['sifre'] == sifre:
            if kullanici['yetki'] == 'admin':
                print("Admin olarak giriş yapıldı.\n")
            else:
                print("Kullanıcı olarak giriş yapıldı.\n")
            return
    print("Hatalı e-posta adresi veya şifre!\n")

# şifremi unuttum fonksiyonu
def sifremi_unuttum():
    print("Şifremi Unuttum\n")
    eposta = input("E-posta adresinizi girin: ")
    for kullanici in kullanicilar:
        if kullanici['eposta'] == eposta:
            secim = input("1- Yeni şifre belirle\n2- Şifremi göster\nSeçiminiz: ")
            if secim == '1':
                sifre = input("Yeni şifrenizi girin: ")
                kullanici['sifre'] = sifre
                print("Yeni şifreniz başarıyla oluşturuldu!\n")
            elif secim == '2':
                print(f"Şifreniz: {kullanici['sifre']}\n")
            else:
                print("Geçersiz seçim!\n")
            return
    print("Böyle bir e-posta adresi kayıtlı değil!\n")


# admin yetki ve işlemleri
def admin_menu():
    admin = Admin()

    while True:
        print("---------- ADMIN İŞLEMLERİ ----------")
        print("1- Kitap Ekle")
        print("2- Kitap Sil")
        print("3- Kitap Listele")
        print("4- Okuyucu Ekle")
        print("5- Okuyucu Kitap Ekle")
        print("6- Okuyucu Kitap Sil")
        print("7- Okuyucu Kitaplarını Listele")
        print("8- Geri")

        secim = input("Lütfen yapmak istediğiniz işlemi seçiniz (1-8): ")

        if secim == "1":
            kitap = input("Eklemek istediğiniz kitabın adını girin: ")
            admin.kitap_ekle(kitap)
        elif secim == "2":
            kitap = input("Silmek istediğiniz kitabın adını girin: ")
            admin.kitap_sil(kitap)
        elif secim == "3":
            admin.kitap_listele()
        elif secim == "4":
            ad = input("Okuyucunun adını girin: ")
            soyad = input("Okuyucunun soyadını girin: ")
            email = input("Okuyucunun email adresini girin: ")
            admin.okuyucu_ekle(ad, soyad, email)
        elif secim == "5":
            email = input("Kitap eklemek istediğiniz okuyucunun email adresini girin: ")
            kitap = input("Eklemek istediğiniz kitabın adını girin: ")
            admin.okuyucu_kitap_ekle(email, kitap)
        elif secim == "6":
            email = input("Kitap silmek istediğiniz okuyucunun email adresini girin: ")
            kitap = input("Silmek istediğiniz kitabın adını girin: ")
            admin.okuyucu_kitap_sil(email, kitap)
        elif secim == "7":
            email = input("Kitaplarını listelemek istediğiniz okuyucunun email adresini girin: ")
            admin.okuyucu_kitaplar(email)
        elif secim == "8":
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyiniz.")

        print()

# okuyucu yetki ve işlemleri
def okuyucu_menu():
    ad = input("Adınızı girin: ")
    soyad = input("Soyadınızı girin: ")
    email = input("Email adresinizi girin: ")

    okuyucu = Okuyucu(ad, soyad, email)

    while True:
        print("---------- OKUYUCU İŞLEMLERİ ----------")
        print("1- Kitap Ekle")
        print("2- Kitap Sil")
        print("3- Kitap Listele")
        print("4- Geri")

        secim = input("Lütfen yapmak istediğiniz işlemi seçiniz (1-4): ")

        if secim == "1":
            kitap = input("Eklemek istediğiniz kitabın adını girin: ")
            okuyucu.kitap_ekle(kitap)
        elif secim == "2":
            kitap = input("Silmek istediğiniz kitabın adını girin: ")
            okuyucu.kitap_sil(kitap)
        elif secim == "3":
            okuyucu.kitap_listele()
        elif secim == "4":
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyiniz.")

        print()

def menu():
    print("---------- KÜTÜPHANE SİSTEMİ ----------")
    print("1- Sisteme Üye Ol")
    print("2- Sisteme Giriş Yap")
    print("3- Şifremi Unuttum")
    print("4- Admin İşlemleri")
    print("5- Okuyucu İşlemleri")
    print("6- Çıkış Yap")

    secim = input("Lütfen yapmak istediğiniz işlemi seçiniz (1-4): ")

    if secim == "1":
        uye_ol()
    elif secim == "2":
        giris_yap()
    elif secim == "3":
        sifremi_unuttum()
    elif secim == "4":
        admin_menu()
    elif secim == "5":
        okuyucu_menu()
    elif secim == "6":
        print("Çıkış yapmayı seçtiniz ! Programdan çıkış yapılıyor...")
        exit()
    else:
        print("Geçersiz seçim ! Lütfen tekrar deneyiniz !")
        menu()

while(1):
    menu()