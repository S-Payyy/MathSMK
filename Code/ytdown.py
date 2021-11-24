def ytdown():
    from pytube import YouTube
    url = input('Masukan Link Youtube > ') 
    down = YouTube(url)
    print(f'\n> {down.title} <\n')
    down = down.streams.get_lowest_resolution()
    down.download()
    '''
    x = input('Pilih Resolusi Video\n1. Low\n2. High\nPilih Nomer > ')
    if x == '1': 
        low = down.streams.get_lowest_resolution()
        low.download()
    elif x == '2': 
        high = down.streams.get_highest_resolution()
        high.download()
    else: 
        ytdown()
    '''