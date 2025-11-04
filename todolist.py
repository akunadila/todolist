# todolist.py
tasks = []

while True:
    print("\nTo-Do List")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        tugas = input("Masukkan tugas baru: ")
        tasks.append(tugas)
        print(f"Tugas '{tugas}' berhasil ditambahkan.")
    elif pilihan == "2":
        print("\nDaftar Tugas:")
        if not tasks:
            print("Belum ada tugas.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
    elif pilihan == "3":
        hapus = int(input("Masukkan nomor tugas yang akan dihapus: "))
        if 0 < hapus <= len(tasks):
            print(f"Tugas '{tasks[hapus-1]}' dihapus.")
            tasks.pop(hapus-1)
        else:
            print("Nomor tidak valid.")
    elif pilihan == "4":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid.")
