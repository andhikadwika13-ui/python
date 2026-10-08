produk = {
    "nama": "Laptop",
    "harga": 7500000,
    "stok": 10,
    "merek": "Lenovo"
}
produk.update({"kategori":"Elektronik", "stok":15, })

print(produk.keys())
print(produk.values())

if "garansi" in produk:
    print("Ada garansi")
else:
    print("Tidak ada garansi")

print(len(produk))