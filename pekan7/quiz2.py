nama_pembeli = input("Masukkan Nama Pembeli: ")
no_hp_pembeli = input("Masukkan No Hp Pembeli: ")


pesan_menu = input("Pesan Menu Apa? (makanan atau minuman): ")

menu_makanan = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Ayam Geprek": 18000
}

menu_minuman = {
    "Aneka Jus": 15000,
    "Soft Drink": 10000,
    "Sweet Ice Tea": 5000
}

if pesan_menu.lower() == "makanan":
    print("Menu Makanan:")
    for makanan, harga in menu_makanan.items():
        print(f"{makanan} - Rp. {harga}")
elif pesan_menu.lower() == "minuman":
    print("Menu Minuman:")
    for minuman, harga in menu_minuman.items():
        print(f"{minuman} - Rp. {harga}")
else:
    print("Pilihan tidak valid. Hanya makanan atau minuman yang diperbolehkan.")

pesanan = input("Masukkan pesanan: ")
jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))
total_harga = 0

if pesan_menu.lower() == "makanan":
    if pesanan in menu_makanan:
        total_harga = menu_makanan[pesanan] * jumlah_pesanan
elif pesan_menu.lower() == "minuman":
    if pesanan in menu_minuman:
        total_harga = menu_minuman[pesanan] * jumlah_pesanan

print("Nama Pembeli:", nama_pembeli)
print("No Hp Pembeli:", no_hp_pembeli)
print("Menu yang di Pesan:", pesanan)
print("Jumlah Pesanan:", jumlah_pesanan)
print("Harga yang harus di bayarkan: Rp.", total_harga)
