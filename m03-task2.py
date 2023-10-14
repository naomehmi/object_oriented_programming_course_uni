from class_k import Coconut, Banana, MuridSD, MuridSMP, MuridSMA

listKelas = ["SD", "SMP","SMA"]
listMurid = []
c = ""
while c != 3:
    print("Pilih salah satu")
    print("1. Input Data Murid baru")
    print("2. Cetak Data Murid")
    print("3. Keluar")
    c = int(input("Pilih (1/2/3) : "))
    if c == 1:
        print()
        pil = ""
        while pil not in listKelas:
            pil = input("Kelas Murid (SD/SMP/SMA) : ").upper()
            if pil not in listKelas:
                print("Input yang terima hanya berupa 'SD', 'SMP', dan 'SMA'. Coba lagi.")
        if pil == "SD":
            a = input("Nama siswa : ")
            b = input("Nomor HP orang tua : ")
            c = ""
            while c not in ["P","L"]:
                c = input("Jenis Kelamin siswa (L/P): ").upper()
                if c not in ["P","L"]:
                    print("Input hanya terima 'L' atau 'P'.Coba lagi")
            listMurid.append(MuridSD(a,b,c))
        elif pil == "SMP":
            a = input("Nama siswa : ")
            b = input("Nomor HP orang tua : ")
            c = input("Umur siswa : ")
            listMurid.append(MuridSMP(a,b,c))
        else:
            a = input("Nama siswa : ")
            b = input("Nomor HP orang tua : ")
            c = None
            while c != "IPA" and c != "IPS":
                c = input("Kelas siswa (IPA/IPS) : ").upper()
                if c != "IPA" and c != "IPS":
                    print("Input hanya menerima 'IPA' atau 'IPS'. Coba lagi.")
            listMurid.append(MuridSMA(a,b,c))
    elif c == 2:
        if len(listMurid) > 0:
            print("\nData Siswa:")
            for i in range(len(listMurid)):
                print(f"{i+1}. {listMurid[i].nama}")
            print()
            pil = 0
            while pil <= 0 or pil >= len(listMurid) + 1:
                pil = int(input(f"Cetak data siswa nomor berapa? (1-{len(listMurid)}): "))
                if pil <= 0 or pil >= len(listMurid) + 1:
                    print("Tidak ada murid dengan nomor itu. Mohon coba lagi.")
            print()
            listMurid[pil-1].cetakData()
        else:
            print("Belum ada data murid.")
    elif c != 3:
        print("Input hanya terima '1','2', atau '3'. Coba lagi.")
    print()
