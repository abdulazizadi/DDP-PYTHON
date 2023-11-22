nama_kendaraan = input("Nama kendaraan? (contoh: mobil, motor): ")
jenis_bensin = input("Jenis bensin? (Pertalite, Pertamax, Pertamax Turbo): ")
kota_tujuan = input("Kota yang dituju? (Jakarta, Bekasi, Depok, Tangerang, Bogor): ")
jenis_bensin_data = {
    "Pertalite": {"harga_per_liter": 10000, "jarak_tempuh": 12},
    "Pertamax": {"harga_per_liter": 14000, "jarak_tempuh": 13},
    "Pertamax Turbo": {"harga_per_liter": 17000, "jarak_tempuh": 13.5}
}

jarak_kota_data = {
    "Jakarta": 20,
    "Bekasi": 35.7,
    "Depok": 5,
    "Tangerang": 99,
    "Bogor": 120.6
}

harga_per_liter = jenis_bensin_data.get(jenis_bensin, {}).get("harga_per_liter")
jarak_tempuh = jenis_bensin_data.get(jenis_bensin, {}).get("jarak_tempuh")
jarak_kota = jarak_kota_data.get(kota_tujuan)

if not harga_per_liter or not jarak_tempuh or not jarak_kota:
    print("Input tidak valid. Pastikan Anda memasukkan jenis bensin dan kota yang benar.")
else:

    pemakaian_bensin = jarak_kota / jarak_tempuh
    total_harga_bensin = pemakaian_bensin * harga_per_liter

    print("Nama Kendaraan:", nama_kendaraan)
    print("Jenis Bensin:", jenis_bensin)
    print("Kota yang dituju:", kota_tujuan)
    print("Pemakaian Bensin (liter):", pemakaian_bensin)
    print("Total Harga dari Bensin (rupiah):", total_harga_bensin)



