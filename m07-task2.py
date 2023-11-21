from class_k import NaomiPrisellaM7_2

data = NaomiPrisellaM7_2()

while True:
    try:
        print("STOCK E-COMMERCE\n")
        print("1. Input data baru")
        print("2. Cetak semua data produk")
        print("3. Tampil stok yang tinggal sedikit")
        print("4. Keluar")
        print()
        pil = int(input("Pilih salah satu (1/2/3/4) : "))
        print()
        if pil < 1 or pil > 4:
            raise ValueError

        if pil == 1:
            while True:
                try:
                    print("Jika kode, nama, dan jenis produk yang diinput sudah ada di dalam database, maka jumlah stoknya akan bertambah")
                    a = data.inputData()
                    next(a)
                    w = input("Jenis barang : ").lower().lstrip().rstrip()
                    x = input("Kode barang : ").upper().lstrip().rstrip()
                    y = input("Nama barang : ").title().lstrip().rstrip()
                    z = int(input("Stock barang : "))
                    if not data.validasi1(w, x, y, z):
                        continue
                    a.send(w)
                    a.send(x)
                    a.send(y)
                    a.send(z)
                    print("Jumlah stok :",data.totalSemua())
                    print()

                    while True:
                        try:
                            pil2 = input("Apakah masih mau input barang lagi? (Y/N) : ").lower()

                            if pil2 != 'y' and pil2 != 'n':
                                raise ValueError("Jawaban hanya boleh berupa 'y' atau 'n'")

                            break

                        except ValueError as e:
                            print(str(e))

                    if pil2 == 'n':
                        break

                            
                except ValueError:
                    print("Stock harus berupa angka di atas 0")

        elif pil == 2:
            if not data.barang:
                print("Data masih kosong")
                continue
            data.cetakData()
            print("Total :",data.totalSemua())

        elif pil == 3:
            data.sisaDikit()

        elif pil == 4:
            break

    except ValueError:
        print("Hanya boleh isi angka 1, 2, atau 3. Coba lagi")
