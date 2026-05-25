# README – Praktikum Kecerdasan Buatan Pertemuan 9

# NAMA : YOGA ADI NUGRAHA
# NIM  : H1D024118
# SHIFT : D

## Implementasi Algoritma Genetika pada Knapsack Problem

### Identitas Praktikum

* **Mata Kuliah** : Praktikum Kecerdasan Buatan
* **Modul/Pertemuan** : Pertemuan 9 – Algoritma Genetika
* **Topik** : Genetic Algorithm untuk Optimasi Knapsack Problem

---

# Deskripsi Program

Program ini merupakan implementasi **Algoritma Genetika (Genetic Algorithm)** menggunakan bahasa pemrograman Python untuk menyelesaikan **Knapsack Problem**.

Knapsack Problem adalah permasalahan optimasi dalam memilih kombinasi barang terbaik berdasarkan:

* **Nilai/Fitness tertinggi**
* **Batas kapasitas maksimum tas**

Pada program ini, Algoritma Genetika digunakan untuk mencari kombinasi barang paling optimal dengan memanfaatkan proses:

1. Inisialisasi populasi
2. Evaluasi fitness
3. Seleksi parent
4. Crossover
5. Mutasi
6. Evolusi generasi

---

# Tujuan Praktikum

Tujuan dari praktikum ini adalah:

* Memahami konsep dasar Algoritma Genetika
* Mengetahui proses evolusi solusi menggunakan Genetic Algorithm
* Mengimplementasikan Algoritma Genetika pada kasus nyata
* Menyelesaikan Knapsack Problem menggunakan pendekatan optimasi berbasis populasi

---

# Konsep Dasar Algoritma Genetika

Algoritma Genetika merupakan metode optimasi yang terinspirasi dari proses evolusi biologis dan seleksi alam.

Dalam implementasi ini:

* Setiap solusi direpresentasikan sebagai **kromosom**
* Setiap gen bernilai:

  * `1` → barang dipilih
  * `0` → barang tidak dipilih

Contoh kromosom:

```python
[1, 0, 1, 1, 0]
```

Artinya:

* Barang ke-1 dipilih
* Barang ke-3 dipilih
* Barang ke-4 dipilih

---

# Struktur Program

Program terdiri dari beberapa file utama:

| File                  | Fungsi                        |
| --------------------- | ----------------------------- |
| `inisiasipopulasi.py` | Membuat populasi awal         |
| `EvaluasiFitness.py`  | Menghitung fitness individu   |
| `selection.py`        | Seleksi parent                |
| `crossover.py`        | Proses crossover              |
| `mutation.py`         | Proses mutasi                 |
| `main.py`             | Menjalankan seluruh algoritma |

---

# Tahapan Algoritma

## 1. Inisialisasi Populasi

Tahap awal dilakukan dengan membuat populasi awal secara acak.

Contoh:

```python
[1,0,1,1,0,1,0,0,1]
```

Setiap individu merepresentasikan solusi potensial.

---

## 2. Evaluasi Fitness

Fitness dihitung berdasarkan:

* Total nilai barang
* Total bobot barang

Jika bobot melebihi kapasitas tas, maka fitness bernilai `0`.

Rumus sederhana:

[
Fitness = \sum nilai\ barang
]

dengan syarat:

[
Total\ Bobot \leq Kapasitas\ Tas
]

---

## 3. Seleksi

Program menggunakan metode:

* **Roulette Wheel Selection**
* **Tournament Selection**

Seleksi bertujuan memilih parent terbaik untuk menghasilkan generasi baru.

---

## 4. Crossover

Crossover digunakan untuk menggabungkan dua parent menjadi offspring baru.

Metode yang digunakan:

* One Point Crossover
* Two Point Crossover
* Uniform Crossover

Contoh:

Parent 1:

```python
[1,0,1,1,0]
```

Parent 2:

```python
[0,1,0,0,1]
```

Hasil crossover:

```python
[1,0,1,0,1]
```

---

## 5. Mutasi

Mutasi dilakukan untuk menjaga keberagaman populasi agar algoritma tidak terjebak pada solusi lokal.

Metode mutasi:

* Swap Mutation
* Inversion Mutation
* Uniform Mutation

---

## 6. Evolusi Generasi

Semua proses diulang selama sejumlah generasi tertentu hingga diperoleh solusi terbaik.

---

# Library yang Digunakan

Program menggunakan beberapa library berikut:

```python
import random
import matplotlib.pyplot as plt
import numpy as np
```

---

# Cara Menjalankan Program

## 1. Install Library

```bash
pip install matplotlib numpy
```

---

## 2. Jalankan Program

```bash
python main.py
```

---

# Hasil Output Program

Berikut hasil yang diperoleh setelah program dijalankan:

```bash
Nilai Fitness Terbaik: 334
Total Bobot: 48
Barang Terpilih:
- Barang5
- Barang6
- Barang7
- Barang8
- Barang9
```

---

# Analisis Hasil

Berdasarkan hasil pengujian:

* Algoritma berhasil menemukan kombinasi barang optimal
* Total fitness terbaik yang diperoleh adalah **334**
* Total bobot barang adalah **48**, sehingga masih memenuhi batas kapasitas tas yaitu **50**
* Barang yang dipilih merupakan kombinasi paling optimal berdasarkan nilai dan bobot

Kombinasi barang terbaik:

| Barang  | Status  |
| ------- | ------- |
| Barang5 | Dipilih |
| Barang6 | Dipilih |
| Barang7 | Dipilih |
| Barang8 | Dipilih |
| Barang9 | Dipilih |

---

# Visualisasi Fitness

Program juga menampilkan grafik perkembangan fitness:

* Fitness tertinggi
* Fitness terendah
* Fitness rata-rata

Grafik digunakan untuk melihat proses evolusi populasi pada setiap generasi.

---

# Kesimpulan

Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa:

1. Algoritma Genetika mampu menyelesaikan masalah optimasi Knapsack Problem dengan baik.
2. Proses seleksi, crossover, dan mutasi berperan penting dalam menghasilkan solusi optimal.
3. Semakin banyak generasi, peluang menemukan solusi terbaik menjadi lebih besar.
4. Genetic Algorithm sangat efektif digunakan pada permasalahan optimasi kompleks.

---

# Dokumentasi Output

```bash
PS D:\KULIAH UNSOED SMS 4\Praktikum Kecerdasan Buatan> python main.py

Nilai Fitness Terbaik: 334
Total Bobot: 48
Barang Terpilih:
- Barang5
- Barang6
- Barang7
- Barang8
- Barang9
```

---

# Repository GitHub

Format repository yang digunakan:

```bash
H1D024118-PraktikumKB-Pertemuan9
```

Contoh:

```bash
H1D024118-PraktikumKB-Pertemuan9
```


