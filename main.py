from aritmatika import *
from konversi import *
from ubah_bilangan import *

while True:
    print("\n===== MENU UTAMA =====")
    print("1. Aritmatika")
    print("2. Konversi")
    print("3. Ubah Bilangan")
    print("4. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        print("\n--- Menu Aritmatika ---")
        print("1. Penjumlahan")
        print("2. Perpangkatan")
        print("3. Perkalian")

        sub = input("Pilih: ")

        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))

        if sub == "1":
            print("Hasil =", penjumlahan(a, b))
        elif sub == "2":
            print("Hasil =", perpangkatan(a, b))
        elif sub == "3":
            print("Hasil =", perkalian(a, b))
        else:
            print("Pilihan tidak tersedia.")

    elif pilih == "2":
        print("\n--- Menu Konversi ---")
        print("1. CM ke M")
        print("2. M ke CM")

        sub = input("Pilih: ")

        nilai = float(input("Masukkan nilai: "))

        if sub == "1":
            print("Hasil =", cm_ke_m(nilai), "meter")
        elif sub == "2":
            print("Hasil =", m_ke_cm(nilai), "cm")
        else:
            print("Pilihan tidak tersedia.")

    elif pilih == "3":
        print("\n--- Menu Ubah Bilangan ---")
        print("1. Desimal ke Biner")
        print("2. Desimal ke Oktal")
        print("3. Desimal ke Heksadesimal")

        sub = input("Pilih: ")

        nilai = int(input("Masukkan bilangan desimal: "))

        if sub == "1":
            print("Hasil =", desimal_ke_biner(nilai))
        elif sub == "2":
            print("Hasil =", desimal_ke_oktal(nilai))
        elif sub == "3":
            print("Hasil =", desimal_ke_heksadesimal(nilai))
        else:
            print("Pilihan tidak tersedia.")

    elif pilih == "4":
        print("Terima kasih telah menggunakan program.")
        break

    else:
        print("Pilihan tidak valid.")