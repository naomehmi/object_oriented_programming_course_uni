from class_k import NaomiPrisellaM7_1

data = NaomiPrisellaM7_1()

pil1 = None

while True:
    try:
        print("Menu Utama")
        print("==========\n")
        print("1. Input absensi mahasiswa baru")
        print("2. Tampil data mahasiswa")
        print("3. Cari mahasiswa")
        print("4. Keluar\n")

        pil1 = int(input("Pilih salah satu (1/2/3) : "))

        if pil1 < 1 or pil1 > 4:
            raise ValueError

        print()

    except ValueError:
        print("\nInput angka 1, 2, atau 3.\n")

    if pil1 == 1:
        pil2 = 'y'

        while pil2 == 'y':
            a = data.absensi()
            next(a)
            x = input("NIM Mahasiswa : ").lstrip().rstrip()
            y = input("Nama Mahasiswa : ").title().lstrip().rstrip()
            z = input("Nomor HP Mahasiswa : ").lstrip().rstrip()
            print()
            if not data.validasi(x,y,z):
                continue
            print("Berhasil diinput")
            a.send(x)
            a.send(y)
            a.send(z)
            print("\nJumlah mahasiswa yang telah absensi : ", len(data.mahasiswa),"\n")

            while True:
                try:
                    pil2 = input("Apakah masih mau input mahasiswa? (Y/N) : ").lower()

                    if pil2 != 'y' and pil2 != 'n':
                        raise ValueError("Jawaban hanya boleh berupa 'y' atau 'n'")

                    break

                except ValueError as e:
                    print(str(e))

    elif pil1 == 2:
        if not data.mahasiswa:
            print("Data masih kosong. Input dulu")
        else:
            print("Berikut data yang telah diurutkan : \n")
            data.cetakData()

    elif pil1 == 3:
        cari = input("NIM Mahasiswa yang ingin dicari: ")
        data.pencarianData(cari)

    elif pil1 == 4:
        break

    print()
