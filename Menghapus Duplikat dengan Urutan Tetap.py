def hapus_duplikat(angka):
    hasil = []
    for x in angka:
        if x not in hasil:
            hasil.append(x)
    return hasil
 
print(hapus_duplikat([4, 2, 4, 1, 2, 5, 1]))
