import random
import matplotlib.pyplot as plt

# Mengimpor fungsi-fungsi dari modul yang sudah Anda buat
from inisiasipopulasi import inisialisasi_populasi
from EvaluasiFitness import hitung_fitness
from selection import tournament_selection
from crossover import uniform_crossover
from mutation import swap_mutation

# Data barang: (Nama, Keuntungan, Ukuran)
barang = [
    ("Barang1", 10, 5),
    ("Barang2", 40, 4),
    ("Barang3", 30, 6),
    ("Barang4", 50, 3),
    ("Barang5", 35, 7)
]

def run_ga(jumlah_generasi, jumlah_populasi, prob_crossover, prob_mutasi, kapasitas_gudang):
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
        fitness_populasi = [hitung_fitness(individu, barang, kapasitas_gudang) for individu in populasi]

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
            # 1. SELEKSI: Menggunakan Tournament Selection (Digit NIM 1 -> TS)
            parent1, idx1 = tournament_selection(populasi, fitness_populasi)

            available_indices = [i for i in range(len(populasi)) if i != idx1]
            if not available_indices:
                parent2 = parent1
            else:
                parent2, _ = tournament_selection(
                    [populasi[i] for i in available_indices], 
                    [fitness_populasi[i] for i in available_indices]
                )

            # 2. CROSSOVER: Menggunakan Uniform Crossover (Digit NIM 8 -> Uniform)
            if random.random() < prob_crossover:
                anak1, anak2 = uniform_crossover(parent1, parent2)
            else:
                anak1, anak2 = parent1[:], parent2[:]

            # 3. MUTASI: Menggunakan Swap Mutation (Digit NIM 1+8=9 -> Swap)
            if random.random() < prob_mutasi:
                anak1 = swap_mutation(anak1)
            if random.random() < prob_mutasi:
                anak2 = swap_mutation(anak2)

            new_populasi.extend([anak1, anak2])

        # Menggantikan populasi lama dengan yang baru
        populasi = new_populasi[:jumlah_populasi]

    # Visualisasi
    plt.figure(figsize=(12, 7))
    for i in range(jumlah_generasi):
        x = [i + 1] * len(all_fitness[i])
        y = all_fitness[i]
        plt.scatter(x, y, color='gray', alpha=0.1)

    plt.plot(range(1, jumlah_generasi + 1), best_fitness_list, color='blue', label='Keuntungan Tertinggi')
    plt.plot(range(1, jumlah_generasi + 1), worst_fitness_list, color='yellow', label='Keuntungan Terendah')
    plt.plot(range(1, jumlah_generasi + 1), avg_fitness_list, color='red', label='Keuntungan Rata-rata')

    plt.title('Perkembangan Algoritma Genetika (Gudang Toko)')
    plt.xlabel('Generasi')
    plt.ylabel('Total Keuntungan')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Cetak hasil
    selected_items = [barang[i][0] for i in range(len(best_individu)) if best_individu[i] == 1]
    selected_value = hitung_fitness(best_individu, barang, kapasitas_gudang)
    selected_weight = sum([barang[i][2] for i in range(len(best_individu)) if best_individu[i] == 1])

    print(f"\nKeuntungan Maksimal (Fitness): {selected_value}")
    print(f"Total Ukuran Digunakan: {selected_weight} / {kapasitas_gudang}")
    print("Barang yang harus dibeli:")
    for item in selected_items:
        print(f"- {item}")

# Eksekusi skrip
if __name__ == "__main__":
    run_ga(
        jumlah_generasi=50,
        jumlah_populasi=20,
        prob_crossover=0.7,
        prob_mutasi=0.1,
        kapasitas_gudang=15 # Batas maksimal gudang sesuai modul
    )