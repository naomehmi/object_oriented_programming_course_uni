from class_k import NaomiPrisellaM6_1

pil = ''
data = NaomiPrisellaM6_1()

while True:
    try:
        print()
        print("Data Mahasiswa Mikroskil")
        print("="*24)
        print()
        print("1. Input Data")
        print("2. Cetak Data")
        print("3. Pencarian Data")
        print("4. Keluar")
        print()
        pil = int(input("Pilih salah satu (1/2/3/4) : "))
        print()
        if pil < 1 or pil > 4:
            raise ValueError
        
        if pil == 1:
            while True:
                try:
                    n = int(input("Ingin input berapa data? : "))
                    print()
                    if n < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Isi suatu angka lebih besar dari 0\n")
            for i in range(n):
                while True:
                    a = input("NIM Mahasiswa : ").lstrip().rstrip()
                    b = input("Nama Mahasiswa : ").title().lstrip().rstrip()
                    c = input("Nomor HP Mahasiswa : ").lstrip().rstrip()
                    if not data.inputData(a, b, c):
                        continue
                    break

        elif pil == 2:
            if not data.mahasiswa:
                print("Data masih kosong. Input dulu.")
            else:
                print("Berikut data yang telah diurutkan:\n")
                data.cetakData()

        elif pil == 3:
            cari = input("NIM mahasiswa yang ingin dicari: ")
            data.pencarianData(cari)
        
        elif pil == 4:
            break

    except ValueError:
        print("Hanya boleh isi dengan 1, 2, atau 3. Coba lagi.")
