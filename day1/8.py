saldo = 100000 
print("=== ATM ===")
print("1. cek saldo")
print("2. Tarik Uang")
print("3. keluar")
pilih = int(input("pilih:"))

while pilih !=3:
    if pilih == 1:
         print("== SALDO:", saldo,"==")
    
    elif pilih == 2:
             penarikan = int(input("jumlah penarikan:"))
             if penarikan <= 0:
               print("Jumlah Penarikan Tidak Valid")
         
             elif penarikan <= saldo:
               saldo -= penarikan
               print("== Penarikan Berhasil! ==")
         
             else:
               print("== Saldo Tidak Cukup ==")

    print("=== ATM ===")
    print("1. cek saldo")
    print("2. Tarik Uang")
    print("3. keluar")

    pilih = int(input("pilih:"))
