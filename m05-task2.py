from class_k import NaomiPrisellaM5_2, ProdukM5

listProduk = NaomiPrisellaM5_2()
nama = [["HS-001","Hand Sanitizer"], ["BM-034","Ban Mobil"], ["BB-404","Buah-Buahan"], ["BM-111","Botol Minuman Bayi"]]

listProduk.pemasukanData(nama)

while True:
    try:
        n = int(input("\nIngin melakukan berapa pencarian data? : "))
        if n < 1:
            raise ValueError
        break
    except ValueError:
        print("Input angka di atas 1.")

for i in range(n):
    nama = input("Input kode produk atau nama produk yang ingin dicek stoknya : ").lower()
    listProduk.pencarianStok(nama)
    print()
