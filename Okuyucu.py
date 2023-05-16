class Okuyucu:
    def __init__(self, ad, soyad, email):
        self.ad = ad
        self.soyad = soyad
        self.email = email
        self.kitaplar = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
        print(f"{kitap} kitabı başarıyla eklendi.")

    def kitap_sil(self, kitap):
        if kitap in self.kitaplar:
            self.kitaplar.remove(kitap)
            print(f"{kitap} kitabı başarıyla silindi.")
        else:
            print(f"{kitap} kitabı bulunamadı.")

    def kitap_listele(self):
        print("Kitap Listesi:")
        for kitap in self.kitaplar:
            print(kitap)
