def terbesar_kedua(angka):
    unik = sorted(set(angka), reverse=True)
 
    if len(unik) < 2:
        return None
 
    return unik[1]
 
print(terbesar_kedua([12, 7, 20, 20, 15]))
