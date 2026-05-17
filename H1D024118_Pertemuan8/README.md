# README - Praktikum Kecerdasan Buatan Pertemuan 8

# NAMA : YOGA ADI NUGRAHA
# NIM  : H1D024118
# SHIFT : D

## Implementasi Convolutional Neural Network (CNN) untuk Klasifikasi Rock Paper Scissors

Repository ini berisi implementasi **Convolutional Neural Network (CNN)** menggunakan **TensorFlow** dan **Keras** untuk melakukan klasifikasi gambar **Rock, Paper, dan Scissors**.

Praktikum ini merupakan lanjutan materi **Jaringan Syaraf Tiruan (JST) 3** yang berfokus pada pengolahan citra digital menggunakan arsitektur CNN.

---

# Tujuan Praktikum

Tujuan dari praktikum ini adalah:

* Memahami konsep dasar Convolutional Neural Network (CNN).
* Mempelajari cara kerja layer konvolusi dan pooling.
* Mengimplementasikan CNN menggunakan TensorFlow dan Keras.
* Melakukan preprocessing dataset gambar menggunakan `ImageDataGenerator`.
* Melatih model CNN untuk klasifikasi citra.
* Mengevaluasi performa model menggunakan accuracy dan loss.
* Melakukan prediksi terhadap data gambar baru.

---

# Dataset

Dataset yang digunakan adalah:

## Rock Paper Scissors Dataset

Dataset terdiri dari 3 kelas gambar:

* Rock
* Paper
* Scissors

Dataset diambil dari Kaggle sesuai modul praktikum:

