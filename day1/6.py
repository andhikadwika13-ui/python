usn = (input("username:"))
pw = (input("password:"))

if usn == "admin" and pw == "12345":
    print ("LOGIN BERHASIL!!")
    print("selamat datang admin")
elif usn != "admin" or pw != "12345":
    if usn == "admin" and pw != "12345":
     print("username benar, password salah")
    elif usn != "admin":
     print ("username tidak ditemukan")