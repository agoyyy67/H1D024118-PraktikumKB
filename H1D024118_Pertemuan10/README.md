# README – Praktikum Kecerdasan Buatan Pertemuan 10

# NAMA : YOGA ADI NUGRAHA
# NIM  : H1D024118
# SHIFT : D

## Implementasi Algoritma Genetika 2 pada Knapsack Problem

### Identitas Praktikum

* **Mata Kuliah** : Praktikum Kecerdasan Buatan
* **Modul/Pertemuan** : Pertemuan 10 – Algoritma Genetika 2
* **Topik** : Optimasi Knapsack Problem Menggunakan Genetic Algorithm

---

# Deskripsi Program

Program ini merupakan implementasi lanjutan dari **Algoritma Genetika (Genetic Algorithm)** untuk menyelesaikan permasalahan **Knapsack Problem**.

Pada studi kasus ini, sebuah toko memiliki kapasitas gudang terbatas. Program bertujuan menentukan kombinasi barang terbaik yang harus dibeli agar:

* keuntungan maksimal dapat diperoleh,
* kapasitas gudang tidak melebihi batas yang ditentukan.

Algoritma Genetika digunakan karena mampu mencari solusi optimal melalui proses evolusi populasi secara bertahap.

---

# Tujuan Praktikum

Tujuan dari praktikum ini adalah:

* Memahami implementasi lanjutan Algoritma Genetika
* Menerapkan konsep optimasi pada kasus nyata
* Menggunakan metode seleksi, crossover, dan mutasi berdasarkan aturan NIM
* Menentukan solusi terbaik pada Knapsack Problem

---

# Dasar Teori

Algoritma Genetika merupakan algoritma optimasi yang terinspirasi dari proses evolusi biologis seperti:

* seleksi alam,
* crossover,
* mutasi.

Setiap solusi direpresentasikan dalam bentuk kromosom biner:

```python id="xxp5m1"
[1, 0, 1, 1, 0]
```

Keterangan:

* `1` → barang dipilih
* `0` → barang tidak dipilih

---

# Studi Kasus

Permasalahan yang diselesaikan:

> Sebuah toko memiliki gudang dengan ukuran maksimal tertentu. Tentukan barang apa saja yang harus dibeli agar keuntungan maksimal dapat diperoleh tanpa melebihi kapasitas gudang.

---

# Metode Berdasarkan NIM

NIM:

```text
H1D024118
```

Dua digit terakhir:

```text
18
```

## Penentuan Metode

| Langkah   | Digit     | Metode                    |
| --------- | --------- | ------------------------- |
| Seleksi   | 1         | Tournament Selection (TS) |
| Crossover | 8         | Uniform Crossover         |
| Mutasi    | 1 + 8 = 9 | Swap Mutation             |

Berdasarkan aturan modul praktikum: 

---

# Struktur Program

| File              | Fungsi                |
| ----------------- | --------------------- |
| `main.py`         | Program utama         |
| `selection.py`    | Proses seleksi parent |
| `crossover.py`    | Proses crossover      |
| `mutation.py`     | Proses mutasi         |
| `fitness.py`      | Perhitungan fitness   |
| `inisialisasi.py` | Inisialisasi populasi |

---

# Tahapan Algoritma

## 1. Inisialisasi Populasi

Program membuat populasi awal secara acak.

Contoh:

```python id="7k2v4r"
[1,0,1,1,0]
```

Setiap individu mewakili solusi potensial.

---

## 2. Evaluasi Fitness

Fitness dihitung berdasarkan:

* total keuntungan barang,
* total ukuran barang.

Jika ukuran melebihi kapasitas gudang maka fitness dianggap tidak valid.

Konsep fitness:

[
Fitness = \sum keuntungan\ barang
]

dengan syarat:

[
Total\ Ukuran \leq Kapasitas\ Maksimal
]

---

## 3. Seleksi – Tournament Selection

Program menggunakan metode:

## Tournament Selection (TS)

Pada metode ini:

* beberapa individu dipilih secara acak,
* individu dengan fitness terbaik dipilih sebagai parent.

