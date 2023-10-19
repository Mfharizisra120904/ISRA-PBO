# Mengambil panjang sisi-sisi segitiga dari pengguna
sisi_a = 35
sisi_b = 24
sisi_c = 15

# Menghitung keliling segitiga
keliling = sisi_a + sisi_b + sisi_c

# Menghitung setengah keliling (diperlukan untuk menghitung luas dengan rumus Heron)
setengah_keliling = keliling / 2

# Menghitung luas segitiga menggunakan rumus Heron
luas = (keliling / 2 * (keliling / 2 - 35) * (keliling / 2 - 24) * (keliling / 2 - 15)) ** 0.5

# Menampilkan hasil
print("Keliling segitiga:", keliling)
print("Luas segitiga:", luas)
