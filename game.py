import random

hp = 100
magic = 30
musuh = 5

print("================================")
print("       MAGIC SURVIVAL")
print("================================")
print("Kamu memiliki", hp, "HP")
print("Musuh yang harus dikalahkan:", musuh)

while hp > 0 and musuh > 0:

    print("\n----------------------------")
    print("HP kamu   :", hp)
    print("HP magic  :", magic)
    print("Musuh     :", musuh)
    print("----------------------------")

    print("1. Serang dengan Magic")
    print("2. Heal")
    print("3. Kabur")

    pilih = input("Pilih aksi: ")

    if pilih == "1":

        damage = random.randint(10, magic)

        print("🔮 Kamu menyerang!")
        print("Damage:", damage)

        musuh -= damage

        if musuh <= 0:
            print("\n🔥 SEMUA MUSUH KALAH!")
            print("🏆 KAMU MENANG!")
            break

        serangan_musuh = random.randint(5, 15)
        hp -= serangan_musuh

        print("👾 Musuh menyerang balik!")
        print("Damage:", serangan_musuh)

    elif pilih == "2":

        heal = random.randint(10, 20)
        hp += heal

        if hp > 100:
            hp = 100

        print("💚 Kamu melakukan heal!")
        print("HP bertambah:", heal)

        serangan_musuh = random.randint(5, 15)
        hp -= serangan_musuh

        print("👾 Musuh menyerang saat kamu heal!")
        print("Damage:", serangan_musuh)

    elif pilih == "3":

        print("🏃 Kamu kabur dari pertarungan!")
        break

    else:

        print("❌ Pilihan tidak valid!")

if hp <= 0:
    print("\n💀 HP kamu habis!")
    print("GAME OVER")