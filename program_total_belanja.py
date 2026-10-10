print("=== PROGRAM TOTAL BELANJA ===")

nama_barang = input("Nama barang: ")
harga = float(input("Harga barang: Rp"))
jumlah = int(input("Jumlah barang: "))

# Menghitung total
total = harga * jumlah

# Diskon 10%
diskon = total * 10 / 100
total_bayar = total - diskon

# Ringkasan transaksi
print("\n=== RINGKASAN TRANSAKSI ===")
print("Nama barang :", nama_barang)
print("Harga       : Rp", harga)
print("Jumlah      :", jumlah)
print("Total       : Rp", total)
print("Diskon 10%  : Rp", diskon)
print("Total bayar : Rp", total_bayar)
