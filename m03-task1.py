from class_k import AyamGoreng, ManusiaMikroskil, Mahasiswa_m3, Dosen_m3

n = int(input("Berapa data yang ingin diinput? : "))

for i in range(n):
    pil = None
    while pil != "dosen" and pil != "mahasiswa":
        pil = input("Ingin input data mahasiswa atau dosen : ").lower()
        if pil != "dosen" and pil != "mahasiswa":
            print("Input yang diterima hanya 'dosen' atau 'mahasiswa'. Mohon coba lagi")
        if pil == "mahasiswa":
            a = input("Nama Mahasiswa : ")
            b = input("NIM Mahasiswa : ")
            maha = Mahasiswa_m3(a,b)
            maha.absensi()
        elif pil == "dosen":
            a = input("Nama Dosen : ")
            b = input("NIP Dosen : ")
            dos = Dosen_m3(a,b)
            dos.absensi()
        print()
