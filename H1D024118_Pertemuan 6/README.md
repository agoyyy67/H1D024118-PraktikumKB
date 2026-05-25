# README - Praktikum KB Pertemuan 6

## Jaringan Syaraf Tiruan (JST)

Praktikum ini membahas implementasi dasar **Jaringan Syaraf Tiruan (JST)** menggunakan bahasa pemrograman Python. Materi utama yang dipelajari meliputi konsep neuron, fungsi aktivasi, algoritma **Perceptron** untuk kasus OR, dan algoritma **Backpropagation** untuk kasus XOR. 

---

# Tujuan Praktikum

1. Memahami konsep dasar Jaringan Syaraf Tiruan (JST)
2. Memahami metode pembelajaran pada JST
3. Mengimplementasikan algoritma Perceptron menggunakan Python
4. Mengimplementasikan algoritma Backpropagation menggunakan Python
5. Memvisualisasikan proses pelatihan model JST 

---

# Materi Praktikum

## 1. Jaringan Syaraf Tiruan (JST)

Jaringan Syaraf Tiruan merupakan model komputasi yang terinspirasi dari sistem saraf biologis manusia. JST bekerja menggunakan neuron yang saling terhubung melalui bobot (weight) dan bias untuk memproses informasi. 

---

## 2. Fungsi Aktivasi

Praktikum ini menggunakan beberapa fungsi aktivasi, antara lain:

* Fungsi Undak Biner
* Fungsi Bipolar
* Fungsi Linier
* Fungsi Saturating Linier
* Fungsi Symmetric Saturating Linier
* Fungsi Sigmoid Biner
* Fungsi Sigmoid Bipolar (tanh) 

Contoh fungsi sigmoid bipolar:

y=\frac{1-e^{-y_{in}}}{1+e^{-y_{in}}}

---

# Struktur Project

```bash
.
├── Perceptron.py
├── Perceptron_or.py
├── HasilPerceptron.txt
├── Backpropagation.py
├── Backpropagation_xor.py
├── HasilBackpropagation.txt
└── README.md
```

---

# Studi Kasus 1 - Perceptron OR

## Konsep

Perceptron adalah model JST single layer yang digunakan untuk klasifikasi linear sederhana. Pada praktikum ini digunakan kasus logika OR bipolar.

### Dataset OR

| X1 | X2 | Target |
| -- | -- | ------ |
| 1  | 1  | 1      |
| 1  | -1 | 1      |
| -1 | 1  | 1      |
| -1 | -1 | -1     |



---

## Parameter

* Learning Rate : `0.1`
* Epoch : `10`
* Bobot awal : `0`
* Bias awal : `0`

---

## Menjalankan Program

```bash
python Perceptron_or.py
```

---

## Output

Program akan menghasilkan:

* Visualisasi decision boundary setiap epoch
* File `HasilPerceptron.txt`
* Bobot dan bias akhir model

---

# Studi Kasus 2 - Backpropagation XOR

## Konsep

Backpropagation merupakan pengembangan dari Perceptron dengan hidden layer sehingga mampu menyelesaikan permasalahan non-linear seperti XOR. 

---

## Dataset XOR

| X1 | X2 | Target |
| -- | -- | ------ |
| 1  | 1  | -1     |
| 1  | -1 | 1      |
| -1 | 1  | 1      |
| -1 | -1 | -1     |

---

## Parameter

* Learning Rate : `0.3`
* Max Epoch : `1000`
* Target Error : `0.001`

---

## Arsitektur Model

Model terdiri dari:

* Input Layer
* Hidden Layer
* Output Layer

Dengan mekanisme:

1. Forward Propagation
2. Backward Propagation
3. Update Bobot dan Bias

---

## Fungsi Aktivasi

Backpropagation menggunakan fungsi aktivasi tanh:

h=\tanh(h_{in})

Dan delta error:

\delta=error\times(1-y^2)

---

## Menjalankan Program

```bash
python Backpropagation_xor.py
```

---

## Output

Program akan menghasilkan:

* Grafik penurunan error tiap epoch
* File `HasilBackpropagation.txt`
* Bobot dan bias akhir model

---

# Library yang Digunakan

```python
numpy
matplotlib
```

Install dependency:

```bash
pip install numpy matplotlib
```

---

# Konsep Penting

## Weighted Sum

y_{in}=b+\sum_{i=1}^{n}x_iw_i

## Delta Rule

\Delta w_i=\alpha(t_i-y_i)x_i

## Update Bobot

w_i=w_i+\Delta w_i

---

# Kesimpulan

Pada praktikum ini dipelajari implementasi dasar JST menggunakan algoritma:

* **Perceptron** untuk kasus linear separable (OR)
* **Backpropagation** untuk kasus non-linear separable (XOR)

Selain itu dipelajari pula konsep:

* Fungsi aktivasi
* Forward propagation
* Backward propagation
* Update bobot dan bias
* Visualisasi proses pembelajaran jaringan



