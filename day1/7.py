saldo = 100000
print("== ATM ==")
print("1. cek saldo")
print("2. Tarik Uang")
pilih = int(input(":"))

if pilih == 1:
   print("== SALDO:",saldo,"==")
   
elif pilih == 2:
   penarikan = int(input("jumlah penarikan:"))

   if penarikan <= 0:
    print("Jumlah Penarikan Tidak Valid")
   elif penarikan <= saldo:
    print("== Penarikan Berhasil! ==")
    print("SISA SALDO:", saldo - penarikan)
   else:
    print("== Saldo Tidak Cukup ==")
  
