def kelompokkan_nilai(data):
    hasil = {"A": [], "B": [], "C": [], "D": []}
 
    for nama, nilai in data.items():
        if nilai >= 85:
            hasil["A"].append(nama)
        elif nilai >= 70:
            hasil["B"].append(nama)
        elif nilai >= 55:
            hasil["C"].append(nama)
        else:
            hasil["D"].append(nama)
 
    return hasil
 
data = {
    "Andi": 90,
    "Budi": 75,
    "Citra": 60,
    "Dina": 45,
    "Eka": 88
}
 
print(kelompokkan_nilai(data))
