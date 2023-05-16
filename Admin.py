class Admin:
    def __init__(self):
        self.kitaplar = []
        self.okuyucular = {}

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

    def okuyucu_ekle(self, ad, soyad, email):
        if email not in self.okuyucular:
            self.okuyucular[email] = {'ad': ad, 'soyad': soyad, 'kitaplar': []}
            print(f"{ad} {soyad} isimli okuyucu başarıyla eklendi.")
        else:
            print("Bu email adresine sahip bir okuyucu zaten var.")

    def okuyucu_kitap_ekle(self, email, kitap):
        if email in self.okuyucular:
            self.okuyucular[email]['kitaplar'].append(kitap)
            print(f"{self.okuyucular[email]['ad']} {self.okuyucular[email]['soyad']} isimli okuyucuya {kitap} kitabı eklendi.")
        else:
            print("Okuyucu bulunamadı.")

    def okuyucu_kitap_sil(self, email, kitap):
        if email in self.okuyucular:
            if kitap in self.okuyucular[email]['kitaplar']:
                self.okuyucular[email]['kitaplar'].remove(kitap)
                print(f"{self.okuyucular[email]['ad']} {self.okuyucular[email]['soyad']} isimli okuyucunun {kitap} kitabı silindi.")
            else:
                print("Kitap bulunamadı.")
        else:
            print("Okuyucu bulunamadı.")

    def okuyucu_kitaplar(self, email):
        if email in self.okuyucular:
            if len(self.okuyucular[email]['kitaplar']) == 0:
                print("Okuyucunun kitapları bulunamadı.")
            else:
                print(f"{self.okuyucular[email]['ad']} {self.okuyucular[email]['soyad']} isimli okuyucunun kitapları:")
                for kitap in self.okuyucular[email]['kitaplar']:
                    print(kitap)
        else:
            print("Okuyucu bulunamadı.")
