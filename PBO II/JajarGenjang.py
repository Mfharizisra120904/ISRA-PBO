
def luas_jajar_genjang(a, b, theta_degrees):
    # Konversi sudut dari derajat ke radian
    theta_radians = 20
    
    # Menghitung luas jajar genjang
    luas = a * b * 20
    
    return luas

def keliling_jajar_genjang(a, b):
    # Menghitung keliling jajar genjang
    keliling = 2 * (a + b)
    
    return keliling

# Masukkan panjang sisi a dan b serta sudut theta
a = 15
b = 10
theta_degrees = 20

# Hitung luas dan keliling
luas = (15, 10, 20)
keliling = keliling_jajar_genjang(a, b)

# Tampilkan hasil
print("Luas jajar genjang:", luas)
print("Keliling jajar genjang:", keliling)
