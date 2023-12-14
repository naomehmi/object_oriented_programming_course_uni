from class_k import Total, UangPendaftaran, KuliahPertama, uangMPT

def formatHarga(a):
  for i in range(len(a)-4,-1,-3):
    a = a[:i+1] + "." + a[i+1:]
  return "IDR " + a

if __name__ == "__main__":
  biaya = [UangPendaftaran("Uang Pendaftaran", 200000), KuliahPertama("Uang Kuliah Pertama", 1500000)]
  mpt = [uangMPT("Uang Training", 100000), uangMPT("Uang Penginapan", 200000), uangMPT("Uang Komsumsi", 150000)]
  grandTotal = Total(biaya + mpt)

  print("-"*57)
  print("| {:<25} | {:<25} |".format("Biaya","Total"))
  print("-"*57)
  for b in biaya: print("| {:<25} | {:<25} |".format(b.name, formatHarga(str(b.price))))
  print("| {:<25} | {:<25} |".format("Uang MPT:",""))
  for m in mpt: print("| {:<25} | {:<25} |".format("- " + m.name, formatHarga(str(m.price))))
  print("-"*57)
  print("| {:<25} | {:<25} |".format("Grand Total",formatHarga(str(grandTotal.returnPrice()))))
  print("-"*57)
