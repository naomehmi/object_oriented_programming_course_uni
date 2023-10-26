from class_k import NaomiPrisellaM5_1

listMahasiswa = NaomiPrisellaM5_1()

while True:
    try:
        n = int(input("Berapa data mahasiswa yang ingin diinput? : "))
        if n < 1:
            raise ValueError
        break
    except ValueError:
        print("Input angka di atas 1.")

listMahasiswa.pemasukanData(n)

while True:
    try:
        n = int(input("\nIngin melakukan berapa pencarian data? : "))
        if n < 1:
            raise ValueError
        break
    except ValueError:
        print("Input angka di atas 1.")

for i in range(n):
    nim = input("Input NIM mahasiswa yang ingin dicari: ")
    listMahasiswa.absensi(nim)
