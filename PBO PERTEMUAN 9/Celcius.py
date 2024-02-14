    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    def celsius_to_kelvin(celsius):
        kelvin = celsius + 273.15
        return kelvin
    # Mengambil input suhu dalam Celsius dari pengguna
    celsius_temperature = float(input("Masukkan suhu dalam Celsius: "))

    # Menghitung konversi suhu
    fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
    kelvin_temperature = celsius_to_kelvin(celsius_temperature)

    # Menampilkan hasil konversi
    print(f"{celsius_temperature} Celsius setara dengan {fahrenheit_temperature:.2f} Fahrenheit")
    print(f"{celsius_temperature} Celsius setara dengan {kelvin_temperature:.2f} Kelvin")
