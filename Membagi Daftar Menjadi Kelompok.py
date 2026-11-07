def bagi_kelompok(data, ukuran):
    hasil = []
 
    for i in range(0, len(data), ukuran):
        hasil.append(data[i:i+ukuran])
 
    return hasil
 
print(bagi_kelompok([1, 2, 3, 4, 5, 6, 7], 3))
