def pasangan_target(angka, target):
    hasil = set()
 
    for i in range(len(angka)):
        for j in range(i + 1, len(angka)):
            if angka[i] + angka[j] == target:
                pasangan = tuple(sorted((angka[i], angka[j])))
                hasil.add(pasangan)
 
    return sorted(hasil)
 
print(pasangan_target([1, 2, 3, 4, 5, 3], 6))
