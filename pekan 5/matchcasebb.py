print ("""
===================================
Sistem penghitung berat badan ideal

Pilih jenis kelamin:
1.Laki-laki
2.Perempuan""")

jk = int(input("masukkan pilihan jenis kelamin:"))
tinggi= int(input("masukkan tinggi badan:"))

match jk:
    case 1:
        ideal = (tinggi - 100) - (tinggi -100) * 0.1
        print("berat badan ideal laki-laki untuk tinggi",tinggi,"adalah",ideal)
    case 2:
        ideal = (tinggi -100) - (tinggi -100) * 0.15
        print("berat badan ideal perempuan untuk tinggi",tinggi ,"adalah", ideal)
    case _:
        print("pilihan yang anda masukkan tidak valid.")