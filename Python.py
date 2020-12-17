#SISTEM INFORMASI BANK SAMPAH DESA KUNCEN, KELURAHAN BUBAKAN, KECAMATAN MIJEN, KOTA SEMARANG
#Mareta Mahliyasmita
#UTS Algoritma


def harga_sampah():
    berat_sampah = int(input("Masukkan berat sampah anda : "))
    pilihan = 1
    while pilihan !=0:
        print()
        print("Pilih jenis sampah yang Anda inginkan")
        print("1, sampah plastik")
        print("2, sampah kertas")
        print("3, sampah besi")
        print("4, sampah botol")
        print("5, sampah elektronik")
        print("6, sampah karet")
        
        pilihan = int(input("Masukkan jenis sampah yang Anda inginkan : "))
        if pilihan==1:
            harga_sampah = berat_sampah * 500
            print()
            print("harga sampah  : ", harga_sampah)
            print()
        elif pilihan==2:
            harga_sampah = berat_sampah * 2000
            print()
            print("harga sampah : ", harga_sampah)
            print()
        elif pilihan==3:
            harga_sampah = berat_sampah * 3000
            print()
            print("harga sampah : ", harga_sampah)
            print()
        elif pilihan==4:
            harga_sampah = berat_sampah * 5500
            print()
            print("harga sampah : ", harga_sampah)
            print()
        elif pilihan==5:
            harga_sampah = berat_sampah * 10000
            print()
            print("harga sampah : ", harga_sampah)
            print()
        elif pilihan==6:
            harga_sampah = berat_sampah * 15000
            print()
            print("harga sampah : ", harga_sampah)
            print()

pilihan = 1
while pilihan !=0:
    print()
    print("====================SELAMAT DATANG DI PROGRAM BANK SAMPAH KUNCEN====================")
    print("1. Pengelola/Admin")
    print("2. Nasabah")
    print("3. Keluar")
    print()
    pilihan = int(input("Masukkan Nomor Pilihan Anda : "))
    if pilihan==1:
        print("harga sampah plastik : 500")
        print("harga sampah kertas : 2000")
        print("harga sampah besi : 3000")
        print("harga sampah botol : 5500")
        print("harga sampah elektronik : 10000")
        print("harga sampah karet : 15000")
    
    elif pilihan==2:
        harga_sampah()
