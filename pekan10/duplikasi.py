def duplikasi(daftar_buah):
    hasil = []

    for buah in daftar_buah:
        hasil.append(buah)
        hasil.append(buah)

    return hasil

# Contoh penggunaan

buah_asli = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
hasil_duplikasi = duplikasi(buah_asli)
print(hasil_duplikasi)