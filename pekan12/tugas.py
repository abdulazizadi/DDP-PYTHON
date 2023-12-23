class Animal:
    def __init__(self, nama, makanan, habitat, cara_berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.cara_berkembang_biak = cara_berkembang_biak

    def makan(self):
        print(f"{self.nama} sedang makan {self.makanan}")

    def hidup(self):
        print(f"{self.nama} hidup di {self.habitat}")

    def berkembang_biak(self):
        print(f"{self.nama} berkembang biak dengan cara {self.cara_berkembang_biak}")


class Badak(Animal):
    def __init__(self, nama, habitat):
        super().__init__(nama, "tumbuhan", habitat, "reproduksi seksual")
        self.ukuran_cula = "besar"
        self.jenis_kulit = "tebal"

    def menyerang(self):
        print(f"{self.nama} menyerang dengan cula {self.ukuran_cula}")


class Ikan(Animal):
    def __init__(self, nama, habitat):
        super().__init__(nama, "plankton", habitat, "pemijahan")
        self.jenis_ekor = "dorsal"
        self.warna_sisik = "perak"

    def berenang(self):
        print(f"{self.nama} berenang dengan ekor {self.jenis_ekor}")


class Ular(Animal):
    def __init__(self, nama, habitat):
        super().__init__(nama, "hewan kecil", habitat, "bertelur")
        self.panjang = "panjang"
        self.berbisa = True

    def merayap(self):
        print(f"{self.nama} sedang merayap dengan tubuhnya yang {self.panjang}")

    def gigit(self):
        if self.berbisa:
            print(f"{self.nama} menggigit dengan bisa")
        else:
            print(f"{self.nama} menggigit")


# Contoh penggunaan
badak = Badak("Badak", "padang rumput")
badak.makan()
badak.hidup()
badak.berkembang_biak()
badak.menyerang()

ikan = Ikan("Ikan", "laut")
ikan.makan()
ikan.hidup()
ikan.berkembang_biak()
ikan.berenang()

ular = Ular("Ular", "hutan")
ular.makan()
ular.hidup()
ular.berkembang_biak()
ular.merayap()
ular.gigit()
