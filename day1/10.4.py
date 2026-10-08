def total(harga, jumlah):
    return (harga*jumlah) 

hasil = total(5000, 3) 
pajak = hasil * 10/100
subtotal = hasil + pajak
print(subtotal)
