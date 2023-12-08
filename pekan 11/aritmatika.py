import math
def tambah (bil1,bil2):
    hasil = bil1+bil2
    print("hasil tambah dari",bil1,"+",bil2,"=",hasil)

def kurang (bil1, bil2):
    hasil = bil1-bil2
    print("hasil pengurangan dari",bil1,"-",bil2,"=",hasil)

def kali(bil1, bil2):
    hasil = bil1 * bil2
    print("hasil perkalian dari",bil1,"*",bil2,"=",hasil)

def bagi(bil1, bil2):
    hasil = bil1 / bil2
    print("hasil pembagian dari",bil1,"/",bil2,"=",hasil)

def pangkat(bil1, bil2):
    hasil = math.pow(bil1, bil2)
    print("hasil pemangkatan dari",bil1,"^",bil2,"=",hasil)

def akar_kuadrat(bil):
    hasil = math.sqrt(bil)
    print("hasil akar kuadrat dari", bil,"=",hasil)

def log(bil):
    log = math.log(bil)
    hasil = round(log, bil)
    print ("hasil log dari", bil,"=",hasil)

def cos(bil):
    cos = math.cos(bil)
    hasil = round(cos, bil)
    print ("hasil dari cos",bil,"=",hasil)

def modulus(bil1, bil2):
    hasil = math.fmod(bil1, bil2)
    print ("hasil dari modulus",bil1,"%",bil2,"=",hasil)
    
def pembagian_bulat (bil):
    hasil = math.floor(bil / 2)
    print ("hasil dari pembagian bulat",bil,"//2","=",hasil)