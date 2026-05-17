# ==========================================
# 1. IMPORT LIBRARY YANG DIPERLUKAN
# ==========================================
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# ==========================================
# 2. PREPROCESSING DAN AUGMENTASI DATA
# ==========================================
# Path menuju folder dataset utama
dataset_path = "H1D024118_Pertemuan8/rockpaperscissors"

# Inisialisasi generator dengan rescale dan split validasi 20%
train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

# Generator untuk data training
train_generator = train_datagen.flow_from_directory(
    dataset_path,
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical',
    subset='training'
)

# Generator untuk data validasi
validation_generator = train_datagen.flow_from_directory(
    dataset_path,
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical',
    subset='validation'
)

# ==========================================
# 3. MEMBANGUN ARSITEKTUR MODEL CNN
# ==========================================
model = Sequential([
    # Blok Konvolusi 1
    Conv2D(32, (3,3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D(2,2),
    
    # Blok Konvolusi 2
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    
    # Blok Konvolusi 3
    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    
    # Flatten & Fully Connected Layer (MLP)
    Flatten(),
    Dense(512, activation='relu'),
    Dense(3, activation='softmax') # 3 Kelas: rock, paper, scissors
])

# Menampilkan ringkasan arsitektur model
model.summary()

# ==========================================
# 4. KOMPILASI MODEL
# ==========================================
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# ==========================================
# 5. PELATIHAN MODEL (MODEL FITTING)
# ==========================================
history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=10
)

# ==========================================
# 6. EVALUASI MODEL
# ==========================================
val_loss, val_acc = model.evaluate(validation_generator)
print(f'Validation loss: {val_loss}, Validation accuracy: {val_acc}')

# ==========================================
# 7. PREDIKSI DATA BARU
# ==========================================
predictions = model.predict(validation_generator)
print(predictions)  # Output berupa probabilitas distribusi tiap kelas