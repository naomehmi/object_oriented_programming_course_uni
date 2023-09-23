from class_k import card

kartu = []
choice = ""
while choice != "k":
    out = ""
    print("\nMESIN PENCETAKAN KARTU SISWA PRIVATE LES KENTANG")
    print("="*48)
    print()
    print("Selamat datang ke Private Les Kentang. Ada yang bisa dibantu?")
    print(" > Registrasi Murid Baru (R)")
    print(" > Cetak Kartu (C)")
    print(" > Keluar (K)")
    print("Pilih salah satu (R/C/K)")
    choice = input("=> ").lower()
    if choice == "r":
        while out != "k":
            out = ""
            print("\nRegistrasi")
            print("*"*10)
            print("\nTolong isi data berikut di bawah:\n")
            a = input("Nama Lengkap Siswa : ")
            a = a.title()
            b = ""
            while b != "tk" and b != "sd" and b != "smp" and b != "sma":
                b = input("Tingkatan Siswa (TK/SD/SMP/SMA) : ").lower()
                if b != "tk" and b != "sd" and b != "smp" and b != "sma":
                    print("Jawaban hanya bisa berupa dalam bentuk TK, SD, SMP, atau SMA. Mohon coba lagi.")
            b = b.upper()
            siswaBaru = card(a, b)
            kartu.append(siswaBaru)
            while out != "r" and out != "k": 
                    print("\nTerima kasih telah mendaftar ke Private Les Kentang. Apakah anda ingin kembali ke menu utama atau registrasi siswa lain?")
                    print(" > Registrasi siswa lain (R)")
                    print(" > Kembali ke menu utama (K)")
                    print("Pilih salah satu (R/K)")
                    out = input("=> ").lower()
                    if out != "r" and out != "k":
                        print("Jawaban hanya bisa berupa dalam bentuk R atau K. Mohon coba lagi.")
    elif choice == "c":
        if kartu == []:
            print("\nBelum ada data yang di-input, jadi pencetakan kartu tidak dapat dilakukan. Mohon registrasi dulu.")
        else:
            while out != "k":
                out = ""
                print("\nCetak Kartu")
                print("*"*11)
                print("\nKartu siswa mana yang ingin dicetak? Input nomor siswa yang tertera di bawah.\n")
                for i in range(len(kartu)):
                    print(f"{i+1}. {kartu[i].nama}")
                no = 0
                print()
                while no < 1 or no > len(kartu):
                    no = int(input("=> "))
                    if 1 <= no <= len(kartu):
                        kartu[no - 1].cetak()
                    else:
                        print("Tidak ada siswa dengan nomor tersebut. Mohon coba lagi.")
                while out != "c" and out != "k": 
                    print("\nApakah anda ingin kembali ke menu utama atau cetak kartu siswa lain?")
                    print(" > Cetak lagi (C)")
                    print(" > Kembali ke menu utama (K)")
                    print("Pilih salah satu (C/K)")
                    out = input("=> ").lower()
                    if out != "c" and out != "k":
                        print("Jawaban hanya bisa berupa dalam bentuk C atau K. Mohon coba lagi.")  
    elif choice == "k":
        print("Terima kasih telah menggunakan mesin pencetakan kartu siswa private les kentang.")
    else:
        print("Jawaban hanya bisa berupa dalam bentuk R, C, dan K. Mohon coba lagi.")
