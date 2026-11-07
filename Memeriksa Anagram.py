def cek_anagram(teks1, teks2):
    teks1 = teks1.lower().replace(" ", "")
    teks2 = teks2.lower().replace(" ", "")
 
    return sorted(teks1) == sorted(teks2)
 
print(cek_anagram("Mata", "Atam"))
