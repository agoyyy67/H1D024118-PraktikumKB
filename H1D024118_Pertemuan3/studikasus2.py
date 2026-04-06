# STUDI KASUS 2
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 1. Definisi Antecedent (Input) dan Consequent (Output)
# Range ditentukan berdasarkan semesta pembicaraan pada soal
informasi_jelas = ctrl.Antecedent(np.arange(0, 101, 1), 'informasi_jelas')
persyaratan_jelas= ctrl.Antecedent(np.arange(0, 101, 1), 'persyaratan_jelas')
kompetensi_petugas= ctrl.Antecedent(np.arange(0, 101, 1), 'kompetensi_petugas')
ketersediaan_fasilitas = ctrl.Antecedent(np.arange(0, 101, 1), 'ketersediaan_fasilitas')
tingkat_kepuasan = ctrl.Consequent(np.arange(0, 401, 1), 'tingkat_kepuasan')

# 2. Membership Functions (Menggunakan fungsi segitiga/trapmf sebagai standar)
# kejelasaninformasi
informasi_jelas['tidak memuaskan'] = fuzz.trapmf(informasi_jelas.universe, [0, 0, 60,75])
informasi_jelas['cukup memuaskan'] = fuzz.trimf(informasi_jelas.universe, [60, 75, 90])
informasi_jelas['memuaskan'] = fuzz.trapmf(informasi_jelas.universe, [75, 90, 100,100]) # Corrected typo here

# kejelasanpersyarat
persyaratan_jelas['tidak memuaskan'] = fuzz.trapmf(persyaratan_jelas.universe, [0, 0, 60,75])
persyaratan_jelas['cukup memuaskan'] = fuzz.trimf(persyaratan_jelas.universe, [60, 75, 90])
persyaratan_jelas['memuaskan'] = fuzz.trapmf(persyaratan_jelas.universe, [75, 90, 100,100])

# kemampuanpetugas
kompetensi_petugas['tidak memuaskan'] = fuzz.trapmf(kompetensi_petugas.universe, [0, 0, 60,75])
kompetensi_petugas['cukup memuaskan'] = fuzz.trimf(kompetensi_petugas.universe, [60, 75, 90])
kompetensi_petugas['memuaskan'] = fuzz.trapmf(kompetensi_petugas.universe, [75, 90, 100,100])
# ketersediaansarpras
ketersediaan_fasilitas['tidak memuaskan'] = fuzz.trapmf(ketersediaan_fasilitas.universe, [0, 0, 60,75])
ketersediaan_fasilitas['cukup memuaskan'] = fuzz.trimf(ketersediaan_fasilitas.universe, [60, 75, 90])
ketersediaan_fasilitas['memuaskan'] = fuzz.trapmf(ketersediaan_fasilitas.universe, [75, 90, 100,100])

# kepuasanpelayanan
tingkat_kepuasan['tidak memuaskan'] = fuzz.trapmf(tingkat_kepuasan.universe, [0, 0, 50,75])
tingkat_kepuasan['kurang memuaskan'] = fuzz.trapmf(tingkat_kepuasan.universe, [50, 75, 100,150])
tingkat_kepuasan['cukup memuaskan'] = fuzz.trapmf(tingkat_kepuasan.universe, [100, 150, 250,275])
tingkat_kepuasan['memuaskan'] = fuzz.trapmf(tingkat_kepuasan.universe, [250, 275, 325,350])
tingkat_kepuasan['sangat memuaskan'] = fuzz.trapmf(tingkat_kepuasan.universe, [325, 350,400,400])

# 3. Definisi Rules
aturan1 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['kurang memuaskan'])
aturan2 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan3 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan4 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan5 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan6 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan7 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan8 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan9 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['memuaskan'])

aturan10 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan11 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan12 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan13 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan14 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan15 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['memuaskan'])
aturan16 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan17 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['memuaskan'])
aturan18 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['memuaskan'])

aturan19 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan20 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan21 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['memuaskan'])
aturan22 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan23 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['memuaskan'])
aturan24 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['memuaskan'])
aturan25 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['memuaskan'])
aturan26 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['memuaskan'])
aturan27 = ctrl.Rule(informasi_jelas['tidak memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['sangat memuaskan'])

aturan28 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan29 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan30 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan31 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan32 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan33 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['memuaskan'])
aturan34 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan35 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['memuaskan'])
aturan36 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['memuaskan'])

