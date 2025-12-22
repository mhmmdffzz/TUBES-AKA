import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

"""
Program: Perbandingan Kinerja Algoritma Fibonacci
Deskripsi:
Program ini membandingkan waktu eksekusi algoritma Fibonacci
menggunakan pendekatan rekursif dan iteratif untuk berbagai nilai n.
Hasil ditampilkan dalam bentuk tabel dan grafik.
"""

# =========================
# FIBONACCI REKURSIF
# =========================
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# =========================
# FIBONACCI ITERATIF
# =========================
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# =========================
# DATA UNTUK GRAFIK & TABEL
# =========================
n_values = []
recursive_times = []
iterative_times = []


# =========================
# FUNGSI GRAFIK
# =========================
def update_graph():
    plt.figure(figsize=(8, 6))
    plt.plot(
        n_values,
        recursive_times,
        label="Recursive",
        marker="o",
        linestyle="-"
    )
    plt.plot(
        n_values,
        iterative_times,
        label="Iterative",
        marker="o",
        linestyle="-"
    )
    plt.title("Performance Comparison: Recursive vs Iterative Fibonacci")
    plt.xlabel("Input (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()


# =========================
# FUNGSI TABEL EKSEKUSI
# =========================
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["n", "Recursive Time (s)", "Iterative Time (s)"]

    min_len = min(len(n_values), len(recursive_times), len(iterative_times))
    for i in range(min_len):
        table.add_row([
            n_values[i],
            recursive_times[i],
            iterative_times[i]
        ])

    print(table)


# =========================
# PROGRAM UTAMA
# =========================
def main():
    print("=== Perbandingan Algoritma Fibonacci ===")
    print("Masukkan nilai n (ketik -1 untuk keluar)\n")

    while True:
        try:
            n = int(input("Masukkan nilai n: "))

            if n == -1:
                print("\nProgram selesai. Terima kasih!")
                break

            if n < 0:
                print("Nilai n harus bilangan positif!")
                continue

            n_values.append(n)

            # Waktu eksekusi rekursif
            start_time = time.time()
            fibonacci_recursive(n)
            recursive_times.append(time.time() - start_time)

            # Waktu eksekusi iteratif
            start_time = time.time()
            fibonacci_iterative(n)
            iterative_times.append(time.time() - start_time)

            # Tampilkan tabel
            print_execution_table()

            # Tampilkan grafik
            update_graph()

        except ValueError:
            print("Masukkan angka yang valid!")


# =========================
# EKSEKUSI PROGRAM
# =========================
if __name__ == "__main__":
    main()
