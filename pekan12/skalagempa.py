class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            return "Dampak gempa di {} tidak berasa.".format(self.lokasi)
        elif 2 <= self.skala < 4:
            return "Dampak gempa di {} membuat bangunan retak-retak.".format(self.lokasi)
        elif 4 <= self.skala < 6:
            return "Dampak gempa di {} membuat bangunan roboh.".format(self.lokasi)
        else:
            return "Dampak gempa di {} membuat bangunan roboh dan berpotensi tsunami.".format(self.lokasi)