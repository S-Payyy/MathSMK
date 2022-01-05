# tahap pengembangan ~

import math


def kaidah_pencacahan():
    txt = input("Nilai (ex : 1 2 3 4...) = ")
    x = txt.replace(' ', '*')
    print(f'Hasil Pencacahan = {eval(x)}')
    print('\n')

    back = input('Coba lagi [Y/N] ? ').upper()
    if back == 'Y':
        print('\n')
        return kaidah_pencacahan()
    else:
        menucal()

def filling_slot():
    import os

    os.system('cls')
    print('Code created by @xcl')
    print(120*"=")
    print("a. Angka boleh Berulang")
    print("b. Angka tidak boleh Berulang\n")
    c = input("Masukkan pilihan a/b > ").lower()
    if c == 'a':
        x = input("Masukkan angka > ").split(' ')
        y = input('Jumlah digit > ')
        z = len(x)
        out = int(z)**int(y)
        print(f'Hasil = {out} cara\n')
        back = input('Coba lagi [Y/N] ? ').upper()
        if back == 'Y':
            print('\n')
            return filling_slot()
        else:
            menucal()
    elif c == 'b':
        x = input("Masukkan angka > ").split(' ')
        y = input('Jumlah digit (max 10)> ')
        z = len(x)
        out1 = int(z)
        out2 = int(z)*int(z-1)
        out3 = int(z)*int(z-1)*int(z-2)
        out4 = int(z)*int(z-1)*int(z-2)*int(z-3)
        out5 = int(z)*int(z-1)*int(z-2)*int(z-3)*int(z-4)
        out6 = int(z)*int(z-1)*int(z-2)*int(z-3)*int(z-4)*int(z-5)
        out7 = int(z)*int(z-1)*int(z-2)*int(z-3)*int(z-4)*int(z-5)*int(z-6)
        out8 = int(z)*int(z-1)*int(z-2)*int(z-3)*int(z-4)*int(z-5)*int(z-6)*int(z-7)
        out9 = int(z)*int(z-1)*int(z-2)*int(z-3)*int(z-4)*int(z-5)*int(z-6)*int(z-7)*int(z-8)
        out10 = int(z)*int(z-1)*int(z-2)*int(z-3)*int(z-4)*int(z-5)*int(z-6)*int(z-7)*int(z-8)*int(z-9)
        print(f'Banyak Digit 1 > {out1}')
        print(f'Banyak Digit 2 > {out2}')
        print(f'Banyak Digit 3 > {out3}')
        print(f'Banyak Digit 4 > {out4}')
        print(f'Banyak Digit 5 > {out5}')
        print(f'Banyak Digit 6 > {out6}')
        print(f'Banyak Digit 7 > {out7}')
        print(f'Banyak Digit 8 > {out8}')
        print(f'Banyak Digit 9 > {out9}')
        print(f'Banyak Digit 10 > {out10}\n')
        if z == int(y):
            print(f'Banyak Digit {y} > 1\n')
        else:
            pass

    back = input('Coba lagi [Y/N] ? ').upper()
    if back == 'Y':
        print('\n')
        return filling_slot()
    else:
        menucal()

def notasi_faktorial():
    import math

    print(120*'=')
    n = int(input('Masukkan nilai faktorial > '))
    fak = math.factorial(n)
    print(f'\nNilai {n}! adalah {fak}')
    
    back = input('\nCoba lagi [Y/N] ? ').upper()
    if back == 'Y':
        print('\n')
        return notasi_faktorial()
    else:
        menucal()

def permutasi_unsur_berbeda():
    import math
    print(120*'=')
    print('Index nilai = "nPr"')
    n = int(input('Masukkan nilai n > '))
    r = int(input('Masukkan nilai r > '))
    z = (n-r)
    n_fac = math.factorial(n)
    z_fac = math.factorial(z)
    out = n_fac/z_fac
    print(f'\nHasil = {int(out)} Cara ')

    back = input('\nCoba lagi [Y/N] ? ').upper()
    if back == 'Y':
        print('\n')
        return permutasi_unsur_berbeda()
    else:
        menucal()

