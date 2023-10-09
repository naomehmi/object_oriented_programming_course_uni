from class_k import RyanRussell, handSanitizer, banMobil, buahBuahan, botolMinumBayi

namaProduk = ["Hand Sanitizer", "Ban Mobil", "Buah-Buahan", "Botol Minuman Bayi"]
stock = []
for i in range(4):
    stock.append(int(input(f"Masukkan jumlah {namaProduk[i].lower()} yang terjual bulan ini : ")))
produk = []
produk.append(handSanitizer("HS-008",stock[0],100))
produk.append(banMobil("BM-010",stock[1],50))
produk.append(buahBuahan("BB-505",stock[2],"Australia"))
produk.append(botolMinumBayi("BM-066",stock[3],150))
print()
print("{:^75}".format("LAPORAN BULANAN E-COMMERCE"))
print()
print("="*75)
for i in range(4):
    produk[i].laporan()
