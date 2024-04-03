class Personel:
    def __init__(self, ad, soyad, yas, kimlik_no):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.kimlik_no = kimlik_no

    def bilgileri_goster(self):
        print(f"Adı: {self.ad}\nSoyadı: {self.soyad}\nYaşı: {self.yas}\nKimlik No: {self.kimlik_no}")

class Ogrenci(Personel):
    ogrenciNo = "belirtilmedi"

    def __init__(self, ad, soyad, yas, kimlik_no, ogrenciNo=None):
        super().__init__(ad, soyad, yas, kimlik_no) ## super() fonksiyonu ile Personel sınıfının __init__ fonksiyonunu çağırıyoruz
        if ogrenciNo is not None:
            self.ogrenciNo = ogrenciNo

    def ogrenciNo_degistirme(self, yeni_ogrenciNo):
        self.ogrenciNo = yeni_ogrenciNo

    ## Ogrenci sınıfının bilgilerini göstermek için Personel sınıfının fonksiyonunu genişletelim
    def bilgileri_goster(self):
        super().bilgileri_goster() ## super() fonksiyonu ile Personel sınıfının fonksiyonunu çağırıyoruz
        print(f"Öğrenci No: {self.ogrenciNo}")


tunay = Ogrenci("tunay", "ince", 20, "1223456789", "222007560")
tunay.bilgileri_goster()
