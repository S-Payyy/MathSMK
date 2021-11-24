import os

def rekap():
#input data
  from Code import menu as m
  os.system('cls')
  print(120*"=")
  data_kelas = str(input("Masukkan Data Kelas : ")).lower()

#variabel
  classmates = ["abil", "akmal", "alejandro", "alfarid", "dafa", "danu", "fahmi", "farhad", "febrian", "ilham", "iqnas", "keiza", "khairul", "akbar", "maheswara", "iqbal", "rifai", "albi", "ihsan", "raihan", "ardyanto", "syawal", "seto", "steven", "syahrul", "thomas", "yoga", "zaki"]
  alpha = []
  tidak_hadir = 0
  hadir = 0

#fungsi 1
  for name in classmates:
    match name in data_kelas: #this
      case False:
        tidak_hadir += 1
        alpha.append(name)
      case True:
        hadir += 1
    jumlah_siswa = tidak_hadir + hadir

#output dari fungsi 1
  print(1*'\n')
  print('= Daftar siswa yang tidak/terlambat Absen = ')
  print(1*'\n')
  for name in alpha:
    print(f'>> {name.capitalize()}, Tidak Absen')

  print('\n')
  print(f' Jumlah siswa kelas XII TKJ 1  > {jumlah_siswa}')
  print(f' Jumlah siswa yang Absen       > {hadir}')
  print(f' Jumlah siswa yang tidak Absen > {tidak_hadir}')
  print('\n')

  # Percabangan Loop dari fungsi 1
  print("Coba lagi [Y/N]?")
  back = input("").upper()
  if back == 'Y':
    rekap()
  else:
    os.system('cls')
    print('Code created by @xcl')
    m.show_menu()
