import unittest
from class_k import NaomiPrisellaM9, MahasiswaM9, DosenM9, AbsensiM9

class checkTotal(unittest.TestCase):
  def sampleData(self):
    data = AbsensiM9()
    mh1 = MahasiswaM9(NaomiPrisellaM9("221111798", "Naomi Prisella", "Perempuan"))
    mh1.detail("Teknik Informatika", "221111798@students.mikroskil.ac.id")
    mh2 = MahasiswaM9(NaomiPrisellaM9("231120000", "Anonim Anonim", "Laki-laki"))
    mh2.detail("Sistem Informasi", "anonim.anonim@students.mikroskil.ac.id")
    ds1 = DosenM9(NaomiPrisellaM9("111222333", "Nadya Sikana", "Perempuan"))
    ds1.detail("Dosen Informatika", "081111222")
    data.hadir(mh1)
    data.hadir(mh2)
    data.hadir(ds1)
    return data

  def testing(self):
    data = self.sampleData()
    self.assertEqual(data.total,3)

if __name__ == "__main__":
  unittest.main(verbosity=2)
