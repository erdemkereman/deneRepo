def hesap_makinesi():
    print("Hesap Makinesi")
    print("1: Toplama\n2: Çıkarma\n3: Çarpma\n4: Bölme")

    try:
        secim = int(input("Bir işlem seçin (1/2/3/4): "))
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))

        if secim == 1:
            print(f"Sonuç: {sayi1 + sayi2}")
        elif secim == 2:
            print(f"Sonuç: {sayi1 - sayi2}")
        elif secim == 3:
            print(f"Sonuç: {sayi1 * sayi2}")
        elif secim == 4:
            if sayi2 != 0:
                print(f"Sonuç: {sayi1 / sayi2}")
            else:
                print("Bir sayı 0'a bölünemez!")
        else:
            print("Geçersiz bir işlem seçtiniz.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

hesap_makinesi()
