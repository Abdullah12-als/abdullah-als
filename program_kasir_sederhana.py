
print("=== PROGRAM KASIR SEDERHANA ===")

nama_pembeli = input("Nama Pembeli : ").strip().upper()
jumlah_jenis = int(input("Jumlah barang : ").strip())

total_belanja = 0

for i in range(1, jumlah_jenis + 1):
    print(f"\nBarang ke-{i}")

    nama_barang = input("Nama   : ").strip().upper()
    harga = int(input("Harga  : ").strip())
    jumlah = int(input("Jumlah : ").strip())

    subtotal = harga * jumlah
    total_belanja += subtotal

    print(f"Subtotal : Rp{subtotal:,}".replace(",", "."))

# Menentukan diskon
if total_belanja >= 500000:
    diskon = 15
elif total_belanja >= 250000:
    diskon = 10
elif total_belanja >= 100000:
    diskon = 5
else:
    diskon = 0

# Menghitung potongan dan total bayar
potongan = total_belanja * diskon // 100
total_bayar = total_belanja - potongan

# Menampilkan struk
print("\n========== STRUK ==========")
print(f"Pembeli       : {nama_pembeli}")
print(f"Total Belanja : Rp{total_belanja:,}".replace(",", "."))
print(f"Diskon        : {diskon}%")
print(f"Potongan      : Rp{potongan:,}".replace(",", "."))
print(f"Total Bayar   : Rp{total_bayar:,}".replace(",", "."))
print("===========================")
