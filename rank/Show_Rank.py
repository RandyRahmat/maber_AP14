# comment 1. Panggil >> showing_rank << dengan variable nama_player dan point_player untuk menampilkan rank player di main menu atau laman lainnya

class Warna:
    RESET = '\033[0m'
    LEGENDARY = '\033[95m'  # Magenta Cerah
    MASTER = '\033[91m'     # Merah Cerah
    DIAMOND = '\033[96m'    # Cyan Cerah
    GOLD = '\033[93m'       # Kuning Cerah
    SILVER = '\033[37m'     # Putih (sering digunakan untuk Silver)
    BRONZE = '\033[33m'     # Oranye/Coklat muda

def Rank(Player_point):
    if Player_point >= 1000:
        return Warna.LEGENDARY + "Legendary" + Warna.RESET
    elif Player_point >= 750:
        return Warna.MASTER + "Master" + Warna.RESET
    elif Player_point >= 500:
        return Warna.DIAMOND + "Diamond" + Warna.RESET
    elif Player_point >= 250:
        return Warna.GOLD + "Gold" + Warna.RESET
    elif Player_point >= 100:
        return Warna.SILVER + "Silver" + Warna.RESET
    else:
        return Warna.BRONZE + "Bronze" + Warna.RESET

# Ini function yang dimaksud oleh comment 1 
def showing_rank(nama_player, point_player):
    print("====================================")
    print("=         RANKING PLAYER          =")
    print("====================================")
    print("= Nama Player : " + nama_player)
    print("= Rank Player : " + Rank(point_player))
    print("====================================")


# Contoh penggunaan
showing_rank("Ade Fahreza", 850)