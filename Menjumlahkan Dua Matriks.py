def jumlah_matriks(matriks1, matriks2):
    if len(matriks1) != len(matriks2):
        return None
 
    if any(len(a) != len(b) for a, b in zip(matriks1, matriks2)):
        return None
 
    hasil = []
    for i in range(len(matriks1)):
        baris = []
        for j in range(len(matriks1[i])):
            baris.append(matriks1[i][j] + matriks2[i][j])
        hasil.append(baris)
 
    return hasil
 
m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]
 
print(jumlah_matriks(m1, m2))
