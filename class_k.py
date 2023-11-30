import abc

# M01

class mahasiswa:
    def __init__(self,nama,nim,jenisKel,jurusan,email):
        self.nama = nama
        self.nim = nim
        if jenisKel == "l":
            self.jenisKel = "Laki-laki"
        else:
            self.jenisKel = "Perempuan"
        if jurusan == "if":
            self.jurusan = "Teknik Informatika"
        elif jurusan == "si":
            self.jurusan = "Sistem Informasi"
        elif jurusan == "ti":
            self.jurusan = "Teknologi Informasi"
        elif jurusan == "mn":
            self.jurusan = "Manajemen"
        elif jurusan == "ak":
            self.jurusan = "Akuntansi"
        self.email = email

    def cetak(self):
        print("| {:<23}:{:>32} |".format("NIM Mahasiswa",self.nim))
        print("| {:<23}:{:>32} |".format("Nama Mahasiswa",self.nama))
        print("| {:<23}:{:>32} |".format("Jurusan Mahasiswa",self.jurusan))
        print("| {:<23}:{:>32} |".format("Jenis Kelamin Mahasiswa",self.jenisKel))
        print("| {:<23}:{:>32} |".format("Email Mahasiswa",self.email))
        
class dosen:
    def __init__(self, nama, nip, jabatan, jenisKel, noHp):
        self.nama = nama
        self.nip = nip
        self.jabatan = jabatan
        if jenisKel == "l":
            self.jenisKel = "Laki-laki"
        else:
            self.jenisKel = "Perempuan"
        self.noHp = noHp

    def cetak(self):
        print("| {:<23}:{:>32} |".format("NIP Dosen",self.nip))
        print("| {:<23}:{:>32} |".format("Nama Dosen",self.nama))
        print("| {:<23}:{:>32} |".format("Jaatan Dosen",self.jabatan))
        print("| {:<23}:{:>32} |".format("Jenis Kelamin Dosen",self.jenisKel))
        print("| {:<23}:{:>32} |".format("Nomor HP Dosen",self.noHp))

class produk:
    def __init__(self, kode, nama, qty):
        self.kode = kode
        self.nama = nama
        self.qty = qty

class card:
    def __init__(self,nama,tingkatan):
        self.nama = nama
        self.tingkatan = tingkatan
        if self.tingkatan == "TK":
            self.jamPengajaran = "2 jam"
            self.biayaLes = "Rp. 300.000"
        elif self.tingkatan == "SD":
            self.jamPengajaran = "2 jam"
            self.biayaLes = "Rp. 500.000"
        elif self.tingkatan == "SMP":
            self.jamPengajaran = "1 jam"
            self.biayaLes = "Rp. 700.000"
        elif self.tingkatan == "SMA":
            self.jamPengajaran = "1 jam"
            self.biayaLes = "Rp. 1.000.000"
    def cetak(self):
        print("_"*50)
        print("| {:<46} |".format(" "))
        print("| {:<46} |".format("KARTU TANDA SISWA PRIVATE LES KENTANG"))
        print("| {:<46} |".format("="*46))
        print("| {:<15}:{:>30} |".format("Nama Siswa", self.nama))
        print("| {:<15}:{:>30} |".format("Tingkatan", self.tingkatan))
        print("| {:<15}:{:>30} |".format("Jam Pengajaran", self.jamPengajaran))
        print("| {:<15}:{:>30} |".format("Biaya Les", self.biayaLes))
        print("| {:<46} |".format(" "))
        print("_"*50)

# M02

class NaomiPrisella:
    def __init__(self, noInduk, nama, jenisKelamin, noHp):
        self.noInduk = noInduk
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.noHp = noHp

class mahasiswa_m2(NaomiPrisella):
    def __init__(self, noInduk, nama, jenisKelamin, noHp):
        super().__init__(noInduk, nama, jenisKelamin, noHp)
    def absensi(self):
        print("| {:<30}:{:>40} |".format("NIM",self.noInduk))
        print("| {:<30}:{:>40} |".format("Nama Mahasiswa",self.nama))

