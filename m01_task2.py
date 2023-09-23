from class_k import produk

brg = [["HS-E1","Hand Sanitizer"], ["BM-E2", "Ban Mobil"], ["BH-E3","Buah-buahan"], ["BM-E4", "Botol Minuman Bayi"]]
brg_class = []
print("LAPORAN STOCK E-COMMERCE")
print("="*24)
print()
for i in range(4):
    pcs = int(input(f"Sisa stock {brg[i][1]} : "))
    pro = produk(brg[i][0],brg[i][1],pcs)
    brg_class.append(pro)
print()
print("="*50)
for i in range(4):
    print("| {:<21}{:^3}{:>22} |".format("Kode Produk",":",brg_class[i].kode))
    print("| {:<21}{:^3}{:>22} |".format("Nama Produk",":",brg_class[i].nama))
    print("| {:<21}{:^3}{:>22} |".format("Qty Produk",":",str(brg_class[i].qty)+" pcs"))
    print("="*50)
