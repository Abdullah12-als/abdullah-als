def statistik_nilai(nilai):
    return {
        "minimum": min(nilai),
        "maksimum": max(nilai),
        "rata_rata": round(sum(nilai) / len(nilai), 2)
    }
 
print(statistik_nilai([75, 80, 90, 65, 85]))
