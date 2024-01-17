from class_k import MahasiswaM15, DosenM15, KumpulanDosen, KumpulanMahasiswa, AbsensiManager

data = AbsensiManager(KumpulanDosen, KumpulanMahasiswa)

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
        data.tambah(MahasiswaM15(input("NIM : "), input("Nama : "), input("Jenis Kelamin : "), input("Jurusan : "), input("Email : ")))
    else:
        data.tambah(DosenM15(input("NIP : "), input("Nama : "), input("Jenis Kelamin : "), input("Jabatan : "), input("NoHp : ")))

data.printSelf()
