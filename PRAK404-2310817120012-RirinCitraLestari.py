def calculator():
    while True:
        print("Pilih program\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Exit")
        choice = int(input("Masukkan Pilihan: "))

        if choice == 5:
            print(f"Terimakasih, telah menggunakan kalkulator Ririn")
            break

        if choice < 1 or choice > 4:
            print("Input anda salah, silahkan coba lagi")
            continue

        num1 = float(input("Masukkan nilai pertama: "))
        num2 = float(input("Masukkan nilai kedua: "))

        if choice == 1:
            result = num1 + num2
            operation = "Penjumlahan"
        elif choice == 2:
            result = num1 - num2
            operation = "Pengurangan"
        elif choice == 3:
            result = num1 * num2
            operation = "Perkalian"
        elif choice == 4:
            if num2 == 0:
                print("Error: Pembagian dengan 0")
                continue
            result = num1 / num2
            operation = "Pembagian"

        print(f"Hasil {operation} antara {num1:.2f} dengan {num2:.2f} adalah {result:.2f}")

if __name__ == "__main__":
    calculator()
