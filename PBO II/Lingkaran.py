import math

# Menghitung keliling lingkaran (2 * π * r)
def keliling_lingkaran(radius):
    return 2 * math.pi * radius

# Menghitung luas lingkaran (π * r^2)
def luas_lingkaran(radius):
    return math.pi * radius ** 2

# Masukkan nilai radius (r) di sini
radius =5
 
keliling = keliling_lingkaran(radius)
luas = luas_lingkaran(radius)

print(f"Keliling lingkaran dengan radius {radius} adalah {keliling:.2f}")
print(f"Luas lingkaran dengan radius {radius} adalah {luas:.2f}")
