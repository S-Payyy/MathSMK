def show_menu():
    import os
    from Code import RekapKelas as rk
    from Code import matematika as mt
    import time

    os.system('color 9')
    print(120*"=")
    print('0. Exit')
    print('1. Absensi kelas XII TKJ 1')
    print('2. Matematika kelas XII TKJ 1')
    print(120*"=")
    menu = input("Code Program > ")
    print('\n')

    if menu=='1':
        rk.rekap()
        os.system('cls')
        print('Code created by @xcl')
  
    elif menu=='2':
        mt.menucal()
        os.system('cls')
        os.system('color 4')
        print('Code created by @xcl')

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
