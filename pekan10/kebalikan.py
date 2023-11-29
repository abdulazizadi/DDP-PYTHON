def kebalikan(daftar_buah):
    panjang = len(daftar_buah)
    hasil = []

    for i in range(panjang - 1, -1, -1):
        hasil.append(daftar_buah[i])

    return hasil

# Contoh penggunaan
buah_asli = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
hasil_kebalikan = kebalikan(buah_asli)
print(hasil_kebalikan)