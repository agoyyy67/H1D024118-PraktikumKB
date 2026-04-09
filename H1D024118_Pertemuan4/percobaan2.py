# --- DATABASE PENYAKIT (Knowledge Base) ---
# Berdasarkan tabel gejala pada modul [cite: 160]
knowledge_base = {
    "tertiana": {"nyeri_otot", "muntah", "kejang"},
    "quartana": {"nyeri_otot", "menggigil", "tidak_enak_badan"},
    "tropika": {"keringat_dingin", "sakit_kepala", "mimisan", "mual"},
    "pernisiosa": {"menggigil", "tidak_enak_badan", "demam", "mimisan", "mual"}
}

# --- REPRESETASI FAKTA DINAMIS ---
# Meniru perilaku 'assertz' dan 'retract' di Prolog 
gejala_pasien = set()

def tambah_gejala(gejala):
    """Fungsi ini seperti assertz di Prolog"""
    gejala_pasien.add(gejala)
    print(f"Menambah fakta: {gejala}")

def hapus_gejala(gejala):
    """Fungsi ini seperti retract di Prolog"""
    gejala_pasien.discard(gejala)
    print(f"Menghapus fakta: {gejala}")

def diagnosa(nama_pasien):
    """Mengecek apakah gejala pasien memenuhi syarat penyakit tertentu"""
    ditemukan = False
    for penyakit, syarat_gejala in knowledge_base.items():
        # Mengecek apakah semua syarat_gejala ada di gejala_pasien
        if syarat_gejala.issubset(gejala_pasien):
            print(f"HASIL: {nama_pasien} terdeteksi mengidap Malaria {penyakit.capitalize()}.")
            ditemukan = True
    
    if not ditemukan:
        print(f"HASIL: {nama_pasien} belum terdeteksi penyakit tertentu.")

# --- SIMULASI SESUAI MODUL [cite: 199-208] ---

print("=== Simulasi Percobaan 2 (Python Version) ===")

# 1. Cek awal (Belum ada gejala)
diagnosa("Steph")

# 2. Tambah gejala (Simulasi Malaria Quartana) [cite: 201]
print("\n--- Input Gejala 1 ---")
tambah_gejala("nyeri_otot")
tambah_gejala("menggigil")
tambah_gejala("tidak_enak_badan")
diagnosa("Steph") # Output: Quartana

# 3. Hapus gejala dan ganti (Simulasi Malaria Pernisiosa) [cite: 203-208]
print("\n--- Update Gejala ---")
hapus_gejala("nyeri_otot")
tambah_gejala("demam")
tambah_gejala("mimisan")
tambah_gejala("mual")
diagnosa("Steph") # Output: Pernisiosa