[Kaggle Rock Paper Scissors Dataset](https://www.kaggle.com/datasets/drgfreeman/rockpaperscissors?utm_source=chatgpt.com)

Struktur dataset:

```text id="m4rw2u"
rockpaperscissors/
│
├── rock/
├── paper/
└── scissors/
```

---

# Library yang Digunakan

Program menggunakan beberapa library utama berikut:

```python id="84nmk7"
numpy
pandas
tensorflow
keras
ImageDataGenerator
```

Install dependency:

```bash id="1xub9k"
pip install tensorflow pandas numpy
```

---

# Konsep CNN yang Digunakan

Pada praktikum ini digunakan beberapa komponen utama CNN:

| Komponen     | Fungsi                                  |
| ------------ | --------------------------------------- |
| Conv2D       | Mengekstraksi fitur gambar              |
| MaxPooling2D | Mengurangi dimensi feature map          |
| Flatten      | Mengubah feature map menjadi vektor     |
| Dense Layer  | Fully Connected Layer untuk klasifikasi |
| Softmax      | Menghasilkan probabilitas tiap kelas    |

---

# Preprocessing dan Augmentasi Data

Dataset diproses menggunakan:

```python id="s9kq9d"
ImageDataGenerator
```

Fitur preprocessing yang digunakan:

* Rescale pixel → `1./255`
* Validation split → `20%`

Implementasi:

```python id="yo9c6w"
train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)
```

Dataset kemudian dibagi menjadi:

| Dataset    | Persentase |
| ---------- | ---------- |
| Training   | 80%        |
| Validation | 20%        |

Hasil pembagian dataset:

```text id="m5l7tl"
Found 1751 images belonging to 3 classes.
Found 437 images belonging to 3 classes.
```

---

# Arsitektur Model CNN

Model CNN yang digunakan terdiri dari:

| Layer        | Konfigurasi                         |
| ------------ | ----------------------------------- |
| Conv2D       | 32 filter, kernel 3x3, ReLU         |
| MaxPooling2D | Pool size 2x2                       |
| Conv2D       | 64 filter, kernel 3x3, ReLU         |
| MaxPooling2D | Pool size 2x2                       |
| Conv2D       | 128 filter, kernel 3x3, ReLU        |
| MaxPooling2D | Pool size 2x2                       |
| Flatten      | Mengubah feature map menjadi vektor |
| Dense        | 512 neuron, ReLU                    |
| Output Layer | 3 neuron, Softmax                   |

Implementasi model:

```python id="3kn3dp"
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(150,150,3)),
    MaxPooling2D(2,2),

    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Flatten(),

    Dense(512, activation='relu'),

    Dense(3, activation='softmax')
])
```

---

# Ringkasan Model

Hasil `model.summary()`:

| Layer        | Output Shape |
| ------------ | ------------ |
| Conv2D       | (148,148,32) |
| MaxPooling2D | (74,74,32)   |
| Conv2D       | (72,72,64)   |
| MaxPooling2D | (36,36,64)   |
| Conv2D       | (34,34,128)  |
| MaxPooling2D | (17,17,128)  |
| Flatten      | (36992)      |
| Dense        | (512)        |
| Dense Output | (3)          |

Total parameter:

```text id="jcf3cz"
19,035,203 parameters
```

Model memiliki sekitar:

## 19 juta parameter trainable

yang digunakan untuk mempelajari pola citra pada dataset.

---

# Kompilasi Model

Model dikompilasi menggunakan:

```python id="dlv8rw"
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)
```

Penjelasan:

| Komponen                 | Fungsi                               |
| ------------------------ | ------------------------------------ |
| Adam Optimizer           | Optimasi bobot model                 |
| categorical_crossentropy | Loss function klasifikasi multikelas |
| accuracy                 | Mengukur akurasi model               |

---

# Pelatihan Model

Model dilatih menggunakan:

```python id="56i5o5"
epochs = 10
```

Training dilakukan menggunakan:

```python id="7m8g5z"
history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=10
)
```

---

# Hasil Training

Berikut hasil accuracy dan loss selama training:

| Epoch | Accuracy | Validation Accuracy |
| ----- | -------- | ------------------- |
| 1     | 68.65%   | 89.93%              |
| 5     | 98.80%   | 97.71%              |
| 10    | 98.97%   | 97.03%              |

Hasil evaluasi akhir:

```text id="xj5mk7"
Validation loss: 0.1921
Validation accuracy: 0.9703
```

Model berhasil memperoleh akurasi validasi sebesar:

# 97.03%

Hal ini menunjukkan bahwa CNN mampu mengenali pola gambar dengan sangat baik.

---

# Evaluasi Model

Evaluasi dilakukan menggunakan:

```python id="e4n1wr"
val_loss, val_acc = model.evaluate(validation_generator)
```

Tujuan evaluasi:

* Mengukur performa model pada data validasi
* Mengetahui tingkat generalisasi model
* Memastikan model tidak mengalami overfitting berlebihan

---

# Prediksi Data Baru

Program juga dapat melakukan prediksi terhadap gambar baru menggunakan:

```python id="w6f7ry"
predictions = model.predict(validation_generator)
```

Output berupa probabilitas masing-masing kelas:

Contoh:

```text id="h5h4x6"
[[1.47982393e-09 2.23571340e-25 1.00000000e+00]
 [1.43162315e-05 9.99985695e-01 1.05972280e-11]]
```

Interpretasi:

* Nilai probabilitas terbesar menunjukkan kelas hasil prediksi.
* Softmax menghasilkan distribusi probabilitas total = 1.

---

# Analisis Hasil Praktikum

Berdasarkan hasil praktikum dapat dianalisis bahwa:

* CNN sangat efektif untuk pengolahan citra dibandingkan MLP biasa.
* Layer konvolusi berhasil mengekstraksi fitur penting dari gambar.
* Max pooling membantu mengurangi kompleksitas data.
* Accuracy model meningkat signifikan setiap epoch.
* Model memiliki performa klasifikasi yang sangat baik dengan accuracy di atas 97%.
* Penggunaan dataset gambar yang cukup banyak membantu model belajar lebih optimal.
* Softmax sangat cocok untuk klasifikasi multikelas.

Selain itu, praktikum ini memberikan pemahaman mengenai:

* Computer Vision dasar
* Deep Learning untuk image classification
* Feature extraction
* CNN architecture
* Training model citra
* Image preprocessing

---

# Kesimpulan

Pada praktikum pertemuan 8 ini berhasil dibuat model **Convolutional Neural Network (CNN)** menggunakan TensorFlow dan Keras untuk melakukan klasifikasi gambar Rock, Paper, dan Scissors.

Model CNN yang dibangun mampu mencapai validation accuracy sebesar 97.03%, yang menunjukkan bahwa CNN sangat efektif dalam mengenali pola visual pada citra digital.

Praktikum ini memberikan pemahaman penting mengenai implementasi deep learning pada bidang computer vision, khususnya klasifikasi gambar menggunakan arsitektur CNN.

---

# Cara Menjalankan Program


Masuk ke folder project:

```bash id="y5q0t8"
cd H1D024118_Pertemuan8
```

Jalankan program:

```bash id="d4m3qn"
python index.py
```
