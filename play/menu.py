from ui_utils import info, line, space, text_left, warning


def chooseCategory():
    while True:
        space()
        text_left("Pilih Kategori Soal:")
        text_left("1. Aritmatika Dasar ➗")
        text_left("2. Teka Teki Gambar 🟰")
        text_left("3. Deret Angka 📏")
        text_left("4. Kembali ke Menu Utama 🔙")
        space()

        choice = input("Pilih opsi (1-4): ")

        if choice == "1":
            info("Kamu memilih kategori Aritmatika Dasar.")

        elif choice == "2":
            info("Kamu memilih kategori Teka Teki Gambar.")

        elif choice == "3":
            info("Kamu memilih kategori Deret Angka.")

        elif choice == "4":
            info("Kembali ke Menu Utama.")
            break
        else:
            warning("Opsi tidak valid. Silakan coba lagi.")