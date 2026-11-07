def frekuensi_kata(kalimat):
    kalimat = kalimat.lower()
    kalimat = kalimat.replace(",", "").replace(".", "")
 
    hasil = {}
    for kata in kalimat.split():
        hasil[kata] = hasil.get(kata, 0) + 1
 
    return hasil
 
print(frekuensi_kata("Python mudah, python menarik. Belajar Python"))
