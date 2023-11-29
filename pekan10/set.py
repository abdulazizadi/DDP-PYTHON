motor = {"Beat","Vario","Aerox",}
mobil = {"Lamborgini","Ferrari","Bemo","Angkot"}

# menambah item
motor.add("Nmax")
print(motor)

# menghapus item
motor.remove("Beat")

# Menggabungkan set
kendaraan = motor.union(mobil)
print(kendaraan)

#Update set
motor.update (mobil)
print(motor)