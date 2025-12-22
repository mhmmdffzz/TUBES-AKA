import sys
import time
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable


# SET RECURSION LIMIT
sys.setrecursionlimit(6000)


# ALGORITMA FAKTORIAL
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# BENCHMARK FUNCTION
def measure_time(func, n, repeat):
    start = time.perf_counter()
    for _ in range(repeat):
        func(n)
    end = time.perf_counter()
    return ((end - start) / repeat) * 1000  # ms


# DATA
n_values = []
recursive_times = []
iterative_times = []


# GRAFIK (CURVE)
def update_graph():
    plt.figure(figsize=(8, 6))

    # Iterative
    x_iter = np.array(n_values)
    y_iter = np.array(iterative_times)

    if len(x_iter) > 1:
        x_smooth = np.linspace(x_iter.min(), x_iter.max(), 300)
        y_smooth = np.interp(x_smooth, x_iter, y_iter)
        plt.plot(x_smooth, y_smooth, label="Iterative")
        plt.scatter(x_iter, y_iter)

    # Recursive
    rec_n = []
    rec_t = []
    for i in range(len(n_values)):
        if recursive_times[i] is not None:
            rec_n.append(n_values[i])
            rec_t.append(recursive_times[i])

    if len(rec_n) > 1:
        x_rec = np.array(rec_n)
        y_rec = np.array(rec_t)
        x_rec_smooth = np.linspace(x_rec.min(), x_rec.max(), 300)
        y_rec_smooth = np.interp(x_rec_smooth, x_rec, y_rec)
        plt.plot(x_rec_smooth, y_rec_smooth, label="Recursive")
        plt.scatter(x_rec, y_rec)

    plt.title("Performance Benchmark: Iterative vs Recursive")
    plt.xlabel("Input (n)")
    plt.ylabel("Execution Time (ms)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# TABEL
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["n", "Recursive Time (ms)", "Iterative Time (ms)"]

    for i in range(len(n_values)):
        rec_time = (
            f"{recursive_times[i]:.4f}"
            if recursive_times[i] is not None
            else "N/A"
        )
        table.add_row([
            n_values[i],
            rec_time,
            f"{iterative_times[i]:.4f}"
        ])

    print(table)


# PROGRAM UTAMA
print("Program Analisis Faktorial Iteratif vs Rekursif")

while True:
    try:
        n = int(input("Masukkan nilai n (-1 untuk keluar): "))

        if n == -1:
            break
        if n < 0:
            continue

        n_values.append(n)
        repeat = max(3000 - (n * 20), 50)

        if n <= 5000:
            recursive_times.append(
                measure_time(factorial_recursive, n, repeat)
            )
        else:
            recursive_times.append(None)

        iterative_times.append(
            measure_time(factorial_iterative, n, repeat)
        )

        print_execution_table()
        update_graph()

    except ValueError:
        pass
