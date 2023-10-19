from class_k import Parent, DosenM4, MahasiswaM4

while True:
    try:
        md = input("Ingin input data mahasiswa atau dosen? (M/D) : ").lower()
        if md not in ["m","d"]:
            raise ValueError("Hanya menerima masukkan 'M' atau 'D'. Coba lagi")
        break
    except ValueError as e:
        print(str(e))
    
if md == 'm':
    a = input("Masukkan NIM mahasiswa   : ")
    b = input("Masukkan nama mahasiswa  : ").title()
    c = input("Masukkan no HP mahasiswa : ")
    try:
        maha = MahasiswaM4(a,b,c)
        maha.cetak()
    except AttributeError:
        pass
else:
    a = input("Masukkan NIP dosen   : ")
    b = input("Masukkan nama dosen  : ").title()
    c = input("Masukkan no HP dosen : ")
    try:
        dos = DosenM4(a,b,c)
        dos.cetak()
    except AttributeError:
        pass
