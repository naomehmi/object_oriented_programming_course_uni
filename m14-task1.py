from class_k import MahasiswaM14, DosenM14, Attendance, AddStudent, AddDosen, JumlahManusia, PrintAll

data = Attendance()
tambahMhs = AddStudent()
tambahDos = AddDosen()

while True:
    try:
        n = int(input("Ingin input berapa data? : "))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        print("Harus berupa angka di atas 0")

for i in range(n):
    while True:
        try:
            md = input("Ingin input data Mahasiswa/Dosen? : ").lower()
            if md != "mahasiswa" and md != "dosen":
                raise ValueError
            break
        except ValueError:
            print("Hanya boleh input 'mahasiswa' atau 'dosen'.")
    if md == "mahasiswa":
        tambahMhs.tambah(MahasiswaM14(input("NIM : "), input("Nama : ").title().rstrip().lstrip(), input("Jurusan : "), input("Jenis Kelamin : "), input("Email : ")),data)
    else:
       tambahDos.tambah(DosenM14(input("NIP : "), input("Nama : ").title().rstrip().lstrip(), input("Jabatan : "), input("Jenis Kelamin : "), input("Nomor HP : ")),data)

PrintAll().cetak(data)
