import random
import matplotlib.pyplot as plt
import numpy as np

# Mengimpor fungsi-fungsi dari file lain
from inisiasipopulasi import inisialisasi_populasi
from EvaluasiFitness import hitung_fitness
from selection import roulette_wheel_selection
from crossover import one_point_crossover
from mutation import swap_mutation

# Data barang: (nama, nilai, berat)
barang = [
    ("Barang1", 60, 10),
    ("Barang2", 100, 20),
    ("Barang3", 120, 30),
    ("Barang4", 90, 25),
    ("Barang5", 69, 11),
    ("Barang6", 70, 9),
    ("Barang7", 80, 15),
    ("Barang8", 90, 10),
    ("Barang9", 25, 3)
]

def run_ga(jumlah_generasi, jumlah_populasi, prob_crossover, prob_mutasi, kapasitas_tas):
    jumlah_gen = len(barang)
    populasi = inisialisasi_populasi(jumlah_populasi, jumlah_gen)

    best_fitness_list = []
    worst_fitness_list = []
    avg_fitness_list = []
    all_fitness = []

    best_individu = None
    best_fitness_overall = 0

    # Proses evolusi selama jumlah generasi yang ditentukan
    for generasi in range(jumlah_generasi):
        fitness_populasi = [hitung_fitness(individu, barang, kapasitas_tas) for individu in populasi]

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
            # Seleksi orang tua menggunakan roulette wheel
            parent1, idx1 = roulette_wheel_selection(populasi, fitness_populasi)

            # Memastikan orang tua kedua berbeda
            available_indices = [i for i in range(len(populasi)) if i != idx1]
            if not available_indices:
                parent2 = parent1
            else:
                parent2, _ = roulette_wheel_selection(
                    [populasi[i] for i in available_indices], 
                    [fitness_populasi[i] for i in available_indices]
                )

            # Crossover untuk menghasilkan anak
            if random.random() < prob_crossover:
                anak1, anak2 = one_point_crossover(parent1, parent2)
            else:
                anak1, anak2 = parent1[:], parent2[:]

            # Mutasi pada anak
            if random.random() < prob_mutasi:
                anak1 = swap_mutation(anak1)
            if random.random() < prob_mutasi:
                anak2 = swap_mutation(anak2)

            # Menambahkan anak ke populasi baru
            new_populasi.extend([anak1, anak2])

        # Menggantikan populasi lama dengan yang baru
        populasi = new_populasi[:jumlah_populasi]

    # Visualisasi plot perkembangan fitness
    plt.figure(figsize=(12, 7))
    for i in range(jumlah_generasi):
        x = [i + 1] * len(all_fitness[i])
        y = all_fitness[i]
        plt.scatter(x, y, color='gray', alpha=0.1)

    plt.plot(range(1, jumlah_generasi + 1), best_fitness_list, color='blue', label='Fitness Tertinggi')
    plt.plot(range(1, jumlah_generasi + 1), worst_fitness_list, color='yellow', label='Fitness Terendah')
    plt.plot(range(1, jumlah_generasi + 1), avg_fitness_list, color='red', label='Fitness Rata-rata')

    plt.title('Perkembangan Nilai Fitness')
    plt.xlabel('Generasi')
    plt.ylabel('Nilai Fitness')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Ekstraksi hasil individu terbaik
    selected_items = [barang[i][0] for i in range(len(best_individu)) if best_individu[i] == 1]
    selected_value = hitung_fitness(best_individu, barang, kapasitas_tas)
    selected_weight = sum([barang[i][2] for i in range(len(best_individu)) if best_individu[i] == 1])

    print(f"\nNilai Fitness Terbaik: {selected_value}")
    print(f"Total Bobot: {selected_weight}")
    print("Barang Terpilih:")
    for item in selected_items:
        print(f"- {item}")

# Eksekusi script
if __name__ == "__main__":
    run_ga(
        jumlah_generasi=50,
        jumlah_populasi=20,
        prob_crossover=0.5,
        prob_mutasi=0.1,
        kapasitas_tas=50
    )