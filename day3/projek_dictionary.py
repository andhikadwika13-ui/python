produk = {
    "nama": "Laptop",
    "harga": 7500000,
    "stok": 10,
    "merek": "Lenovo",
    "kategori": "Elektronik"
}

print(produk)

produk.update({"harga":7000000, "garansi":"2 tahun"})
del produk["kategori"]

if "garansi" in produk:
    print("Garansi ada")
else:
    print("ga ada garansi")