def permutasi_unsur_sama():
    import math

    print("1. Berapa banyak  cara menyusun huruf dari kata 'SELASA' ?\n2. Dalam suatu perpustakaan terdapat 3 buku bahasa indonesia, 2 buku ppkn, dan 3 buku b.inggris. Berapa banyak cara menyusun buku buku  tersebut?\n")
    soal = input("Pilih contoh soal 1/2 : ")
    print("\n")
    if soal == '1':
        kata = input("Masukkan Kata : ".lower())
        total_huruf = len(kata)
        a = kata.count('a')
        b = kata.count('b')
        c = kata.count('c')
        d = kata.count('d')
        e = kata.count('e')
        f = kata.count('f')
        g = kata.count('g')
        h = kata.count('h')
        i = kata.count('i')
        j = kata.count('j')
        k = kata.count('k')
        l = kata.count('l')
        m = kata.count('m')
        n = kata.count('n')
        o = kata.count('o')
        p = kata.count('p')
        q = kata.count('q')
        r = kata.count('r')
        s = kata.count('s')
        t = kata.count('t')
        u = kata.count('u')
        v = kata.count('v')
        w = kata.count('w')
        x = kata.count('x')
        y = kata.count('y')
        z = kata.count('z')
        if a < 1:
            a = 1
            b = 1
            c = 1
            d = 1
            e = 1
            f = 1
            g = 1
            h = 1
            i = 1
            j = 1
            k = 1
            l = 1
            m = 1
            n = 1
            o = 1
            p = 1
            q = 1
            r = 1
            s = 1
            t = 1
            u = 1
            v = 1
            w = 1
            x = 1
            y = 1
            z = 1

        f_total_huruf = math.factorial(total_huruf)

        f_huruf = math.factorial(a)*math.factorial(b)*math.factorial(c)*math.factorial(d)*math.factorial(e)*math.factorial(f)*math.factorial(g)*math.factorial(h)*math.factorial(i)*math.factorial(j)*math.factorial(k)*math.factorial(l)*math.factorial(m)*math.factorial(n)*math.factorial(o)*math.factorial(p)*math.factorial(q)*math.factorial(r)*math.factorial(s)*math.factorial(t)*math.factorial(u)*math.factorial(v)*math.factorial(w)*math.factorial(x)*math.factorial(y)*math.factorial(z)

        P = f_total_huruf/f_huruf

        print(f'Jawaban adalah : {P}')

        back = input('\nCoba lagi [Y/N] ? ').upper()
        if back == 'Y':
            print('\n')
            return permutasi_unsur_sama()
        else:
            menucal()

    elif soal == '2':
        print('Jika memasukkan hanya angka beri jarak antar angka dengan space ex : 1 2 3 4 dst...')
        kata = input("Masukkan Soal/angka : ".lower())

        f_angka = [int(s) for s in kata.split() if s.isdigit()]

        qq = 0
        fac = []
        for i in f_angka:
            qq = qq + i
            ff = math.factorial(i)
            fac.append(ff)

        result = 1
        for x in fac:
            result = result * x

        f_qq = math.factorial(qq)

        P = f_qq/result

        print(f'Jawaban adalah : {int(P)}')

        back = input('\nCoba lagi [Y/N] ? ').upper()
        if back == 'Y':
            print('\n')
            return permutasi_unsur_sama()
        else:
            menucal()

    else :
        print('\nPilihan salah!')
        return permutasi_unsur_sama()

def permutasi_siklis():
    import math
    print('Contoh soal :\n1. Tidak ada yang berdampingan\n2. Ada yang Berdampingan')
    soal = input('Pilih jenis soal : ')
    print("\n")
    if soal=='1':
        orang = input("Banyaknya orang dalam soal = ")
        ps = (int(orang)-1)
        h = math.factorial(ps)
        print(f'\nHasil = {h}')

        back = input('\nCoba lagi [Y/N] ? ').upper()
        if back == 'Y':
            print('\n')
            return permutasi_siklis()
        else:
            menucal()

    elif soal=='2':
        orang1 = input("Banyaknya orang yang tidak berdampingan = ")
        orang2 = input("Banyaknya orang yang berdampingan = ")
        r1 = (int(orang1)-1)
        f1 = math.factorial(r1)
        r2 = math.factorial(int(orang2))
        h = f1*r2
        
        print(f'\nHasil = {h}')

        back = input('\nCoba lagi [Y/N] ? ').upper()
        if back == 'Y':
            print('\n')
            return permutasi_siklis()
        else:
            menucal()

    else :
        print('\nPilihan salah!')
        return permutasi_siklis()

