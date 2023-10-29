def hitung_luas():
    pilihan = int(input("Pilih bangun datar (1: Persegi, 2: Lingkaran, 3: Segitiga): "))

    match pilihan:
        case 1:
            sisi = float(input("Masukkan panjang sisi persegi: "))
            luas = sisi * sisi
            print(f"Luas persegi: {luas}")
        case 2:
            jari_jari = float(input("Masukkan jari-jari lingkaran: "))
            luas = 3.14 * jari_jari * jari_jari
            print(f"Luas lingkaran: {luas}")
        case 3:
            alas = float(input("Masukkan panjang alas segitiga: "))
            tinggi = float(input("Masukkan tinggi segitiga: "))
            luas = 0.5 * alas * tinggi
            print(f"Luas segitiga: {luas}")
        case _:
            print("Salah pilih angka!")

hitung_luas()