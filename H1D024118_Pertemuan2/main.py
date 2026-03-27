import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt # Tambahan penting untuk menahan grafik

# 1. Definisi Variabel (Universe)
# Rentang sesuai ketentuan modul
suhu = ctrl.Antecedent(np.arange(0, 41, 1), 'suhu')             # 0 - 40 C
kelembapan = ctrl.Antecedent(np.arange(0, 101, 1), 'kelembapan') # 0 - 100 %
kecepatan = ctrl.Consequent(np.arange(0, 101, 1), 'kecepatan')   # 0 - 100

# 2. Pembuatan Himpunan Fuzzy (Membership Function)
# Menggunakan fungsi segitiga (trimf)
suhu['dingin'] = fuzz.trimf(suhu.universe, [0, 0, 20])
suhu['normal'] = fuzz.trimf(suhu.universe, [15, 25, 35])
suhu['panas'] = fuzz.trimf(suhu.universe, [30, 40, 40])

kelembapan['kering'] = fuzz.trimf(kelembapan.universe, [0, 0, 45])
kelembapan['normal'] = fuzz.trimf(kelembapan.universe, [35, 50, 75])
kelembapan['lembap'] = fuzz.trimf(kelembapan.universe, [65, 100, 100])

kecepatan['lambat'] = fuzz.trimf(kecepatan.universe, [0, 0, 40])
kecepatan['sedang'] = fuzz.trimf(kecepatan.universe, [30, 50, 70])
kecepatan['cepat'] = fuzz.trimf(kecepatan.universe, [60, 100, 100])

# 3. Aturan Fuzzy (Fuzzy Rules)
# Membuat 5 aturan logis yang merepresentasikan kondisi dunia nyata
rule1 = ctrl.Rule(suhu['dingin'] & kelembapan['kering'], kecepatan['lambat'])
rule2 = ctrl.Rule(suhu['dingin'] & kelembapan['lembap'], kecepatan['lambat'])
rule3 = ctrl.Rule(suhu['normal'] & kelembapan['normal'], kecepatan['sedang'])
rule4 = ctrl.Rule(suhu['panas'] & kelembapan['kering'], kecepatan['sedang'])
rule5 = ctrl.Rule(suhu['panas'] & kelembapan['lembap'], kecepatan['cepat'])

# 4. Sistem Kontrol & Simulasi
kipas_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
kipas_sim = ctrl.ControlSystemSimulation(kipas_ctrl)

# 5. Testing Input Data
suhu_input = 32.0
kelembapan_input = 80.0

kipas_sim.input['suhu'] = suhu_input
kipas_sim.input['kelembapan'] = kelembapan_input

# 6. Proses Inferensi (Menghitung hasil)
kipas_sim.compute()

# 7. Output Text di Terminal
print("=== HASIL INFERENSI LOGIKA FUZZY ===")
print(f"Suhu Lingkungan : {suhu_input} Â°C")
print(f"Kelembapan      : {kelembapan_input} %")
print(f"Kecepatan Kipas : {kipas_sim.output['kecepatan']:.2f} %")

# 8. Visualisasi
# Memanggil fungsi view() untuk melihat area hasil defuzzifikasi
kecepatan.view(sim=kipas_sim)

# INI KUNCI AGAR GRAFIK TIDAK LANGSUNG TERTUTUP:
plt.show()