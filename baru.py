barang = ["buku", "pensil", "penghapus", "pulpen"]
harga = [5000, 2000, 3000, 4000]

nama = input("nama kasir: ")

print("=====DAFTAR BARANG=====")
print("1.", barang[0], "     Rp.", harga[0])
print("2.", barang[1], "   Rp.", harga[1])
print("3.", barang[2], "Rp.", harga[2])
print("4.", barang[3], "   Rp.", harga[3])
print("=======================")

pilih = int(input("pilih barang: "))

while pilih:

    if pilih == 1:
        jumlah = int(input("jumlah: "))
        print("=======================")
        print("barang:", barang[0], "Rp.", harga[0], "|", jumlah, "x")

        total = harga[0] * jumlah

        if total >= 30000:
            diskon = total * 10 / 100
            total = total - diskon
            print("total: Rp.", total)
            print("diskon 10%")
        else:
            print("total: Rp.", total)

        break

    elif pilih == 2:
        jumlah = int(input("jumlah: "))
        print("=======================")
        print("barang:", barang[1], "Rp.", harga[1], "|", jumlah, "x")

        total = harga[1] * jumlah

        if total >= 30000:
            diskon = total * 10 / 100
            total = total - diskon
            print("total: Rp.", total)
            print("diskon 10%")
        else:
            print("total: Rp.", total)

        break

    elif pilih == 3:
        jumlah = int(input("jumlah: "))
        print("=======================")
        print("barang:", barang[2], "Rp.", harga[2], "|", jumlah, "x")

        total = harga[2] * jumlah

        if total >= 30000:
            diskon = total * 10 / 100
            total = total - diskon
            print("total: Rp.", total)
            print("diskon 10%")
        else:
            print("total: Rp.", total)

        break

    elif pilih == 4:
        jumlah = int(input("jumlah: "))
        print("=======================")
        print("barang:", barang[3], "Rp.", harga[3], "|", jumlah, "x")

        total = harga[3] * jumlah

        if total >= 30000:
            diskon = total * 10 / 100
            total = total - diskon
            print("total: Rp.", total)
            print("diskon 10%")
        else:
            print("total: Rp.", total)

        break

    else:
        print("barang tidak ditemukan!!")
        break