aturan37 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan38 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan39 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['memuaskan'])
aturan40 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan41 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['memuaskan'])
aturan42 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['memuaskan'])
aturan43 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['memuaskan'])
aturan44 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['memuaskan'])
aturan45 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['sangat memuaskan'])

aturan46 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan47 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['memuaskan'])
aturan48 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['memuaskan'])
aturan49 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['memuaskan'])
aturan50 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['memuaskan'])
aturan51 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['sangat memuaskan'])
aturan52 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['memuaskan'])
aturan53 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['sangat memuaskan'])
aturan54 = ctrl.Rule(informasi_jelas['cukup memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['sangat memuaskan'])

aturan55 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan56 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan57 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['memuaskan'])
aturan58 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan59 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['memuaskan'])
aturan60 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['memuaskan'])
aturan61 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['memuaskan'])
aturan62 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['memuaskan'])
aturan63 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['tidak memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['sangat memuaskan'])

aturan64 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['cukup memuaskan'])
aturan65 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['memuaskan'])
aturan66 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['memuaskan'])
aturan67 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['memuaskan'])
aturan68 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['memuaskan'])
aturan69 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['sangat memuaskan'])
aturan70 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['memuaskan'])
aturan71 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['sangat memuaskan'])
aturan72 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['cukup memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['sangat memuaskan'])

aturan73 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['memuaskan'])
aturan74 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['memuaskan'])
aturan75 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['tidak memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['sangat memuaskan'])
aturan76 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['memuaskan'])
aturan77 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['sangat memuaskan'])
aturan78 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['cukup memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['sangat memuaskan'])
aturan79 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], tingkat_kepuasan['sangat memuaskan'])
aturan80 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], tingkat_kepuasan['sangat memuaskan'])
aturan81 = ctrl.Rule(informasi_jelas['memuaskan'] & persyaratan_jelas['memuaskan'] & kompetensi_petugas['memuaskan'] & ketersediaan_fasilitas['memuaskan'], tingkat_kepuasan['sangat memuaskan'])

# 4. Sistem Kontrol dan Simulai
sistem_kepuasan = ctrl.ControlSystem([
    aturan1, aturan2, aturan3, aturan4, aturan5, aturan6, aturan7, aturan8, aturan9,
    aturan10, aturan11, aturan12, aturan13, aturan14, aturan15, aturan16, aturan17, aturan18,
    aturan19, aturan20, aturan21, aturan22, aturan23, aturan24, aturan25, aturan26, aturan27,
    aturan28, aturan29, aturan30, aturan31, aturan32, aturan33, aturan34, aturan35, aturan36,
    aturan37, aturan38, aturan39, aturan40, aturan41, aturan42, aturan43, aturan44, aturan45,
    aturan46, aturan47, aturan48, aturan49, aturan50, aturan51, aturan52, aturan53, aturan54,
    aturan55, aturan56, aturan57, aturan58, aturan59, aturan60, aturan61, aturan62, aturan63,
    aturan64, aturan65, aturan66, aturan67, aturan68, aturan69, aturan70, aturan71, aturan72,
    aturan73, aturan74, aturan75, aturan76, aturan77, aturan78, aturan79, aturan80, aturan81
])
simulasi_kepuasan = ctrl.ControlSystemSimulation(sistem_kepuasan)

# 5. Memasukkan Nilai Input Sesuai Soal
simulasi_kepuasan.input['informasi_jelas'] = 80
simulasi_kepuasan.input['persyaratan_jelas'] = 60
simulasi_kepuasan.input['kompetensi_petugas'] = 50
simulasi_kepuasan.input['ketersediaan_fasilitas'] = 90
# 6. Melakukan Perhitungan (Crushing/Compute)
simulasi_kepuasan.compute()

# 7. Output Hasil
hasil_kepuasan = simulasi_kepuasan.output['tingkat_kepuasan']
print("--- HASIL PERHITUNGAN LOGIKA FUZZY ---")
print(f"Kejelasan Informasi : 80")
print(f"Kejelasan Persyaratan     : 60")
print(f"Kemampuan petugas : 50")
print(f"ketersediaan sarpras         : 90")
print("--------------------------------------")
print(f"kepuasan pelayanan: {hasil_kepuasan:.2f} unit")

# Visualisasi (Opsional, butuh matplotlib)
informasi_jelas.view(sim=simulasi_kepuasan)
persyaratan_jelas.view(sim=simulasi_kepuasan)
kompetensi_petugas.view(sim=simulasi_kepuasan)
ketersediaan_fasilitas.view(sim=simulasi_kepuasan)
tingkat_kepuasan.view()