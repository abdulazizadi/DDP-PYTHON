data_diri = {"nama":"Aziz","rombel":"23TI03"}

# mengkses dictiornary
print(data_diri["nama"])

# menambah item
data_diri["jurusan"] = "Teknik informatika"
print(data_diri)

#update item
data_diri["nama"]= "Abdul Aziz Adi"
print(data_diri)

# menghapus item
data_diri.pop ("rombel")
print(data_diri)


#cek keberadaan key

if "nama" in data_diri:
    print("Terdapat Nama")
else: 
    print("Tidak ada nama")