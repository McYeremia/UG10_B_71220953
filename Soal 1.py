print ("~~~~~~~~~~ /('V')\ ~~~~~~~~~~")
print ("PROGRAM PENGHITUNG VOLUME BANGUN RUANG")
print ("~~~~~~~~~~ /('V')\ ~~~~~~~~~~")
print ("")
print ("Pilihlah salah satu bangun ruang yang ingin dihitung volumenya: ")
print ("1. Limas")
print ("2. Bola")
print ("3. Prisma")
print ("4. Kerucut")
print ("")
pilihan = input("Masukan pilihan Anda: ")
if pilihan == "1":
    plim = float(input ("Masukan panjang sisi alas limas: "))
    tlim = float(input ("Masukan tinggi limas: "))
    print ("Volume limas tersebut adalah", 1/3 * tlim * plim * plim)
elif pilihan == "2":
    phi = 3.14
    jbola = float(input("Masukan panjang jari-jari bola: "))
    print ("Volume bola tersebut adalah", 4/3 * phi * jbola ** 3)
elif pilihan == "3":
    print ("Pilihlah salah satu dari pilihan di bawah: ")
    print ("1. Prisma Segitiga")
    print ("2. Prisma Segiempat")
    print ("3. Prisma Segilima")
    pilp = input("Tentukan pilihan anda: ")
    if pilp == "1":
        apris = int(float(input("Masukkan panjang sisi alas prisma: ")))
        tapris = int(float(input("Masukkan tinggi alas prisma: ")))
        tppris = int(float(input("Masukkan tinggi prisma segitiga: ")))
        print ("Volume prisma segitiga tersebut adalah", 1/2 * apris * tapris * tppris)
    if  pilp == "2":
        apris = int(float(input("Masukkan panjang sisi alas prisma: ")))
        tapris = int(float(input("Masukkan tinggi alas prisma: ")))
        tppris = int(float(input("Masukkan tinggi prisma segiempat: ")))
        print ("Volume prisma segiempat tersebut adalah", apris * tapris * tppris)
    if pilp == "3":
        ppris = int(float(input("Masukkan panjang sisi alas prisma: ")))
        tapris = int(float(input("Masukkan tinggi alas prisma: ")))
        tppris = int(float(input("Masukkan tinggi prisma segilima: ")))
        print ("Volume prisma segilima tersebut adalah", (1/2 * 5 * ppris * tapris * tppris))
    else:
        print ("Prisma yang Anda cari belum tersedia di Kalkulator ini")
elif pilihan == "4":
    phi = 3.14
    jker = float(input("Masukkan jari-jari kerucut: "))
    tker = float(input("Masukkan tinggi kerucut: "))
    print ("Volume kerucut tersebut adalah", 1/3 * phi * jker * jker * tker)