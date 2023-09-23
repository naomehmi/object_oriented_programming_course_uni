from class_k import mahasiswa, dosen

print("REKAP ABSENSI")
print("*************")

rep = True
jlh = 0
listMahasiswa = []
listDosen = []

while rep:
    print("\nApakah anda ingin menginput data mahasiswa (M) atau dosen (D)?")
    pilih = input("=> ")
    if pilih.lower() == "m":
        print()
        a = input(f"Nama Mahasiswa\t\t\t\t: ")
        a = a.title()
        b = int(input("NIM Mahasiswa\t\t\t\t: "))
        c = ""
        while c.lower() != "l" and c.lower() != "p":
            c = input("Jenis Kelamin Mahasiswa (L/P)\t\t: ")
            if c.lower() != "l" and c.lower() != "p":
                print("Jawaban hanya boleh dalam bentuk L atau P. Coba lagi.")
            else:
                if c.lower() == "l":
                    c = "Laki - laki"
                else:
                    c = "Perempuan"
                break
        d = ""
        while d.lower() != "if" and d.lower() != "si" and d.lower() != "ti" and d.lower() != "mn" and d.lower() != "ak":
            d = input("Jurusan Mahasiswa (IF/SI/TI/MN/AK)\t: ")
            if d.lower() != "if" and d.lower() != "si" and d.lower() != "ti" and d.lower() != "mn" and d.lower() != "ak":
                print("Jawaban hanya boleh berupa dalam bentuk IF, SI, TI, MN, atau AK. Coba lagi.")
            else:
                if d.lower() == "if":
                    d = "Teknik Informatika"
                elif d.lower() == "si":
                    d = "Sistem Informasi"
                elif d.lower() == "ti":
                    d = "Teknologi Informasi"
                elif d.lower() == "mn":
                    d = "Manajemen"
                else:
                    d = "Akuntansi"
                break
        e = input("Email Mahasiswa\t\t\t\t: ")
        maha = mahasiswa(a,b,c,d,e)
        listMahasiswa.append(maha)
        jlh += 1
    elif pilih.lower() == "d":
        print()
        a = input("Nama Dosen\t\t\t\t: ")
        a = a.title()
        b = int(input("NIP Dosen\t\t\t\t: "))
        c = input("Jabatan Dosen\t\t\t\t: ").title()
        d = ""
        while d.lower() != "l" and d.lower() != "p":
            d = input("Jenis Kelamin Dosen (L/P)\t\t: ")
            if d.lower() != "l" and d.lower() != "p":
                print("Jawaban hanya boleh dalam bentuk L atau P. Coba lagi.")
            else:
                if d.lower() == "l":
                    d = "Laki - laki"
                else:
                    d = "Perempuan"
                break
        e = input("Nomor HP Dosen\t\t\t\t: ")
        dos = dosen(a,b,c,d,e)
        listDosen.append(dos)
        jlh += 1
    else:
        print("Jawaban hanya bisa dalam bentuk M atau D. Coba lagi.")
        continue

    while pilih.lower() != "y" and pilih.lower() != "n":
        print("\nApakah anda ingin menginput data lagi? (Y/N)")
        pilih = input("=> ")
        if pilih.lower() == "y":
            rep = True
        elif pilih.lower() == "n":
            rep = False
        else:
            print("Jawaban hanya bisa berupa Y atau N. Coba lagi.")

print()
print("{:^75}".format("LAPORAN ABSENSI ACARA COOLEYAH"))
print("{:^75}".format("="*30))
print()

print("-"*75)
print("|{: ^73}|".format("Dosen"))
print("-"*75)
for i in range(len(listDosen)):
    print("| {:<72}|".format("Dosen ke-"+str(i+1)))
    listDosen[i].cetak()
    print("-"*75)
if listDosen == []:
    print("|{: ^73}|".format("Tidak ada dosen yang hadir pada acara"))
    print("-"*75)
print("|{: ^73}|".format("Mahasiswa"))
print("-"*75)
for i in range(len(listMahasiswa)):
    print("| {:<72}|".format("Mahasiswa ke-"+str(i+1)))
    listMahasiswa[i].cetak()
    print("-"*75)
if listMahasiswa == []:
    print("|{: ^73}|".format("Tidak ada mahasiswa yang hadir pada acara"))
    print("-"*75)
print("| {:<23}{:^1}{:>47} |".format("Jumlah Pengunjung",":",jlh))
print("-"*75)
