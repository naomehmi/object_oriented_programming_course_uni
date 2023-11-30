from class_k import NaomiPrisellaM10, HadirAcaraM10

data = NaomiPrisellaM10()
md = None

while True:
    try:
        print("Absensi Acara Coolyeah")
        print("="*22 + "\n")
        print("1. Input data")
        print("2. Cetak Rekap Absensi")
        print("3. Cari Data")
        print("4. Keluar\n")

        pil = int(input("Pilih salah satu (1/2/3/4) : "))

        if pil < 1 or pil > 4:
            raise ValueError
        
        if pil == 1:
            n = int(input("Ingin input berapa data? : "))

            for i in range(n):
                print("\nORANG KE-" + str(i+1) + "\n")
                
                while True:
                    try:
                        md = input("Ingin input data Mahasiswa / Dosen ? : ").capitalize()
                        if md not in ["Mahasiswa", "Dosen"]:
                            raise ValueError
                        break
                    except ValueError:
                        print("Input 'mahasiswa' atau 'dosen'")

                if md == "Mahasiswa":
                    while True:
                        try:
                            a = input("NIM Mahasiswa : ").lstrip().rstrip()
                            b = input("Nama Mahasiswa : ").lstrip().rstrip().title()
                            c = input("Jurusan Mahasiswa (IF/SI/TI/AK/MN) : ").upper().lstrip().rstrip()
                            d = input("Jenis Kelamin Mahasiswa (L/P) : ").lstrip().rstrip().upper()
                            e = input("Email Mahasiswa : ").lstrip().rstrip()

                            if len(a) != 9 or not a.isnumeric(): raise ValueError("NIM hanya boleh terdiri dari angka dan memiliki panjang 9 karakter")

                            tmp = b.split()

                            for t in tmp:
                                if not t.isalpha(): raise ValueError("Nama hanya boleh terdiri dari huruf dan spasi")

                            if c not in ["IF", "SI", "TI", "AK", "MN"]: raise ValueError("Jurusan hanya ada 'IF', 'SI', 'TI', 'AK', dan 'MN'")

                            c = "Teknik Informatika" if c == "IF" else "Sistem Informasi" if c == "SI" else "Teknologi Informasi" if c == "TI" else "Akuntansi" if c == "AK" else "Manajemen"

                            if d not in ["P", "L"]: raise ValueError("Jenis kelamin hanya boleh 'P' atau 'L'")

                            d = "Perempuan" if d == "P" else "Laki-laki"

                            if "@students.mikroskil.ac.id" not in e or e[:9] != a: raise ValueError("Format email mahasiswa adalah [NIM]@students.mikroskil.ac.id")

                            mhs = HadirAcaraM10(md, NIM = a, Nama = b, Jurusan = c , JenisKelamin = d, Email = e)

                            break

                        except ValueError as e:
                            print(str(e)+". Coba lagi\n")
                else:
                    while True:
                        try:
                            a = input("NIP Dosen : ").lstrip().rstrip()
                            b = input("Nama Dosen : ").lstrip().rstrip().title()
                            c = input("Jabatan Dosen : ").upper().lstrip().rstrip()
                            d = input("Jenis Kelamin Dosen (L/P) : ").lstrip().rstrip().upper()
                            e = input("Nomor Telp Dosen : ").lstrip().rstrip()

                            if len(a) != 9 or not a.isnumeric(): raise ValueError("NIP hanya boleh terdiri dari angka dan memiliki panjang 9 karakter")

                            tmp = b.split()

                            for t in tmp:
                                if not t.isalpha(): raise ValueError("Nama hanya boleh terdiri dari huruf dan spasi")

                            if d.upper() not in ["P", "L"]: raise ValueError("Jenis kelamin hanya boleh 'P' atau 'L'")
                            d = "Perempuan" if d == "P" else "Laki-laki"

                            if e[0] != "+" or not e[1:].isnumeric() or len(e) < 8 or len(e) > 15: raise ValueError("Nomor Telepon harus ada '+' di awal dan terdiri dari 8-15 angka")

                            dos = HadirAcaraM10(md, NIP = a, Nama = b, Jabatan = c, JenisKelamin = d, NoHP = e) 

                            break

                        except ValueError as e:
                            print(str(e)+". Coba lagi\n")


        elif pil == 2:
            mhs.cetakAbsensi() if md == "Mahasiswa" else dos.cetakAbsensi() if md == "Dosen" else print("Belum ada data yang terisi.")

        elif pil == 3:
            while True:
                try:
                    print()
                    tipe = input("Mau cari Mahasiswa atau Dosen? : ").capitalize()
                    if tipe not in ["Mahasiswa", "Dosen"]:
                        raise ValueError("Input 'Mahasiswa' atau 'Dosen'")
                    nama = input("Input nama orang yang ingin dicari : ").lstrip().rstrip().title()

                    mhs.cariAtauCekData(nama, tipe) if md == "Mahasiswa" else dos.cariAtauCekData(nama, tipe) if md == "Dosen" else print("Belum ada data yang terisi.")

                    break

                except ValueError as e:
                    print(str(e))

        else: break

        print()

    except ValueError:
        print("Tolong input 1, 2, 3, atau 4")
