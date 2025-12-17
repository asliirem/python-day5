class Ogrenci:
    def __init__(self, isim, vize, final):
        self.isim = isim
        self.vize = vize
        self.final = final
    def ortalama_hesapla(self):
        return(self.vize * 0.2) + (self.final * 0.8)
    def durum_yazdir(self):
         ortalama = self.ortalama_hesapla()

         print("Öğrenci:", self.isim)
         print("Ortalama:", ortalama)

         if ortalama >=60:
            print("Durum: Geçti ")
         else:
            print("Durum: Kaldı")   

    def harf_notu(self):
        ortalama = self.ortalama_hesapla()

        if ortalama >= 85:
            return "AA"
        elif ortalama >= 70:
            return "BB"
        elif ortalama >= 60:
            return "CC"
        else:
            return "FF"



ogrenci1 = Ogrenci("İrem", 64, 80)
ogrenci2 = Ogrenci("Pelin", 50, 40)

ogrenci1.durum_yazdir()
print("Harf Notu:", ogrenci1.harf_notu())

print("-----")

ogrenci2.durum_yazdir()
print("Harf Notu:", ogrenci2.harf_notu())
