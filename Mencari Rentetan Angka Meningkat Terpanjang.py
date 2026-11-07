def rentetan_meningkat(angka):
    if not angka:
        return []
 
    terbaik = []
    sementara = [angka[0]]
 
    for i in range(1, len(angka)):
        if angka[i] > angka[i-1]:
            sementara.append(angka[i])
        else:
            if len(sementara) > len(terbaik):
                terbaik = sementara
            sementara = [angka[i]]
 
    if len(sementara) > len(terbaik):
        terbaik = sementara
 
    return terbaik
 
print(rentetan_meningkat([2, 4, 6, 1, 3, 5, 7, 2, 4]))
