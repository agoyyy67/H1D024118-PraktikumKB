import os
import time

# =====================================
# HMIF Task & Event Organizer
# =====================================

# Struktur data: list berisi dictionary
tasks = []


def tambah_tugas():
    print("\n=== Tambah Tugas / Proker ===")

    nama = input("Nama Proker        : ")
    deadline = input("Deadline (YYYY-MM-DD): ")
    divisi = input("Divisi Penanggung Jawab : ")

    task = {
        "nama": nama,
        "deadline": deadline,
        "divisi": divisi,
        "status": "Belum Selesai"
    }

    tasks.append(task)

    # Library os → membuat folder dokumentasi
    folder_name = f"dokumentasi_{nama.replace(' ', '_')}"

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    print("Tugas berhasil ditambahkan.")
    print(f"Folder dokumentasi '{folder_name}' dibuat.\n")


def tampilkan_tugas():
    print("\n=== Daftar Tugas HMIF ===")

    if not tasks:
        print("Belum ada tugas yang tercatat.\n")
        return

    for i, task in enumerate(tasks, start=1):
        print(
            f"{i}. {task['nama']} | "
            f"Deadline: {task['deadline']} | "
            f"Divisi: {task['divisi']} | "
            f"Status: {task['status']}"
        )

    print()


def cari_tugas():
    print("\n=== Cari Tugas Belum Selesai ===")

    keyword = input("Masukkan nama proker: ")
    ditemukan = False

    for task in tasks:

        if keyword.lower() not in task["nama"].lower():
            continue

        if task["status"] == "Belum Selesai":
            print("\nTugas ditemukan:")
            print(task)
            ditemukan = True
            break

    if not ditemukan:
        print("Tugas tidak ditemukan atau sudah selesai.\n")


def tandai_selesai():
    tampilkan_tugas()

    if not tasks:
        return

    try:
        nomor = int(input("Pilih nomor tugas yang selesai: "))

        if 1 <= nomor <= len(tasks):
            tasks[nomor - 1]["status"] = "Selesai"
            print("Status tugas diperbarui.\n")
        else:
            print("Nomor tidak valid.\n")

    except ValueError:
        print("Input harus berupa angka.\n")


def pengingat_tugas():
    print("\nMenjalankan pengingat tugas...")
    time.sleep(2)

    for task in tasks:
        if task["status"] == "Belum Selesai":
            print(f"Reminder: '{task['nama']}' belum selesai!")

    print()


def tampilkan_menu():
    print("=================================")
    print("      HMIF TASK ORGANIZER")
    print("=================================")
    print("1. Tambah Tugas / Proker")
    print("2. Lihat Semua Tugas")
    print("3. Cari Tugas Belum Selesai")
    print("4. Tandai Tugas Selesai")
    print("5. Jalankan Pengingat")
    print("6. Keluar")
    print("=================================")


# Program utama
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_tugas()

    elif pilihan == "2":
        tampilkan_tugas()

    elif pilihan == "3":
        cari_tugas()

    elif pilihan == "4":
        tandai_selesai()

    elif pilihan == "5":
        pengingat_tugas()

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.\n")