def kombinasi():
    import math

    n = input('Masukkan Nilai n : ')
    r = input('Masukkan Nilai r : ')
    
    a1 = int(n) 
    a2 = int(r)
    a3 = int(n)-int(r)
    f1 =math.factorial(a1)
    f2 = math.factorial(a2)
    f3 = math.factorial(a3)
    r = f1/(f2*f3)
    print(f'Hasil adalah : {r}')
    
    back = input('\nCoba lagi [Y/N] ? ').upper()
    if back == 'Y':
        print('\n')
        return kombinasi()
    else:
        menucal()

def ruang_sampel():
    logam = 0
    dadu = 0

    logam = input('Masukkan Banyak Logam (Masukkan nilai 0 jika tidak ada) : ')
    dadu = input('Masukkan Banyak Dadu (Masukkan nilai 0 jika tidak ada) : ')

    r = (2**int(logam))*(6**int(dadu))
    if int(logam) <= 0 and int(dadu) <= 0 :
        r = 0
    print(f'Hasil adalah : {r}')
    
    back = input('\nCoba lagi [Y/N] ? ').upper()
    if back == 'Y':
        print('\n')
        return ruang_sampel()
    else:
        menucal()

def peluang_kejadian():
    import fractions as fr
    print("Jenis Sampel : \n1. Logam(can't use)\n2. Dadu\n3. Kartu Bridge(can't use)\n")
    soal = input('Masukkan No Soal : ')
    if soal == '1':
        peluang_kejadian()
    #    def jenis_soal():
    #        print('Jenis Peluang :\n1. Peluang muncul 1 angka\n2. Peluang muncul gambar\n')
    #        jenis = input('Masukkan Jenis Peluang : ')
    #        if jenis == '1':
    #           pass
    #        elif jenis == '2':
    #            pass
    #        elif jenis == '3':
    #            pass
    #        else:
    #            print('\nPilihan salah!\n')
    #            return jenis_soal()
    #    jenis_soal()        

    elif soal == '2':
        def jenis_soal():
            print('Jenis Peluang :\n1. Peluang muncul angka Ganjil\n2. Peluang muncul angka Genap\n3. Pelang muncul angka\n4. Bilangan Prima\n5. Bilangan non Prima')
            jenis = input('Masukkan Jenis Peluang : ')
            if jenis == '1':
                aganjil = 3
                ns = 6
                n = input('\nBanyak dadu : ')
                pa = aganjil/ns**int(n)
                pecahan = fr.Fraction(pa)
                print(f'Hasil adalah : {pa} atau {pecahan}')

            elif jenis == '2':
                agenap = 3
                ns = 6
                n = input('\nBanyak dadu : ')
                pa = agenap/ns**int(n)
                pecahan = fr.Fraction(pa)
                print(f'Hasil adalah : {pa} atau {pecahan}')

            elif jenis == '3':
                from Code import padadu as pad
                pad.peluang_dadu()
                back = input('\nCoba lagi [Y/N] ? ').upper()
                if back == 'Y':
                    print('\n')
                    return peluang_kejadian()
                else:
                    menucal()

            elif jenis == '4':
                pass

            elif jenis == '5':
                pass

            else:
                print('\nPilihan salah!\n')
                return jenis_soal()
        jenis_soal()        

    elif soal == '3':
        peluang_kejadian()
    else :
        print('\nPilihan salah!')
        return peluang_kejadian()

def frekuensi_harapan():
    pass

def peluang_kejadian_saling_lepas():
    pass

def peluang_kejadian_saling_bebas():
    pass

def statistika():
    pass

def ukuran_pemusatan_data_tunggal():
    pass

