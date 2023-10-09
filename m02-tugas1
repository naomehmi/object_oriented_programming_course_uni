from class_k import NaomiPrisella, mahasiswa_m2, dosen_m2

n = int(input("Ingin input berapa data? : "))
listMahasiswa = []
listDosen = []
for i in range(n):
    m = None
    if m != "mahasiswa" and m != "dosen":
        m = input("Ingin input data Mahasiswa/Dosen? : ")
        if m == "mahasiswa":
            a = input("Masukkan NIM : ")
            b = input("Masukkan Nama Mahasiswa : ").title()
            c = input("Masukkan Jenis Kelamin Mahasiswa : ")
            d = input("Masukkan No HP Mahasiswa : ")
            listMahasiswa.append(mahasiswa_m2(a,b,c,d))
        elif m == "dosen":
            a = input("Masukkan NIP : ")
            b = input("Masukkan Nama Dosen : ").title()
            c = input("Masukkan Jenis Kelamin Dosen : ")
            d = input("Masukkan No HP Dosen : ")
            listDosen.append(dosen_m2(a,b,c,d))
print("-"*75)
print("|{:^73}|".format("Absensi"))
print("-"*75)
print("|{:^73}|".format("Dosen"))
print("-"*75)
for i in range(len(listDosen)):
    print("| {:<72}|".format("Dosen ke-"+str(i+1)))
    listDosen[i].perkenalan()
    print("-"*75)
print("|{:^73}|".format("Mahasiswa"))
print("-"*75)
for i in range(len(listMahasiswa)):
    print("| {:<72}|".format("Mahasiswa ke-"+str(i+1)))
    listMahasiswa[i].absensi()
    print("-"*75)
print("| {:<20}:{:>50} |".format("Jumlah Pengunjung",len(listMahasiswa) + len(listDosen)))
print("-"*75)
