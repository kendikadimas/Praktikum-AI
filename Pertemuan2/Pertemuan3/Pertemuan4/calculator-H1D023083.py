import numpy as np
import math

# Struktur data buat nampung operasi
OPERATIONS = {
    '+': lambda a, b: np.add(a, b),
    '-': lambda a, b: np.subtract(a, b),
    '*': lambda a, b: np.multiply(a, b),
    '/': lambda a, b: "Error: Division by zero" if b == 0 else np.divide(a, b),
    'akar dua': lambda a: "Error: Cannot calculate square root of a negative number" if a < 0 else math.sqrt(a)
}

# Struktur kontrol buat nampilkan menu 
def display_menu():
    print("\nSelamat Datang di Kalkulator!")
    print("Operasi yang didukung:")
    for op in OPERATIONS.keys():
        print(f"  - {op}")

# Struktur kontrol buat meminta user input
def get_user_input(operation):
    try:
        if operation == 'akar dua':
            num1 = float(input("Masukkan angka: "))
            return num1, None  
        else:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))
            return num1, num2
    except ValueError:
        print("Input tidak valid! Silakan masukkan angka.")
        return None, None

# Struktur kontrol buat memproses operasi
def process_operation(operation, num1, num2):
    if operation in OPERATIONS:
        func = OPERATIONS[operation]
        if operation == 'akar dua':
            return func(num1)
        else:
            return func(num1, num2)
    else:
        return "Operasi tidak valid!"

# Struktur kontrol buat menjalankan kalkulator
def kalkulator():
    while True:
        display_menu()
        operation = input("Masukkan operasi yang diinginkan: ").strip().lower()

        if operation not in OPERATIONS:
            print("Operasi tidak valid! Silakan pilih operasi yang benar.")
            continue

        num1, num2 = get_user_input(operation)
        if num1 is None:  # Jika input tidak valid, ulangi loop
            continue

        result = process_operation(operation, num1, num2)
        print(f"Hasil: {result}")

        lagi = input("Ingin menggunakan kalkulator lagi? (y/n): ").strip().lower()
        if lagi != 'y':
            print("Terima kasih telah menggunakan kalkulator!")
            break

if __name__ == "__main__":
    kalkulator()
