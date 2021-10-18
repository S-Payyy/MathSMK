# Penghitung Wr ML 
# xcl gabut 

tMatch = input('Total match Anda : ')
tWr = input('Total Win Rate Anda :')
wrReq = input('Berapa Win Rate yang anda inginkan : ')


if (int(wrReq) == 100):
    print('Ga bisa cok!!')
elif (int(wrReq) >= 100):
    print('Ngadi ngadi. . .')
elif (int(wrReq <= tWr)):
    tWin = int(tMatch) * (int(tWr) / 100)
    tLose = int(tMatch) - int(tWin)
    sisaWr = 100 - int(wrReq)
    wrResult = 100 / int(sisaWr)
    seratusPersen = int(tLose) * int(wrResult)
    final = int(seratusPersen) - int(tMatch)
    lose = abs(final)
    print(f'Anda membutuhkan {lose} lose untuk mendapatkan Win Rate {wrReq}%')
else:
    tWin = int(tMatch) * (int(tWr) / 100)
    tLose = int(tMatch) - int(tWin)
    sisaWr = 100 - int(wrReq)
    wrResult = 100 / int(sisaWr)
    seratusPersen = int(tLose) * int(wrResult)
    final = int(seratusPersen) - int(tMatch)
    print(f'Anda membutuhkan {final} win tanpa lose untuk mendapatkan Win Rate {wrReq}%')