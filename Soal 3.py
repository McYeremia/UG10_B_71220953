print ("Selamat Datang Di Program Pengurutan Bilangan")
print ("Silahkan Pilih Metode Yang Akan Dipakai")
print ("")
print ("1. Ascending")
print ("2. Descending")
print ("")
pil = int(input("Masukkan Pilihan yang Anda Inginkan: "))
print ("")
if pil == 1:
    b1 = int(input("Masukan Bilangan Bulat Pertama: "))
    b2 = int(input("Masukan Bilangan Bulat Kedua: "))
    b3 = int(input("Masukan Bilangan Bulat Ketiga: "))
    b4 = int(input("Masukan Bilangan Bulat Keempat: "))
    list1 = [b1 , b2 , b3 , b4]
    print ("Urutan angka dari yang terkecil adalah ", sorted(list1))
elif pil == 2:
    b1 = int(input("Masukan Bilangan Bulat Pertama: "))
    b2 = int(input("Masukan Bilangan Bulat Kedua: "))
    b3 = int(input("Masukan Bilangan Bulat Ketiga: "))
    b4 = int(input("Masukan Bilangan Bulat Keempat: "))
    list1 = [b1 , b2 , b3 , b4]
    print ("Urutan angka dari yang terbesar adalah ", sorted(list1,reverse=True))
else:
    print ("Data yang di input salah")