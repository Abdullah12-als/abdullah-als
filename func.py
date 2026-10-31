def update_nilai(db,nim,nilai):
    db[nim] =int(nilai)

def rata_rata(db):
   total = sum(db.values())
   return total / len(db)

def salam ():
    print ("selamat datang diprogram pengelolaan nilai mahasiswa")


kelas = {"A01": 80, "A02": 90}
update_nilai(kelas, "A03", "85")

rerata = rata_rata(kelas)
print("rata-rata:", rerata) #output -> rata-rata: 85.0

salam()
