from class_k import Murid

listMurid = []

while True:
    print("Mesin Pencetakan Kartu Private Les")
    print("="*34)
    print("\n1. Daftar Murid Baru")
    print("2. Cetak Kartu")
    print("3. Keluar")

    while True:
        try:
            pil = int(input("Pilih salah satu : "))
            if pil > 3 or pil < 1:
                raise ValueError("\nInput hanya boleh '1', '2', atau '3'. Mohon coba lagi\n")
            break
        except ValueError as e:
            print(str(e))

    if pil == 1:
        a = input("\nMasukkan Nama Siswa\t\t\t: ").title().lstrip().rstrip()
        b = input("Masukkan Jenis Kelamin Siswa (L/P)\t: ").upper().lstrip().rstrip()
        c = input("Tingkatan Siswa (SD/SMP/SMA)\t\t: ").upper().lstrip().rstrip()
        try:
            murid = Murid(a,b,c)
            temp = murid.nama
            listMurid.append(murid)
        except AttributeError:
            print("\nBalik ke menu utama...\n")

    elif pil == 2:
        if listMurid:
            print("\nMasukkan nomor murid yang ingin dicetak kartunya: ")
            j = 1
            for i in listMurid:
                print(str(j)+".", i.nama)
                j += 1
            print()
            while True:
                try:
                    pil2 = int(input("Nomor: "))
                    if pil2 < 1 or pil2 > len(listMurid):
                        raise ValueError
                    break
                except ValueError:
                    print("Tidak ada siswa dengan nomor itu. Coba lagi")
            listMurid[pil2 - 1].cetakKartu()
            print()
        else:
            print("\nBelum ada siswa yang terdaftar. Daftar dulu.\n")

    else:
        break
