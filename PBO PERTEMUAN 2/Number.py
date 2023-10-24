def number_to_words(number):
    units = ['Nol', 'Satu', 'Dua', 'Tiga', 'Empat', 'Lima', 'Enam', 'Tujuh', 'Delapan', 'Sembilan']
    teens = ['Sepuluh', 'Sebelas', 'Dua Belas', 'Tiga Belas', 'Empat Belas', 'Lima Belas', 'Enam Belas', 'Tujuh Belas', 'Delapan Belas', 'Sembilan Belas']
    tens = ['', 'Sepuluh', 'Dua Puluh', 'Tiga Puluh', 'Empat Puluh', 'Lima Puluh', 'Enam Puluh', 'Tujuh Puluh', 'Delapan Puluh', 'Sembilan Puluh']
    thousands = ['', 'Ribu', 'Juta', 'Miliar', 'Triliun']

    if number < 10:
        return units[number]
    elif number < 20:
        return teens[number - 10]
    elif number < 100:
        return tens[number // 10] + (' ' + units[number % 10] if number % 10 > 0 else '')
    else:
        words = ''
        for i in range(4):
            if number % 1000 > 0:
                words = number_to_words(number % 1000) + ' ' + thousands[i] + ' ' + words
            number //= 1000
        return words

if __name__ == "__main__":
    number = int(input("Masukkan angka: "))
    words = number_to_words(number)
    print(f"{number} dalam bahasa Indonesia adalah: {words}")
