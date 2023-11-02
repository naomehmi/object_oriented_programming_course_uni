from class_k import NaomiPrisellaM6_2

data = NaomiPrisellaM6_2()
nama = [["HS-001","Hand Sanitizer"], ["BM-034","Ban Mobil"], ["BB-404","Buah-Buahan"], ["BM-111","Botol Minuman Bayi"]]
pil = ''

for i in nama:
    while True:
        try:
            x = int(input(f"Sisa Jumlah Barang {i[0]} ({i[1]}) : "))
            if not data.inputData(i[0],i[1],x):
                continue
            print()
            break
        except ValueError:
            print("Hanya boleh isi dengan angka lebih dari 0")

data.urutkanData()

while True:
    try:
        print()
        print("1. Cetak Semua Data Produk")
        print("2. Tampil Stok yang tinggal sedikit")
        print("3. Keluar")
        print()
        pil = int(input("Pilih salah satu (1/2/3) : "))
        print()
        if pil < 1 or pil > 3:
            raise ValueError
        
        if pil == 1:
            data.cetakData()
        
        elif pil == 2:
            data.sisaDikit()

        elif pil == 3:
            break

    except ValueError:
        print("Hanya boleh isi angka 1, 2, atau 3. Coba lagi.")
