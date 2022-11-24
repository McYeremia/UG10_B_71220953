print ("========== PROGRAM PENGHITUNG PYTHAGORAS ==========")
bsatu = int(input("Masukkan bilangan bulat pertama: "))
bdua = int(input("Masukkan bilangan bulat kedua: "))
btiga = int(input("Masukkan bilangan bulat ketiga : "))
hasil = (bsatu ** 2) + (bdua ** 2) 
if hasil == (btiga ** 2):
    print("Merupakan Pythagoras")
else:
    print("Bukan Merupakan Pythagoras")
