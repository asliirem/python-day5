class Hayvan:
    def __init__(self, isim, tur, yas):
        self.isim = isim
        self.tur = tur
        self.yas = yas

    def bilgi_yazdir(self):
        print("İsim:", self.isim)
        print("Tür:", self.tur)
        print("Yaş:", self.yas)

hayvan1 = Hayvan("pamuk","Kedi", 3)
hayvan2 = Hayvan("Kömür", "Köpek", 5)

hayvan1.bilgi_yazdir()
print("-----")
hayvan2.bilgi_yazdir()