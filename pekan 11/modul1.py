def persegi (sisi):
    luas = sisi * sisi 
    keliling = 4 * sisi
    print("Luas Persegi", luas)
    print("Keliling Persegi:",keliling)

def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling= 2 * (panjang + lebar)
    print("Luas persegi panjang:", luas)
    print("Keliling persegi panjang:", keliling)

def lingkaran (jari2):
    phi = 3,14
    luas= phi * jari2 * jari2
    keliling = 2 * phi * jari2
    print("Luas lingkaran:", luas)
    print("Keliling lingkaran:", keliling)

def segitiga_sama_sisi(alas,tinggi):
    luas= 0.5 * alas * tinggi
    keliling = alas * 3
    print("Luas segitiga sama sisi:", luas)
    print("Keliling segitiga sama sisi:", keliling)

def belah_ketupat (diagonal1,diagonal2,sisi):
    luas= 0.5 * diagonal1 * diagonal2
    keliling= 4 * sisi
    print("Luas belah ketupat:", luas)
    print("Keliling belah ketupat:", keliling)

def jajar_genjang (alas,tinggi,sisi_miring):
    luas = alas * tinggi 
    keliling= 2 * alas + sisi_miring
    print("Luas jajar genjang:", luas)
    print("Keliling jajar genjang:", keliling)

def layang_layang (diagonal1,diagonal2,sisi_atas,sisi_bawah):
    luas= diagonal1 * diagonal2 * 0.5
    keliling= (sisi_atas * 2) + (sisi_bawah * 2)
    print("Luas layang layang:", luas)
    print("Keliling layang layang:", keliling)





