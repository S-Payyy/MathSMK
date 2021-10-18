# Run in Python3.10
# Code by OSIEEE-Xcl

import time
import os
os.system('color 2')

# Manifest
nama = "Rekap Absensi Kelas"
versi = "1.5.2"
versi_python = "3.10"

# startup program
print(120*"=")
print ("Nama  Program : %s" % nama)
print ("Versi Program : %s" % versi)
print ("Versi Python  : %s" % versi_python)

# Fungsi menu
def show_menu():
  os.system('color 9')
  print(120*"=")
  print('0. Exit')
  print('1. Absensi kelas XII TKJ 1')
  print(120*"=")
  menu = input("Code Program > ")
  print('\n')

  if menu=='1':
      rekap()
  elif menu=='0':
    exit()

  else:
    os.system('cls')
    os.system('color 4')
    print("Code salah !")
    time.sleep(0.2)
    os.system('cls')
    print('Code created by @xcl')
  return show_menu()

# Fungsi 1 
def rekap():
#input data
  os.system('cls')
  os.system('color B')
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
  print('= Daftar siswa yang tidak Absen = ')
  print(1*'\n')
  for name in alpha:
    os.system('color 4')
    print(f'>> {name}, Tidak hadir')

  print('\n')
  print(f' Jumlah siswa kelas XII TKJ 1  > {jumlah_siswa}')
  print(f' Jumlah siswa yang Absen       > {hadir}')
  print(f' Jumlah siswa yang tidak Absen > {tidak_hadir}')
  print('\n')

  # Percabangan Loop dari fungsi 1
  print("Coba lagi [Y/N]?")
  back = input("").upper()
  if back == 'Y':
    os.system('cls')
    rekap()
  else:
    os.system('cls')
    print('Code created by @xcl')
    show_menu()
  
show_menu() 