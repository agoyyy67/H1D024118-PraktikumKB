# ==========================================
# 1. IMPORT LIBRARY
# ==========================================
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 2. LOAD DATASET & PREPROCESSING
# ==========================================
# Muat dataset iris dari URL
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
dataset = pd.read_csv(url, header=None, sep=',')

# Menyusun data X (fitur) dan y (label)
X = dataset.iloc[:, :-1].values  # 4 kolom pertama sebagai fitur
y = dataset.iloc[:, -1].values   # Kolom terakhir sebagai label

# Mengonversi label dari string (nama spesies) menjadi numerik (0, 1, 2)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Memisahkan dataset menjadi data latih dan data validasi/uji dengan rasio 80:20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 3. PEMBUATAN & ARSITEKTUR MODEL
# ==========================================
# Buat model neural network dengan 1 layer input dan 4 layer Dense
model = Sequential([
    Input(shape=X_train.shape[1:]),          # Layer input menerima 4 fitur
    Dense(1000, activation='relu'),          # Hidden layer 1
    Dense(500, activation='relu'),           # Hidden layer 2
    Dense(300, activation='relu'),           # Hidden layer 3
    Dense(3, activation='softmax')           # Output layer (3 kelas spesies)
])

# Menampilkan ringkasan arsitektur model
model.summary()

# Kompilasi model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',  # Tepat untuk label integer hasil LabelEncoder
    metrics=['accuracy']
)

# ==========================================
# 4. PELATIHAN & EVALUASI MODEL
# ==========================================
# Melatih model dengan data latih selama 50 epoch
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_data=(X_test, y_test)
)

# Evaluasi model pada data validasi
loss, accuracy = model.evaluate(X_test, y_test)
print(f"\nHasil Evaluasi -> Loss: {loss:.4f}, Accuracy: {accuracy:.4f}")

# Visualisasi perubahan loss dan accuracy selama pelatihan
pd.DataFrame(history.history).plot(figsize=(10, 6))
plt.title('Metrik Pelatihan (Loss & Accuracy)')
plt.grid(True)
plt.show()

# ==========================================
# 5. PREDIKSI & CONFUSION MATRIX
# ==========================================
# Lakukan prediksi pada data uji
predictions = model.predict(X_test)
# Mengambil indeks dari nilai probabilitas tertinggi untuk setiap prediksi
predicted_classes = predictions.argmax(axis=1)

print("\nHasil Prediksi Kelas :", predicted_classes)
print("Label Sebenarnya (Asli):", y_test)

# Buat dan visualisasikan confusion matrix
cm = confusion_matrix(y_test, predicted_classes)

plt.figure(figsize=(8, 6))
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=label_encoder.classes_,
    yticklabels=label_encoder.classes_
)
plt.title('Confusion Matrix - Klasifikasi Iris')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

# ==========================================
# 6. FUNGSI PREDIKSI DATA BARU
# ==========================================
def predict_new_data():
    print("\n--- Input Data Baru untuk Prediksi ---")
    try:
        sepal_length = float(input("Masukkan sepal length : "))
        sepal_width  = float(input("Masukkan sepal width  : "))
        petal_length = float(input("Masukkan petal length : "))
        petal_width  = float(input("Masukkan petal width  : "))
        
        # Membuat data array baru dengan dimensi (1, 4)
        new_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        
        # Melakukan prediksi
        prediction = model.predict(new_data)
        predicted_class = prediction.argmax(axis=1)
        
        # Mengonversi hasil prediksi numerik menjadi label asli string
        predicted_label = label_encoder.inverse_transform(predicted_class)
        print(f"-> Hasil Prediksi Spesies Bunga: {predicted_label[0]}")
    except ValueError:
        print("Input harus berupa angka desimal/integer yang valid.")

# Menjalankan fungsi prediksi data baru
predict_new_data()