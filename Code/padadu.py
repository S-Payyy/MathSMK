def peluang_dadu():
    
    dadu1 = [1,2,3,4,5,6]
    dadu2 = [1,2,3,4,5,6]
    dadu3 = [1,2,3,4,5,6]
    dadu4 = [1,2,3,4,5,6]
    dadu5 = [1,2,3,4,5,6]

    # jd(x) = jumlah dadu
    jenis = input('\nBanyak dadu : ')
    if jenis == '2':
        soal = input('\nPeluang Muncul Angka dadu : ')
        x = int(soal)
        h = 0

        a1 = dadu1[0]+dadu2[0]
        a2 = dadu1[0]+dadu2[1]
        a3 = dadu1[0]+dadu2[2]
        a4 = dadu1[0]+dadu2[3]
        a5 = dadu1[0]+dadu2[4]
        a6 = dadu1[0]+dadu2[5]

        b1 = dadu1[1]+dadu2[0]
        b2 = dadu1[1]+dadu2[1]
        b3 = dadu1[1]+dadu2[2]
        b4 = dadu1[1]+dadu2[3]
        b5 = dadu1[1]+dadu2[4]
        b6 = dadu1[1]+dadu2[5]
        
        c1 = dadu1[2]+dadu2[0]
        c2 = dadu1[2]+dadu2[1]
        c3 = dadu1[2]+dadu2[2]
        c4 = dadu1[2]+dadu2[3]
        c5 = dadu1[2]+dadu2[4]
        c6 = dadu1[2]+dadu2[5]
        
        d1 = dadu1[3]+dadu2[0]
        d2 = dadu1[3]+dadu2[1]
        d3 = dadu1[3]+dadu2[2]
        d4 = dadu1[3]+dadu2[3]
        d5 = dadu1[3]+dadu2[4]
        d6 = dadu1[3]+dadu2[5]
        
        e1 = dadu1[4]+dadu2[0]
        e2 = dadu1[4]+dadu2[1]
        e3 = dadu1[4]+dadu2[2]
        e4 = dadu1[4]+dadu2[3]
        e5 = dadu1[4]+dadu2[4]
        e6 = dadu1[4]+dadu2[5]
        
        f1 = dadu1[5]+dadu2[0]
        f2 = dadu1[5]+dadu2[1]
        f3 = dadu1[5]+dadu2[2]
        f4 = dadu1[5]+dadu2[3]
        f5 = dadu1[5]+dadu2[4]
        f6 = dadu1[5]+dadu2[5]

        if a1 == x:
            h += 1
            
        if a2 == x:
            h += 1

        if a3 == x:
            h += 1

        if a4 == x:
            h += 1

        if a5 == x:
            h += 1

        if a6 == x:
            h += 1

        if b1 == x:
            h += 1

        if b2 == x:
            h += 1

        if b3 == x:
            h += 1

        if b4 == x:
            h += 1

        if b5 == x:
            h += 1

        if b6 == x:
            h += 1

        if c1 == x:
            h += 1
            
        if c2 == x:
            h += 1

        if c3 == x:
            h += 1

        if c4 == x:
            h += 1

        if c5 == x:
            h += 1

        if c6 == x:
            h += 1

        if d1 == x:
            h += 1

        if d2 == x:
            h += 1

        if d3 == x:
            h += 1

        if d4 == x:
            h += 1

        if d5 == x:
            h += 1

        if d6 == x:
            h += 1

        if e1 == x:
            h += 1

        if e2 == x:
            h += 1

        if e3 == x:
            h += 1
            
        if e4 == x:
            h += 1

        if e5 == x:
            h += 1

        if e6 == x:
            h += 1

        if f1 == x:
            h += 1

        if f2 == x:
            h += 1

        if f3 == x:
            h += 1

        if f4 == x:
            h += 1

        if f5 == x:
            h += 1

        if f6 == x:
            h += 1
        
        pa = f'{h}/36' 
        print(f'\nHasil adalah : {pa}\n')
        
    else :
        peluang_dadu()

    def jd3():
        pass