Keuntungan metode ini:

* sederhana,
* efektif,
* mempercepat konvergensi solusi.

---

## 4. Crossover – Uniform Crossover

Metode crossover yang digunakan adalah:

## Uniform Crossover

Setiap gen anak dipilih secara acak dari parent 1 atau parent 2 menggunakan masking biner.

Contoh:

Parent 1:

```python id="57c7js"
[1,0,1,1,0]
```

Parent 2:

```python id="jlwmhf"
[0,1,0,0,1]
```

Mask:

```python id="1ojl9l"
[1,0,1,0,1]
```

Hasil offspring:

```python id="o8wqq8"
[0,0,0,1,1]
```

---

## 5. Mutasi – Swap Mutation

Mutasi dilakukan dengan menukar dua posisi gen secara acak.

Contoh:

Sebelum:

```python id="ev0rdo"
[1,0,1,1,0]
```

Sesudah:

```python id="fxxmsv"
[1,1,1,0,0]
```

Mutasi membantu menjaga keberagaman populasi.

---

# Library yang Digunakan

Program menggunakan library berikut:

```python id="jlwm3e"
import random
import matplotlib.pyplot as plt
import numpy as np
```

---

# Cara Menjalankan Program

## 1. Install Dependency

```bash id="bhp9r7"
pip install matplotlib numpy
```

---

## 2. Jalankan Program

```bash id="jlwm0k"
python main.py
```

---

# Hasil Output Program

Berikut hasil yang diperoleh setelah program dijalankan:

```bash id="hj23vv"
Keuntungan Maksimal (Fitness): 125
Total Ukuran Digunakan: 14 / 15
Barang yang harus dibeli:
- Barang2
- Barang4
- Barang5
```

---

# Analisis Hasil

Berdasarkan hasil pengujian:

* Algoritma berhasil menemukan kombinasi barang terbaik
* Fitness maksimum yang diperoleh adalah **125**
* Total ukuran yang digunakan adalah **14**
* Kapasitas maksimum gudang adalah **15**
* Kombinasi barang yang dipilih sudah optimal dan tidak melebihi kapasitas

Barang yang dipilih:

| Barang  | Status  |
| ------- | ------- |
| Barang2 | Dipilih |
| Barang4 | Dipilih |
| Barang5 | Dipilih |

---

# Penjelasan Evolusi Algoritma

Proses Genetic Algorithm berjalan melalui beberapa generasi:

1. Membuat populasi awal
2. Menghitung fitness seluruh individu
3. Memilih parent terbaik
4. Melakukan crossover
5. Melakukan mutasi
6. Membentuk generasi baru
7. Mengulang proses hingga ditemukan solusi terbaik

Semakin banyak generasi, semakin besar peluang menemukan solusi optimal.

---

# Kesimpulan

Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa:

1. Algoritma Genetika mampu menyelesaikan masalah optimasi knapsack dengan efektif.
2. Pemilihan metode seleksi, crossover, dan mutasi mempengaruhi kualitas solusi.
3. Tournament Selection membantu memilih parent dengan fitness terbaik.
4. Uniform Crossover mampu menghasilkan variasi solusi yang baik.
5. Swap Mutation membantu menjaga keragaman populasi.
6. Genetic Algorithm sangat cocok digunakan pada masalah optimasi kompleks.

---

# Dokumentasi Output

```bash id="xjlwm"
PS D:\KULIAH UNSOED SMS 4\Praktikum Kecerdasan Buatan> python main.py

Keuntungan Maksimal (Fitness): 125
Total Ukuran Digunakan: 14 / 15
Barang yang harus dibeli:
- Barang2
- Barang4
- Barang5

PS D:\KULIAH UNSOED SMS 4\Praktikum Kecerdasan Buatan>
```

---

# Repository GitHub

Format repository:

```bash id="8n13b7"
NIM-PraktikumKB-Pertemuan10
```

Contoh:

```bash id="e6e9px"
H1D024118-PraktikumKB-Pertemuan10
```

