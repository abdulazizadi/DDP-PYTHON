jumlah_baris = int (input("masukan jumlah:"))

for i in range (0, jumlah_baris + 1):
    for kolom in range (i):
        print ("*" ,end="")
    print()