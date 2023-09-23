#M-01

class mahasiswa:
    def __init__(self, nama, nim, jenisKel, jurusan, email):
        self.nama = nama
        self.nim = nim
        self.jenisKel = jenisKel
        self.jurusan = jurusan
        self.email = email

    def cetak(self):
        print("| {:<23}{:^1}{:>47} |".format("NIM Mahasiswa",":",self.nim))
        print("| {:<23}{:^1}{:>47} |".format("Nama Mahasiswa",":",self.nama))
        print("| {:<23}{:^1}{:>47} |".format("Jurusan Mahasiwa",":",self.jurusan))
        print("| {:<23}{:^1}{:>47} |".format("Jenis Kelamin Mahasiswa",":",self.jenisKel))
        print("| {:<23}{:^1}{:>47} |".format("Email Mahasiswa",":",self.email))


class dosen:
    def __init__(self, nama, nip, jabatan, jenisKel, noHp):
        self.nama = nama
        self.nip = nip
        self.jabatan = jabatan
        self.jenisKel = jenisKel
        self.noHp = noHp

    def cetak(self):
        print("| {:<23}{:^1}{:>47} |".format("NIP Dosen",":",self.nip))
        print("| {:<23}{:^1}{:>47} |".format("Nama Dosen",":",self.nama))
        print("| {:<23}{:^1}{:>47} |".format("Jabatan Dosen",":",self.jabatan))
        print("| {:<23}{:^1}{:>47} |".format("Jenis Kelamin Dosen",":",self.jenisKel))
        print("| {:<23}{:^1}{:>47} |".format("Nomor HP Dosen",":",self.noHp))

class produk:
    def __init__(self, kode, nama, qty):
        self.kode = kode
        self.nama = nama
        self.qty = qty

class card:
    def __init__(self, nama, tingkatan):
        self.nama = nama
        self.tingkatan = tingkatan
        if self.tingkatan == "TK":
            self.jamPengajaran = "2 jam"
            self.biayaLes = "300.000"
        elif self.tingkatan == "SD":
            self.jamPengajaran = "2 jam"
            self.biayaLes = "500.000"
        elif self.tingkatan == "SMP":
            self.jamPengajaran = "1 jam"
            self.biayaLes = "700.000"
        elif self.tingkatan == "SMA":
            self.jamPengajaran = "1 jam"
            self.biayaLes = "1.000.000"

    def cetak(self):
        print("_"*50)
        print("| {:^46} |".format(" "))
        print("| {:^46} |".format("KARTU SISWA PRIVATE LES KENTANG"))
        print("| {:^46} |".format("="*46))
        print("| {:<15}{:^1}{:>30} |".format("Nama",":",self.nama))
        print("| {:<15}{:^1}{:>30} |".format("Tingkatan",":",self.tingkatan))
        print("| {:<15}{:^1}{:>30} |".format("Jam Pengajaran",":",self.jamPengajaran))
        print("| {:<15}{:^1}{:>30} |".format("Biaya Les",":",self.biayaLes))
        print("| {:^46} |".format(" "))
        print("_"*50)

#M-02

class naomiPrisella_M2:
    def __init__(self, noInduk, nama, jenisKelamin, noHp):
        self.noInduk = noInduk
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.noHp = noHp

class mahasiswa_M2:
    def __init__(self, noInduk, nama, jenisKelamin, noHp, email):
        super().__init__(noInduk, nama, jenisKelamin, noHp)
        self.email = email

    def absensi(self):
        print("Nomor Induk Mahasiswa (NIM) :",self.noInduk)
        print("Nama Mahasiswa :",self.nama)

class dosen_M2:
    def __init__(self, noInduk, nama, jenisKelamin, noHp):
        super().__init__(noInduk, nama, jenisKelamin, noHp)

    def perkenalan(self):
        print("Nama Dosen : ",self.nama)
        print("Nomor HP   :", self.noHp)
