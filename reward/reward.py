from database.config import player_name
from database.user import get_user, update_user


def cek_tingkat(total_level):
    if 10 <= total_level < 20:
        tingkat = "Tingkat 1 = Bronze"
    elif 20 <= total_level < 30:
        tingkat = "Tingkat 2 = Silver"
    elif 30 <= total_level < 40:
        tingkat = "Tingkat 3 = Gold"
    elif 40 <= total_level < 50:
        tingkat = "Tingkat 4 = Diamond"
    elif 50 <= total_level < 60:
        tingkat = "Tingkat 5 = Master"
    elif total_level == 60:
        tingkat = "Tingkat 6 = Legendary"
    else:
        tingkat = ""
    
    return tingkat

def proses_level(kategori, nyawa, level_dikerjakan):
    user_data = get_user(player_name)
    total_level = user_data[0]
    tingkat = cek_tingkat(total_level)
    update_user(kategori, nyawa, level_dikerjakan, tingkat)
    
    print(f"Kategori: {kategori}, Level ke-{level_dikerjakan} selesai.")
    print(f"Total level yang sudah dikerjakan dari semua kategori soal: {total_level}")
    
    if total_level % 10 == 0 and total_level != 0:
        print(f"🎉 Selamat! Anda naik ke {tingkat}")