def angka_baku():
    print('''
    Nilai matematika Rian 75 dengan rata-rata kelas 67 dan simpangan baku 8. Nilai Bahasa Inggris
    Rian 80 dengan rata-rata kelas 70 dan simpangan baku 12. Bagaimana kedudukan Rian dalam
    pelajaran Matematika? Apakah lebih baik dari Bahasa Inggris atau sebaliknya?
    x = Nilai Rian ( ex 75 )
    x_bar = rata rata (ex 67)
    sd = simpangan baku ( ex 8 )\n
    ''')
    x = input('Masukkan Nilai data = ')
    x_bar = input("Masukkan Nilai rata rata = ")
    sd = input("Masukkan Nilai Simpangan baku = ")
    #calculating

    z = (float(x)-float(x_bar))/float(sd) 

    print(f'Hasil = {round(z, 2)}')
    print('\n')

    back = input('Coba lagi [Y/N] ? ').upper()
    if back == 'Y':
        print('\n')
        return angka_baku()
    else:
        menucal()

def angka_baku2():
    print('''
    Dalam suatu kelas, nilai rata-rata ulangan matematika adalah 70. Bima mempunyai angka baku
    1,5 sedangkan simpangan bakunya 4. Berapakah nilai ulangan Bima?
    x_bar = rata rata (ex 70)
    ab = Angka baku (ex 1.5)
    sd = Simpangan baku (ex 4)\n
    ''')
    x_bar = input("Masukkan Nilai rata rata = ")
    ab = input("Masukkan Nilai Angka baku = ")
    sd = input("Masukkan Nilai Simpangan baku = ")

    x = float(sd)*float(ab)+float(x_bar)

    print(f'hasil = {round(x, 2)}')
    print('\n')

    back = input('Coba lagi [Y/N] ? ').upper()
    if back == 'Y':
        print('\n')
        return angka_baku2()
    else:
        menucal()
def koefisien():
    #Koefisien 
    print('''
    Rata-rata nilai matematika adalah 8,25 dan simpangan baku 0,75. Hitunglah besar koefisien
    variasinya ?
    
    x_bar = rata rata (ex 8.25)
    sd = simpangan baku (ex 0.75)
    \n''')
    
    x_bar = input("Masukkan Nilai rata rata(x_bar)= ")
    sd = input("Masukkan Nilai Simpangan baku(sd)= ")
    
    kv = float(sd)/float(x_bar)*100

    print(f'hasil = {round(kv, 2)}%')
    print('\n')

    back = input('Coba lagi [Y/N] ? ').upper()
    if back == 'Y':
        print('\n')
        return koefisien()
    else:
        menucal()

def menucal():
    import os
    import time
    from Code import menu as m

    os.system('cls')
    os.system('color 9')
    print('Code created by @xcl')
    print(120*"=")
    print('0. Exit')
    print('1. Kaidah pencacahan')
    print('2. Filling slot')
    print('3. Notasi faktorial')
    print('4. Permutasi unsur berbeda')
    print('5. Permutasi unsur sama')
    print('6. Permutasi Siklis')
    print('7. Kombinasi')
    print('8. Ruang Sampel')
    print('9. Peluang kejadian')
    print('10. Frekuensi harapan')
    print('11. Peluang kejadian saling lepas')
    print('12. Peluang kejadian saling bebas')
    print('13. Statistika')
    print('14. Ukuran pemusatan data tunggal')
    print('15. Angka baku')
    print('16. Angka baku(ex.2)')
    print('17. Koefisien')
    print(120*"=")
    i = input("Code Program > ")
    print('\n')
    
    if i=='1':
        kaidah_pencacahan()
        os.system('cls')
        print('Code created by @xcl')
    
    elif i=='2':
        filling_slot()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='3':
        notasi_faktorial()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='4':
        permutasi_unsur_berbeda()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='5':
        permutasi_unsur_sama()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='6':
        permutasi_siklis()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='7':
        kombinasi()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='8':
        ruang_sampel()
        os.system('cls')
        print('Code created by @xcl')
    
    elif i=='9':
        peluang_kejadian()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='10':
        frekuensi_harapan()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='11':
        peluang_kejadian_saling_lepas()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='12':
        peluang_kejadian_saling_bebas()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='13':
        statistika()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='14':
        ukuran_pemusatan_data_tunggal()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='15':
        angka_baku()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='16':
        angka_baku2()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='17':
        koefisien()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='0':
        os.system('cls')
        print('Code created by @xcl')
        m.show_menu()
        
    else:
        os.system('cls')
        os.system('color 4')
        print("Code salah !")
        time.sleep(0.2)
        os.system('cls')
        print('Code created by @xcl')
        return menucal()

# Testing command #
