import random
import matplotlib.pyplot as plt
import numpy as np
from populasi import inisialisasi_populasi
from evaluasiFitness import hitung_fitness
from selection import tournament_selection
from crossover import one_point_crossover
from mutation import uniform_mutation

# data barang (nama, keuntungan, bobot)
barang = [
    ("barang1", 10, 5),
    ("barang2", 40, 4),
    ("barang3", 30, 6),
    ("barang4", 50, 3),
    ("barang5", 35, 7)
]

def run_ga(jumlah_generasi, jumlah_populasi, prob_crossover, prob_mutasi, max_gudang):
    # Menentukan jumlah gen berdasarkan jumlah barang
    jumlah_gen = len(barang)

    # Inisialisasi populasi awal
    populasi = inisialisasi_populasi(jumlah_populasi, jumlah_gen)
    
    # List untuk menyimpan nilai fitness terbaik, terburuk, dan rata-rata setiap generasi
    best_fitness_list = []
    worst_fitness_list = []
    avg_fitness_list = []
    all_fitness = []

    # Variabel untuk menyimpan individu terbaik secara keseluruhan
    best_individu = None
    best_fitness_overall = 0

    # Proses evolusi selama sejumlah generasi
    for generasi in range(jumlah_generasi):
        # Evaluasi fitness untuk setiap individu dalam populasi
        fitness_populasi = [hitung_fitness(individu, barang, max_gudang) for individu in populasi]

        # Menyimpan nilai fitness terbaik, terburuk, dan rata-rata untuk generasi ini
        best_fitness = max(fitness_populasi)
        worst_fitness = min(fitness_populasi)
        avg_fitness = sum(fitness_populasi) / len(fitness_populasi)
        best_fitness_list.append(best_fitness)
        worst_fitness_list.append(worst_fitness)
        avg_fitness_list.append(avg_fitness)
        all_fitness.append(fitness_populasi.copy())

        # Menyimpan individu terbaik secara keseluruhan
        if best_fitness > best_fitness_overall:
            best_fitness_overall = best_fitness
            index_best = fitness_populasi.index(best_fitness)
            best_individu = populasi[index_best]
            
        new_populasi = []

        # Membentuk populasi baru
        while len(new_populasi) < jumlah_populasi:
            # Seleksi menggunakan tournament selection
            parent1 = tournament_selection(populasi, fitness_populasi)
            parent2 = tournament_selection(populasi, fitness_populasi)

            # Crossover dengan probabilitas tertentu
            if random.random() < prob_crossover:
                offspring1, offspring2 = one_point_crossover(parent1, parent2)
            else:
                offspring1, offspring2 = parent1.copy(), parent2.copy()

            # Mutasi dengan probabilitas tertentu
            offspring1 = uniform_mutation(offspring1, prob_mutasi)
            offspring2 = uniform_mutation(offspring2, prob_mutasi)

            new_populasi.append(offspring1)
            if len(new_populasi) < jumlah_populasi:
                new_populasi.append(offspring2)

        populasi = new_populasi

    # Menampilkan grafik fitness
    plt.figure(figsize=(12, 7))

    # Plot semua nilai fitness individu dalam setiap generasi
    for i in range(jumlah_generasi):
        x = [i+1]*len(all_fitness[i])
        y = all_fitness[i]
        plt.scatter(x, y, color='gray', alpha=0.1)

    # Plot nilai fitness terbaik, terburuk, dan rata-rata
    plt.plot(range(1, jumlah_generasi+1), best_fitness_list, color='blue', label='Fitness Tertinggi')
    plt.plot(range(1, jumlah_generasi+1), worst_fitness_list, color='yellow', label='Fitness Terendah')
    plt.plot(range(1, jumlah_generasi+1), avg_fitness_list, color='red',label='Fitness Rata-rata')

    plt.title('Perkembangan Nilai Fitness')
    plt.xlabel('Generasi')
    plt.ylabel('Nilai Fitness')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Menampilkan barang yang terpilih dalam knapsack terbaik
    selected_items = [barang[i][0] for i in range(len(best_individu)) if best_individu[i] == 1]
    selected_value = hitung_fitness(best_individu, barang, max_gudang)
    selected_weight = sum([barang[i][2] for i in range(len(best_individu)) if best_individu[i] == 1])

    print(f"\nNilai Fitness Terbaik: {selected_value}")
    print(f"Total Bobot: {selected_weight}")
    print("Barang Terpilih:")
    for item in selected_items:
        print(f"- {item}")

# Menjalankan algoritma genetika dengan parameter yang ditentukan
run_ga(
    jumlah_generasi=100,
    jumlah_populasi=50,
    prob_crossover=0.8,
    prob_mutasi=0.03,
    max_gudang=15
)