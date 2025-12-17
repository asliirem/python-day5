class Person:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
    
    def bilgi_yazdir(self):
        print("İsim:", self.isim)
        print("Yaş:", self.yas)

class Student(Person):
    def __init__(self, isim, yas, ortalama):
        super().__init__(isim,yas)
        self.ortalama =ortalama
    
    def durum(self):
        if self. ortalama >= 60:
            return "Geçti"
        else:
            return "Kaldı"

class Employee(Person):
    def __init__(self, isim, yas, maas):
        super().__init__(isim, yas)
        self.maas = maas
    
    def maas_bilgisi(self):
        return f"Maaş: {self.maas} TL"
    
ogrenci = Student("İrem", 21, 80)
calisan = Employee("Hasan", 32, 25000)

ogrenci.bilgi_yazdir()
print("Ortalama", ogrenci.ortalama)
print("Durum:", ogrenci.durum())

print("-----")

calisan.bilgi_yazdir()
print(calisan.maas_bilgisi())
                    