class dosen_m2(NaomiPrisella):
    def __init__(self, noInduk, nama, jenisKelamin, noHp):
        super().__init__(noInduk, nama, jenisKelamin, noHp)
    def perkenalan(self):
        print("| {:<30}:{:>40} |".format("Nama Dosen",self.nama))
        print("| {:<30}:{:>40} |".format("Nomor HP Dosen",self.noHp))

class RyanRussell:
    def __init__(self, kode, nama, qty):
        self.kode = kode
        self.nama = nama
        self.qty = qty
        self.props = [self.kode, self.nama, self.qty]
        self.traits = ["Kode Produk", "Nama Produk", "Qty Produk"]
    def laporan(self):
        for i in range(len(self.props)):
            print("| {:<28} : {:>40} |".format(self.traits[i],self.props[i]))
        print("-"*75)

class handSanitizer(RyanRussell):
    def __init__(self, kode, qty, mili):
        super().__init__(kode, "Hand Sanitizer", qty)
        self.mili = mili
        self.props.append(mili)
        self.traits.append("Isi Produk (ml)")

class buahBuahan(RyanRussell):
    def __init__(self, kode, qty, asal):
        super().__init__(kode, "Buah-buahan", qty)
        self.asal = asal
        self.props.append(asal)
        self.traits.append("Asal Produk")

class banMobil(RyanRussell):
    def __init__(self, kode, qty, diameter):
        super().__init__(kode, "Ban Mobil", qty)
        self.diameter = diameter
        self.props.append(self.diameter)
        self.traits.append("Diameter Produk (cm)")

class botolMinumBayi(RyanRussell):
    def __init__(self, kode, qty, mili):
        super().__init__(kode, "Botol Minum Bayi", qty)
        self.mili = mili
        self.props.append(mili)
        self.traits.append("Isi Produk (ml)")

# M03

