import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# 1. Definisi Antecedent (Input) dan Consequent (Output)
# Range ditentukan berdasarkan semesta pembicaraan pada soal
jumlah_terjual = ctrl.Antecedent(np.arange(0, 101, 1), 'jumlah_terjual')
jumlah_permintaan = ctrl.Antecedent(np.arange(0, 301, 1), 'jumlah_permintaan')
harga_satuan = ctrl.Antecedent(np.arange(0, 100001, 1), 'harga_satuan')
keuntungan = ctrl.Antecedent(np.arange(0, 4000001, 1), 'keuntungan')
rekomendasi_stok = ctrl.Consequent(np.arange(0, 1001, 1), 'rekomendasi_stok')

# 2. Membership Functions (Menggunakan fungsi segitiga/trimf sebagai standar)
# Barang Terjual [0 - 100]
jumlah_terjual['rendah'] = fuzz.trimf(jumlah_terjual.universe, [0, 0, 40])
jumlah_terjual['sedang'] = fuzz.trimf(jumlah_terjual.universe, [30, 50, 70])
jumlah_terjual['tinggi'] = fuzz.trimf(jumlah_terjual.universe, [60, 100, 100])

# Permintaan [0 - 300]
jumlah_permintaan['rendah'] = fuzz.trimf(jumlah_permintaan.universe, [0, 0, 100])
jumlah_permintaan['sedang'] = fuzz.trimf(jumlah_permintaan.universe, [50, 150, 250])
jumlah_permintaan['tinggi'] = fuzz.trimf(jumlah_permintaan.universe, [200, 300, 300])

# Harga per Item [0 - 100.000]
harga_satuan['murah'] = fuzz.trimf(harga_satuan.universe, [0, 0, 40000])
harga_satuan['sedang'] = fuzz.trimf(harga_satuan.universe, [30000, 50000, 80000])
harga_satuan['mahal'] = fuzz.trimf(harga_satuan.universe, [60000, 100000, 100000])

# Profit [0 - 4.000.000]
keuntungan['rendah'] = fuzz.trimf(keuntungan.universe, [0, 0, 1000000])
keuntungan['sedang'] = fuzz.trimf(keuntungan.universe, [1000000, 2000000, 2500000])
keuntungan['banyak'] = fuzz.trapmf(keuntungan.universe, [1500000, 2500000, 4000000,4000000])

# Stok Makanan (Output) [0 - 1000]
rekomendasi_stok['sedang'] = fuzz.trimf(rekomendasi_stok.universe, [100, 500, 900])
rekomendasi_stok['banyak'] = fuzz.trimf(rekomendasi_stok.universe, [600, 1000, 1000])

# 3. Definisi Aturan Fuzzy (Rules)
rule1 = ctrl.Rule(jumlah_terjual['tinggi'] & jumlah_permintaan['tinggi'] & harga_satuan['murah'] & keuntungan['banyak'], rekomendasi_stok['banyak'])
rule2 = ctrl.Rule(jumlah_terjual['tinggi'] & jumlah_permintaan['tinggi'] & harga_satuan['murah'] & keuntungan['sedang'], rekomendasi_stok['sedang'])
rule3 = ctrl.Rule(jumlah_terjual['tinggi'] & jumlah_permintaan['sedang'] & harga_satuan['murah'] & keuntungan['sedang'], rekomendasi_stok['sedang'])
rule4 = ctrl.Rule(jumlah_terjual['sedang'] & jumlah_permintaan['tinggi'] & harga_satuan['murah'] & keuntungan['sedang'], rekomendasi_stok['sedang'])
rule5 = ctrl.Rule(jumlah_terjual['sedang'] & jumlah_permintaan['tinggi'] & harga_satuan['murah'] & keuntungan['banyak'], rekomendasi_stok['banyak'])
rule6 = ctrl.Rule(jumlah_terjual['rendah'] & jumlah_permintaan['rendah'] & harga_satuan['sedang'] & keuntungan['sedang'], rekomendasi_stok['sedang'])

# 4. Sistem Kontrol dan Simulasi
sistem_stok = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
simulasi_stok = ctrl.ControlSystemSimulation(sistem_stok)

# 5. Memasukkan Nilai Input Sesuai Soal
# barang terjual = 80, permintaan = 255, harga per item = Rp 25.000, dan profit = Rp 3.500.000
simulasi_stok.input['jumlah_terjual'] = 80
simulasi_stok.input['jumlah_permintaan'] = 255
simulasi_stok.input['harga_satuan'] = 25000
simulasi_stok.input['keuntungan'] = 3500000

# 6. Melakukan Perhitungan (Crushing/Compute)
simulasi_stok.compute()

# 7. Output Hasil
hasil_rekomendasi_stok = simulasi_stok.output['rekomendasi_stok']
print("--- HASIL PERHITUNGAN LOGIKA FUZZY ---")
print(f"Barang Terjual : 80")
print(f"Permintaan     : 255")
print(f"Harga per Item : 25.000")
print(f"Profit         : 3.500.000")
print("--------------------------------------")
print(f"Jumlah Stok Makanan yang Direkomendasikan: {hasil_rekomendasi_stok:.2f} unit")

# Visualisasi 
jumlah_terjual.view(sim=simulasi_stok)
jumlah_permintaan.view(sim=simulasi_stok)
harga_satuan.view(sim=simulasi_stok)
keuntungan.view(sim=simulasi_stok)
rekomendasi_stok.view(sim=simulasi_stok)