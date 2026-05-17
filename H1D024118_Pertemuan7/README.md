# README - Praktikum Kecerdasan Buatan Pertemuan 7

# NAMA : YOGA ADI NUGRAHA
# NIM  : H1D024118
# SHIFT : D

## Jaringan Syaraf Tiruan (JST) 2 Menggunakan TensorFlow dan Keras

Repository ini berisi implementasi **Jaringan Syaraf Tiruan (Artificial Neural Network / ANN)** menggunakan library **TensorFlow** dan **Keras** untuk melakukan klasifikasi spesies bunga **Iris** berdasarkan karakteristik morfologi bunga. Praktikum ini merupakan implementasi lanjutan konsep JST pada mata kuliah Praktikum Kecerdasan Buatan.

Dataset yang digunakan adalah **Iris Dataset** dari UCI Machine Learning Repository yang terdiri dari 150 data dengan 3 kelas spesies bunga, yaitu:

* Iris Setosa
* Iris Versicolor
* Iris Virginica

---

# Tujuan Praktikum

Tujuan dari praktikum ini adalah:

* Memahami implementasi jaringan syaraf tiruan menggunakan TensorFlow dan Keras.
* Mempelajari proses preprocessing dataset.
* Membuat model neural network multilayer.
* Melakukan training dan evaluasi model klasifikasi.
* Menampilkan visualisasi accuracy dan loss selama pelatihan.
* Menggunakan confusion matrix untuk analisis hasil klasifikasi.
* Membuat sistem prediksi data baru secara interaktif.

---

# Dataset

Dataset diambil langsung dari URL resmi UCI Repository:

```python
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
```

Dataset memiliki:

| Fitur        | Keterangan      |
| ------------ | --------------- |
| Sepal Length | Panjang kelopak |
| Sepal Width  | Lebar kelopak   |
| Petal Length | Panjang mahkota |
| Petal Width  | Lebar mahkota   |

Target klasifikasi:

* Iris-setosa
* Iris-versicolor
* Iris-virginica

---

# Library yang Digunakan

Program menggunakan beberapa library utama berikut:

```python
tensorflow
keras
pandas
numpy
scikit-learn
matplotlib
seaborn
```

Install dependency:

```bash
pip install tensorflow pandas numpy scikit-learn matplotlib seaborn
```

---

# Struktur Program

Program dibagi menjadi beberapa bagian utama:

| Bagian           | Fungsi                                |
| ---------------- | ------------------------------------- |
| Import Library   | Mengimpor library yang diperlukan     |
| Load Dataset     | Membaca dataset Iris                  |
| Preprocessing    | Memisahkan fitur dan label            |
| Label Encoding   | Mengubah label string menjadi numerik |
| Train Test Split | Membagi data training dan testing     |
| Pembuatan Model  | Membuat arsitektur neural network     |
| Compile Model    | Konfigurasi optimizer dan loss        |
| Training         | Melatih model                         |
| Evaluasi         | Mengukur akurasi model                |
| Visualisasi      | Menampilkan grafik accuracy dan loss  |
| Confusion Matrix | Analisis hasil klasifikasi            |
| Prediksi Baru    | Input data baru secara manual         |

---

# Arsitektur Neural Network

Model JST yang digunakan terdiri dari:

| Layer          | Neuron  | Aktivasi |
| -------------- | ------- | -------- |
| Input Layer    | 4 fitur | -        |
| Hidden Layer 1 | 1000    | ReLU     |
| Hidden Layer 2 | 500     | ReLU     |
| Hidden Layer 3 | 300     | ReLU     |
| Output Layer   | 3       | Softmax  |

Implementasi model:

```python
model = Sequential([
    Input(shape=X_train.shape[1:]),
    Dense(1000, activation='relu'),
    Dense(500, activation='relu'),
    Dense(300, activation='relu'),
    Dense(3, activation='softmax')
])
```

---

# Compile Model

Model dikompilasi menggunakan:

```python
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

Penjelasan:

* **Adam Optimizer** digunakan untuk mempercepat proses optimasi bobot.
* **Sparse Categorical Crossentropy** digunakan karena label berbentuk integer.
* **Accuracy** digunakan sebagai metrik evaluasi model.

---

# Proses Training

Model dilatih menggunakan:

```python
epochs = 50
batch_size = 32
```

Training dilakukan menggunakan data training sebesar 80% dan data testing sebesar 20%.

---

# Hasil Training

Berdasarkan hasil praktikum:

```text
Hasil Evaluasi -> Loss: 0.2610
Accuracy: 0.8667
```

Artinya model berhasil memperoleh tingkat akurasi sekitar:

## 86.67%

Nilai tersebut menunjukkan bahwa jaringan syaraf tiruan mampu mempelajari pola dataset Iris dengan cukup baik.

---

# Visualisasi Training

Program menampilkan grafik:

* Accuracy Training
* Accuracy Validation
* Loss Training
* Loss Validation

Visualisasi dilakukan menggunakan:

```python
pd.DataFrame(history.history).plot(figsize=(10, 6))
```

Grafik ini membantu dalam menganalisis:

* Performa model
* Stabilitas training
* Potensi overfitting atau underfitting

---

# Confusion Matrix

Confusion matrix digunakan untuk melihat:

* Jumlah prediksi benar
* Jumlah prediksi salah
* Distribusi klasifikasi tiap kelas

Implementasi:

```python
cm = confusion_matrix(y_test, predicted_classes)
```

Visualisasi menggunakan heatmap dari Seaborn:

```python
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
```

---

# Prediksi Data Baru

Program menyediakan fitur input manual data bunga:

```python
Masukkan sepal length :
Masukkan sepal width  :
Masukkan petal length :
Masukkan petal width  :
```

Contoh input:

```text
5
7
9
12
```

Hasil prediksi:

```text
Iris-virginica
```

Fitur ini menunjukkan bahwa model dapat digunakan untuk melakukan klasifikasi data baru secara real-time.

---

# Analisis Hasil Praktikum

Dari hasil praktikum dapat dianalisis bahwa:

* TensorFlow dan Keras sangat mempermudah implementasi JST.
* Fungsi aktivasi ReLU efektif digunakan pada hidden layer.
* Softmax cocok digunakan untuk klasifikasi multikelas.
* Dataset Iris relatif mudah dipelajari oleh neural network.
* Akurasi model cukup tinggi meskipun dataset berukuran kecil.
* Confusion matrix membantu memahami performa model secara detail.
* Training dengan epoch yang terlalu besar dapat menyebabkan fluktuasi accuracy validation.

Selain itu, praktikum ini memberikan pemahaman mengenai:

* Deep Learning dasar
* Arsitektur multilayer perceptron
* Training neural network
* Optimizer dan loss function
* Evaluasi performa model machine learning

---

# Kesimpulan

Pada praktikum pertemuan 7 ini berhasil dibuat model **Jaringan Syaraf Tiruan (JST)** menggunakan TensorFlow dan Keras untuk klasifikasi bunga Iris. Model mampu mengenali tiga spesies bunga berdasarkan empat fitur morfologi dengan akurasi mencapai sekitar 86.67%.

Praktikum ini membuktikan bahwa neural network dapat digunakan untuk menyelesaikan permasalahan klasifikasi multikelas dengan cukup efektif. Selain itu, penggunaan TensorFlow dan Keras membuat proses pembangunan model deep learning menjadi lebih sederhana, terstruktur, dan mudah dipahami.

---

# Cara Menjalankan Program

Masuk ke folder project:

```bash
cd H1D024118_Pertemuan7
```

Jalankan program:

```bash
python index.py
```
