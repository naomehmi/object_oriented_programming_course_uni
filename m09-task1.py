from class_k import NaomiPrisellaM9, MahasiswaM9, DosenM9, AbsensiM9

data = AbsensiM9()

while True:
    try:
        n = int(input("Ingin input berapa data? : "))
        if n < 0:
            raise ValueError
        break
    except ValueError:
        print("Harus input angka di atas 0")

for i in range(n):
    while True:
        try:
            md = input("Ingin input data Mahasiswa/Dosen? : ").lower()
            if md != "mahasiswa" and md != "dosen":
                raise ValueError
            break
        except ValueError:
            print("Hanya menerima input 'mahasiswa' atau 'dosen'")
    if md == "mahasiswa":
        while True:
            try:
                org = MahasiswaM9(NaomiPrisellaM9(input("Nomor Induk Mahasiswa : ").lstrip().rstrip(), input("Nama Mahasiswa : ").lstrip().rstrip().title(), input("Jenis Kelamin Mahasiswa (L/P) : ").lstrip().rstrip().upper()))
                temp1 = org.wrapper.nama
                org.detail(input("Jurusan Mahasiswa (IF/TI/SI/AK/MN) : ").lstrip().rstrip().upper(), input("Email Mahasiswa : ").lstrip().rstrip().lower())
                temp2 = org.wrapper.jurusan
                break
            except AttributeError as e:
                print("Terdapat kesalahan input data. Coba ulangi.\n")
                pass
    else:
        while True:
            try:
                org = DosenM9(NaomiPrisellaM9(input("Nomor Induk Pegawai : ").lstrip().rstrip(), input("Nama Dosen : ").lstrip().rstrip().title(), input("Jenis Kelamin Dosen (L/P) : ").lstrip().rstrip().upper()))
                temp1 = org.wrapper.nama
                org.detail(input("Jabatan Dosen : ").lstrip().rstrip(), input("Nomor HP Dosen : ").lstrip().rstrip())
                temp2 = org.wrapper.jabatan
                break
            except AttributeError:
                print("Terdapat kesalahan input data. Coba ulangi.\n")
                pass
    data.hadir(org)
    print()

data.cetak()
