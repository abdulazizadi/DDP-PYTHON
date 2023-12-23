class Orang :
    def init (self,fnama,lnama):
        self.fnama = fnama
        self.fnama = lnama
    
    def makan(self):
        print("saya bisa makan")
    
    def cetak(self):
        print("nama saya ",self.fnama, self.lnama)

class Mahasiswa(Orang):
    def init(self, fnama, lnama, prodi, angkatan):
            super().init(fnama, lnama)
            self.prodi = prodi
            self.angkatan = angkatan

    def print(self):
        super().cetak

class Pegawai(Orang):
    def bekerja(self):
        print("saya bekerja")

# objek orang
x = Orang("Bagus", "Maulana")
x.cetak()
# x.bekerja()

# objek mahasiswa
y = Mahasiswa("Dwi", "Astuti" ,"Teknik Informatika", 2023)
y.cetak()
y.makan()

# objek pegawai
agus = Pegawai("Agus", "Rahman")
agus.bekerja()

