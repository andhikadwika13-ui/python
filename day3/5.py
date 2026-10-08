siswa = {
        "nama": "Andhika",
        "umur": 16,
        "kelas": "XI",
        "sekolah": "SMK"
}
siswa.update({"umur":17, "kelas":"XII", "jurusan":"RPL", "hobi":"Dengar Musik", "status":"Siswa"})
del siswa["hobi"]
del siswa["status"]

umur = siswa.pop("umur")

print("Nama   :", siswa["nama"] )
print("Umur   :", umur)
print("Kelas  :", siswa["kelas"] )
print("Sekolah:", siswa["sekolah"] )
print("jurusan:", siswa["jurusan"] )