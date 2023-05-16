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


def menu():
    print("---------- KÜTÜPHANE SİSTEMİ ----------")
    print("1- Sisteme Üye Ol")
    print("2- Sisteme Giriş Yap")
    print("3- Şifremi Unuttum")
    print("4- Çıkış Yap")

    secim = input("Lütfen yapmak istediğiniz işlemi seçiniz (1-4): ")

    if secim == "1":
        uye_ol()
    elif secim == "2":
        giris_yap()
    elif secim == "3":
        sifremi_unuttum()
    elif secim == "4":
        print("Çıkış yapmayı seçtiniz ! Programdan çıkış yapılıyor...")
        exit()
    else:
        print("Geçersiz seçim ! Lütfen tekrar deneyiniz !")
        menu()

while(1):
    menu()