class AyamGoreng(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def nama(self):
        pass
    @abc.abstractproperty
    def noInduk(self):
        pass
    @abc.abstractmethod
    def absensi(self):
        pass

class ManusiaMikroskil:
    def __init__(self,nama,noInduk):
        self.nama = nama
        self.noInduk = noInduk

class Mahasiswa_m3(AyamGoreng, ManusiaMikroskil):
    nama = ""
    noInduk = ""
    def __init__(self,nama,noInduk):
        super().__init__(nama,noInduk)
    def absensi(self):
        print("Terima kasih sudah hadir.")

class Dosen_m3(AyamGoreng, ManusiaMikroskil):
    nama = ""
    noInduk = ""
    def __init__(self,nama,noInduk):
        super().__init__(nama,noInduk)
    def absensi(self):
        print("Silahkan mulai pelajaran.")

class Coconut(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def nama(self):
        pass
    @abc.abstractproperty
    def noHpOrtu(self):
        pass
    @abc.abstractproperty
    def biayaLes(self):
        pass
    @abc.abstractmethod
    def cetakData(self):
        pass

class Banana:
    def __init__(self,nama,noHpOrtu,biayaLes):
        self.nama = nama
        self.noHpOrtu = noHpOrtu
        self.biayaLes = biayaLes
        self.data = [self.nama, self.noHpOrtu, self.biayaLes]
        self.prompt = ["Nama","No HP Orang tua", "Biaya Les"]

class MuridSD(Coconut, Banana):
    nama = ""
    noHpOrtu = ""
    biayaLes = 0
    def __init__(self,nama,noHpOrtu,jenisKelamin):
        super().__init__(nama,noHpOrtu,500000)
        self.jenisKelamin = jenisKelamin
        self.data.append(self.jenisKelamin)
        self.prompt.append("Jenis Kelamin")
    def cetakData(self):
        for i in range(len(self.data)):
            print("{:<20}:{:>15}".format(self.prompt[i],self.data[i]))

class MuridSMP(Coconut, Banana):
    nama = ""
    noHpOrtu = ""
    biayaLes = 0
    def __init__(self,nama,noHpOrtu,umur):
        super().__init__(nama,noHpOrtu,800000)
        self.umur = umur
        self.data.append(self.umur)
        self.prompt.append("Umur")
    def cetakData(self):
        for i in range(len(self.data)):
            print("{:<20}:{:>15}".format(self.prompt[i],self.data[i]))

class MuridSMA(Coconut, Banana):
    nama = ""
    noHpOrtu = ""
    biayaLes = ""
    def __init__(self,nama,noHpOrtu, kelas):
        super().__init__(nama,noHpOrtu, 1200000)
        self.kelas = kelas
        self.data.append(self.kelas)
        self.prompt.append("kelas")
    def cetakData(self):
        for i in range(len(self.data)):
            print("{:<20}:{:>15}".format(self.prompt[i],self.data[i]))


#M04

class Parent:
    def __init__(self, kode, nama, noHp):
        if(self.cekKode(kode) and self.cekNama(nama) and self.cekNoHp(noHp)):
            nama = " ".join(nama.split())
            self.kode = kode
            self.nama = nama
            self.noHp = noHp
            print("\nData berhasil diinput.")

    def cekKode(self, kode):
        try:
            if not kode.isnumeric():
                raise ValueError("Kode harus terdiri dari angka")
            if len(kode) != 9:
                raise ValueError("Kode harus memiliki panjang 9 karakter")
            return True
        except ValueError as e:
            print(str(e))

    def cekNama(self, nama):
        try:
            nama = nama.split()
            for i in nama:
                if not i.isalpha():
                    raise ValueError("Nama hanya boleh terdiri dari huruf dan spasi")
            return True
        except ValueError as e:
            print(str(e))

    def cekNoHp(self, noHp):
        try:
            if noHp[0] != "+":
                raise ValueError("No HP harus ada tanda '+' di awal")
            if not noHp[1:].isnumeric():
                raise ValueError("No HP hanya boleh terdiri dari angka")
            if len(noHp) < 8 or len(noHp) > 15:
                raise ValueError("No HP hanya boleh 8 sampai 15 karakter")            
            return True
        except ValueError as e:
            print(str(e))

    def cetak():
        pass

class DosenM4(Parent):
    def __init__(self, nip, nama, noHp):
        super().__init__(nip, nama, noHp)
    def cetak(self):
        print("NIP Dosen :",self.kode)
        print("Nama Dosen :",self.nama)
        print("No HP Dosen :",self.noHp)


class MahasiswaM4(Parent):
    def __init__(self, nim, nama, noHp):
        super().__init__(nim, nama, noHp)
    def cetak(self):
        print("NIM Mahasiswa :",self.kode)
        print("Nama Mahasiswa :",self.nama)
        print("No HP Mahasiswa :",self.noHp)
        
class Murid:
    def __init__(self, nama, jenisKel, tingkatan):
        if(self.cekNama(nama) and self.cekJenisKel(jenisKel) and self.cekTingkatan(tingkatan)):
            nama = " ".join(nama.split())
            biaya = ["300.000", "500.000", "700.000", "1.000.000"]
            jam = ["2", "2", "1", "1"]
            tingkat = ["SD", "SMP", "SMA"]
            if jenisKel == "L":
                jenisKel = "Laki-laki"
            else:
                jenisKel = "Perempuan"

            self.nama = nama
            self.jenisKel = jenisKel
            self.tingkatan = tingkatan
            self.jamPengajaran = jam[tingkat.index(self.tingkatan)]
            self.biayaLes = biaya[tingkat.index(self.tingkatan)]

            print("\nData Siswa berhasil diinpput.\n")

    def cekNama(self, nama):
        try:
            nama = nama.split()
            for i in nama:
                if not i.isalpha():
                    raise ValueError("Nama hanya boleh terdiri dari huruf dan spasi")
            return True
        except ValueError as e:
            print(str(e))

    def cekJenisKel(self, jenisKel):
        try:
            if jenisKel not in ["P", "L"]:
                raise ValueError("Jenis Kelamin hanya boleh 'P' atau 'L'")
            return True
        except ValueError as e:
            print(str(e))

    def cekTingkatan(self,tingkatan):
        try:
            if tingkatan not in ["SD", "SMP", "SMA"]:
                raise ValueError("Tingkatan hanya boleh 'SD', 'SMP', dan 'SMA', mohon coba lagi.")
            return True
        except ValueError as e:
            print(str(e))

    def cetakKartu(self):
        teks = {
            "Nama Siswa" : self.nama,
            "Jenis Kelamin" : self.jenisKel,
            "Tingkatan" : self.tingkatan,
            "Jam Pengajaran" : self.jamPengajaran + " jam",
            "Biaya Les" : "Rp. " + self.biayaLes
        }
        print("="*40)
        for x,y in teks.items():
            print("| {:<15}:{:>20} |".format(x,y))
        print("-"*40)

# M05

class MahasiswaM5:
    def __init__(self, nim, nama, noHp):
        if(self.ceknim(nim) and self.cekNama(nama) and self.cekNoHp(noHp)):
            nama = " ".join(nama.split())
            self.nim = nim
            self.nama = nama
            self.noHp = noHp
            print("\nInput data berhasil.")
        else:
            print("Ada kesalahan input. Coba lagi.")

    def ceknim(self, nim):
        try:
            if not nim.isnumeric():
                raise ValueError("NIM harus terdiri dari angka")
            if len(nim) != 9:
                raise ValueError("NIM harus memiliki panjang 9 karakter")
            return True
        except ValueError as e:
            print(str(e))

    def cekNama(self, nama):
        try:
            if nama.isspace() or nama == "":
                raise ValueError
            nama = nama.split()
            for i in nama:
                if not i.isalpha():
                    raise ValueError
            return True
        except ValueError:
            print(("Nama hanya boleh terdiri dari huruf dan spasi"))

    def cekNoHp(self, noHp):
        try:
            if noHp[0] != "+":
                raise ValueError("No HP harus ada tanda '+' di awal")
            if not noHp[1:].isnumeric():
                raise ValueError("No HP hanya boleh terdiri dari angka")
            if len(noHp) < 8 or len(noHp) > 15:
                raise ValueError("No HP hanya boleh 8 sampai 15 karakter")            
            return True
        except ValueError as e:
            print(str(e))

class NaomiPrisellaM5_1:
    def __init__(self):
        self.isi = []
    
    def pemasukanData(self, n):
        for i in range(n):
            while True:
                print("\nMahasiswa ke-"+str(i+1))
                print("="*(13+len(str(i))))
                print()
                a = input("Masukkan NIM Mahasiswa\t\t: ")
                b = input("Masukkan Nama Mahasiswa\t\t: ").title().lstrip().rstrip()
                c = input("Masukkan Nomor HP Mahasiswa\t: ")
                try:
                    temp1 = MahasiswaM5(a, b, c)
                    temp2 = temp1.nama
                    self.isi.append(temp1)
                    break
                except AttributeError:
                    pass

    def absensi(self, item):
        idx = 1
        for i in self.isi:
            if i.nim == item:
                print("Mahasiswa tersebut ditemukan pada posisi",idx)
                return
            idx += 1
        print("Mahasiswa tersebut tidak ditemukan")

class ProdukM5:
    def __init__(self, kode, nama, stok):
        if self.cekStok(stok):
            self.kode = kode
            self.nama = nama
            self.stok = int(stok)
            print("\nProduk berhasil diinput\n")
    
    def cekStok(self,stok):
        try:
            n = int(stok)
            if n < 0:
                raise ValueError
            return True
        except ValueError:
            print("\nJumlah stok harus berupa angka di atas 0. Coba lagi.\n")
            return False

class NaomiPrisellaM5_2:
    def __init__(self):
        self.isi = []
    
    def pemasukanData(self, iterable):
        for item in iterable:
            while True:
                try:
                    temp1 = ProdukM5(item[0], item[1], input(f"Masukkan jumlah stok item {item[0]} ({item[1]}) bulan ini : "))
                    temp2 = temp1.nama
                    self.isi.append(temp1)
                    break
                except AttributeError:
                    pass
    
    def pencarianStok(self, cari):
        produk = iter(self.isi)
        while True:
            try:
                temp = next(produk)
                if temp.nama.lower() == cari or temp.kode.lower() == cari:
                    print(f"\nSisa stok {temp.nama} bulan ini:",temp.stok)
                    if temp.stok < 10:
                        print("Sudah mau habis. Segera restock.")
                    else:
                        print("Masih banyak sisa produk ini.")
                    break
            except StopIteration:
                print("Tidak ada produk dengan nama tersebut.")
                break            

# M06

class NaomiPrisellaM6_1:
    mahasiswa = []

    def inputData(self, nim, nama, noHp):
        try:
            if len(nim) != 9 or not nim.isnumeric():
                raise ValueError("NIM harus terdiri dari angka dan memiliki 9 karakter")
            if len(self.mahasiswa) > 0 and nim in [i["NIM"] for i in self.mahasiswa]:
                raise ValueError("NIM tersebut sudah pernah diinput")
            if nama == "":
                raise ValueError("Nama hanya boleh terdiri dari huruf dan spasi")
            nama = nama.split()
            for i in nama:
                if not i.isalpha():
                    raise ValueError("Nama hanya boleh terdiri dari huruf dan spasi")
            nama = " ".join(nama)
            if len(noHp) > 15 and len(noHp) < 8:
                raise ValueError("Nomor HP harus memiliki 8 - 15 karakter")
            if noHp[0] != '+':
                raise ValueError("Nomor HP harus dimulai dari '+'")
            if not noHp[1:].isnumeric():
                raise ValueError("Nomor HP hanya boleh terdiri dari angka")
            self.mahasiswa.append({
                "NIM" : nim,
                "Nama" : nama,
                "Nomor HP" : noHp
            })
            print("\nData berhasil diinput :D\n")
            return True
        except ValueError as e:
            print()
            print(str(e))
            print("Input ulang lagi.\n")
            return False
    
    def cetakData(self):
        idx = 1
        self.urutkanData()
        for i in self.mahasiswa:
            print("Mahasiswa ke-"+str(idx))
            for x,y in i.items():
                print(x,":",y)
            print()
            idx += 1

    def urutkanData(self):
        self.mahasiswa = sorted(self.mahasiswa, key = lambda x : x["NIM"])

    def pencarianData(self, cari):
        for i in self.mahasiswa:
            if cari == i["NIM"]:
                print("\nDitemukan!")
                for x,y in i.items():
                    print(x,":",y)
                return
        print("\nMahasiswa dengan NIM tersebut tidak ada di database")

class NaomiPrisellaM6_2:
    barang = []

    def inputData(self, kode, nama, jlh):
        try:
            if int(jlh) < 0:
                raise ValueError
            self.barang.append({
                "Kode" : kode,
                "Nama" : nama,
                "Jumlah Barang" : jlh
            })
            print("Data berhasil diinput")
            return True
        except ValueError:
            print("Jumlah barang tidak boleh angka negatif\n")
            return False
        
    def urutkanData(self):
        self.barang = sorted(self.barang, key= lambda x : x["Kode"])

    def cetakData(self):
        print("Berikut data yang telah diurutkan:\n")
        x = iter(self.barang)
        while True:
            try:
                i = next(x)
                print("Kode Produk :",i["Kode"])
                print("Nama Produk :",i["Nama"])
                print("Jumlah Barang :",i["Jumlah Barang"])
                print()
            except StopIteration:
                break

    def sisaDikit(self):
        temp = [i for i in self.barang if i["Jumlah Barang"] < 10]
        x = iter(temp)
        while True:
            try:
                i = next(x)
                print(f"Sisa barang {i['Nama']} hanya {i['Jumlah Barang']}. Udah mau habis.")
            except StopIteration:
                break

# M07

class NaomiPrisellaM7_1:
    mahasiswa = []

    def validasi(self, nim, nama, noHp):
        try:
            if len(nim) != 9 or not nim.isnumeric():
                raise ValueError("NIM harus terdiri dari angka dan memiliki 9 karakter")
            if len(self.mahasiswa) > 0 and nim in [i["NIM"] for i in self.mahasiswa]:
                raise ValueError("NIM tersebut sudah pernah diinput")
            if nama == "":
                raise ValueError("Nama hanya boleh terdiri dari huruf dan spasi")
            nama = nama.split()
            for i in nama:
                if not i.isalpha():
                    raise ValueError("Nama hanya boleh terdiri dari huruf dan spasi")
            nama = " ".join(nama)
            if len(noHp) > 15 and len(noHp) < 8:
                raise ValueError("Nomor HP harus memiliki 8 - 15 karakter")
            if noHp[0] != '+':
                raise ValueError("Nomor HP harus dimulai dari '+'")
            if not noHp[1:].isnumeric():
                raise ValueError("Nomor HP hanya boleh terdiri dari angka")
            return True
        except ValueError as e:
            print()
            print(str(e))
            print("Input ulang lagi.\n")
            return False

    def absensi(self):
        nim = ''
        nama = ''
        noHp = ''
        while True:
            no = yield nim
            nim = no
            name = yield nama
            nama = name
            phone = yield noHp
            noHp = phone
            self.mahasiswa.append({
                "NIM" : nim,
                "Nama" : nama,
                "Nomor HP" : noHp
            })

    def cekNim(self,nim):
        if nim in [i['NIM'] for i in self.mahasiswa]:
            return False
        return True
    
    def pencarianData(self, cari):
        for i in self.mahasiswa:
            if cari == i["NIM"]:
                print("\nDitemukan!")
                for x,y in i.items():
                    print(x,":",y)
                return
        print("\nMahasiswa dengan NIM tersebut tidak ada di database")

    def cetakData(self):
        idx = 1
        self.urutkanData()
        for i in self.mahasiswa:
            print("Mahasiswa ke-"+str(idx))
            for x,y in i.items():
                print(x,":",y)
            print()
            idx += 1

    def urutkanData(self):
        self.mahasiswa = sorted(self.mahasiswa, key = lambda x : x["NIM"])

class NaomiPrisellaM7_2:
    barang = []

    def inputData(self):
        jenis = ''
        kode = ''
        nama = ''
        stok = ''
        while True:
            tipe = yield jenis
            jenis = tipe
            code = yield kode
            kode = code
            name = yield nama
            nama = name
            stock = yield stok
            stok = stock
            self.barang.append({
                "Jenis" : jenis,
                "Kode" : kode,
                "Nama" : nama,
                "Jumlah Barang" : stok
            })
        
    def urutkanData(self):
        self.barang = sorted(self.barang, key= lambda x : x["Jenis"])

    def cetakData(self):
        print("Berikut data yang telah diurutkan:\n")
        x = iter(self.barang)
        while True:
            try:
                i = next(x)
                print("Jenis Produk :",i["Jenis"])
                print("Kode Produk :",i["Kode"])
                print("Nama Produk :",i["Nama"])
                print("Jumlah Barang :",i["Jumlah Barang"])
                print()
            except StopIteration:
                break

    def sisaDikit(self):
        temp = [i for i in self.barang if i["Jumlah Barang"] < 10]
        x = iter(temp)
        while True:
            try:
                i = next(x)
                print(f"Sisa barang {i['Nama']} hanya {i['Jumlah Barang']}. Udah mau habis.")
            except StopIteration:
                break

# M09

class NaomiPrisellaM9:
    def __init__(self, noInduk, nama, jenisKelamin):
        self.noInduk = noInduk
        self.nama = nama
        self.jenisKelamin = jenisKelamin

class MahasiswaM9:
    def __init__(self, wrapper):
        self.wrapper = wrapper
    
    def detail(self, jurusan, email):
        self.wrapper.jurusan = jurusan
        self.wrapper.email = email

    def cetak(self):
        print("| {:<23}:{:>42} |".format("NIM Mahasiswa",self.wrapper.noInduk))
        print("| {:<23}:{:>42} |".format("Nama Mahasiswa",self.wrapper.nama))
        print("| {:<23}:{:>42} |".format("Jurusan Mahasiswa",self.wrapper.jurusan))
        print("| {:<23}:{:>42} |".format("Jenis Kelamin Mahasiswa",self.wrapper.jenisKelamin))
        print("| {:<23}:{:>42} |".format("Email Mahasiswa",self.wrapper.email))

class DosenM9:
    def __init__(self, wrapper):
        self.wrapper = wrapper

    def detail(self, jabatan, noHp):
        self.wrapper.jabatan = jabatan
        self.wrapper.noHp = noHp

    def cetak(self):
        print("| {:<23}:{:>42} |".format("NIP Dosen",self.wrapper.noInduk))
        print("| {:<23}:{:>42} |".format("Nama Dosen",self.wrapper.nama))
        print("| {:<23}:{:>42} |".format("Jabatan Dosen",self.wrapper.jabatan))
        print("| {:<23}:{:>42} |".format("Jenis Kelamin Dosen",self.wrapper.jenisKelamin))
        print("| {:<23}:{:>42} |".format("Nomor HP Dosen",self.wrapper.noHp))

class AbsensiM9:
    def __init__(self):
        self.mahasiswa = []
        self.dosen = []
        self.total = 0

    def hadir(self, org):
        self.mahasiswa.append(org) if org.__class__.__name__ == "MahasiswaM9" else self.dosen.append(org)
        self.total += 1

    def cetak(self):
        print("-"*70)
        print("|{: ^68}|".format("Dosen"))
        print("-"*60)
        for i in range(len(self.dosen)):
            print("| {:<67}|".format("Dosen ke-"+str(i+1)))
            self.dosen[i].cetak()
            print("-"*70)
        if self.dosen == []:
            print("|{: ^68}|".format("Tidak ada dosen yang hadir pada acara"))
            print("-"*70)
        print("|{: ^68}|".format("Mahasiswa"))
        print("-"*70)
        for i in range(len(self.mahasiswa)):
            print("| {:<67}|".format("Mahasiswa ke-"+str(i+1)))
            self.mahasiswa[i].cetak()
            print("-"*70)
        if self.mahasiswa == []:
            print("|{: ^68}|".format("Tidak ada mahasiswa yang hadir pada acara"))
            print("-"*70)
        print("| {:<23}{:^1}{:>42} |".format("Jumlah Pengunjung",":",self.total))
        print("-"*70)

# M10

class NaomiPrisellaM10:
    _instance = None
    _Absensi = {"Dosen" : dict(), "Mahasiswa" : dict()}
    _idx = 0
    def __init__(self):
        self.__dict__ = self._Absensi

class HadirAcaraM10(NaomiPrisellaM10):
    def __init__(self, tipe, **data):
        NaomiPrisellaM10.__init__(self)
        self._Absensi[tipe].update({self._idx : data})
        self._idx += 1
    
    def cetakAbsensi(self):
        print("{:^70}".format("REKAP ABSENSI"))
        print()
        print("-"*70)
        print("|{: ^68}|".format("Dosen"))
        print("-"*70)
        for i in self._Absensi["Dosen"].values():
            for x, y in i.items():
                key = x
                if x != "NIP":
                    for i in range(1,len(x)):
                        if x[i] == x[i].upper():
                            key = x[:i] + " " + x[i:]
                            break
                key += " Dosen"
                print("| {:<23}:{:>42} |".format(key,y))
            print("-"*70)
        if len(self._Absensi["Dosen"]) == 0:
            print("|{: ^68}|".format("Tidak ada dosen yang hadir pada acara"))
            print("-"*70)
        print("|{: ^68}|".format("Mahasiswa"))
        print("-"*70)
        for i in self._Absensi["Mahasiswa"].values():
            for x, y in i.items():
                key = x
                if x != "NIM":
                    for i in range(1,len(x)):
                        if x[i] == x[i].upper():
                            key = x[:i] + " " + x[i:]
                            break
                key += " Mahasiswa"
                print("| {:<23}:{:>42} |".format(key,y))
            print("-"*70)
        if len(self._Absensi["Mahasiswa"]) == 0:
            print("|{: ^68}|".format("Tidak ada mahasiswa yang hadir pada acara"))
            print("-"*70)

        total = 0
        total = sum([1 for i in self._Absensi["Dosen"].keys()] + [1 for i in self._Absensi["Mahasiswa"].keys()])
        print("| {:<23}{:^1}{:>42} |".format("Jumlah Pengunjung",":",total))
        print("-"*70)
        print()

    def cariAtauCekData(self, nama, tipe):
        for i in self._Absensi[tipe].values():
            print()
            if i["Nama"] == nama:
                print(tipe.capitalize() + " ditemukan!\n")
                for x, y in i.items():
                    key = x
                    if x != "NIM" and x != "NIP":
                        for i in range(1,len(x)):
                            if x[i] == x[i].upper():
                                key = x[:i] + " " + x[i:]
                                break
                    key += " " + tipe
                    print("{:<23}:{:>42}".format(key,y))
                return
        print(tipe.capitalize() + " Tidak ditemukan pada database.")
