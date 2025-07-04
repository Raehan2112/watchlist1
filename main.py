import json
import os
from models.watch_item import Movie, Series

watchlist = []

def load_data():
    if os.path.exists("data/watchlist.json"):
        with open("data/watchlist.json", "r") as f:
            raw_data = json.load(f)
            for item in raw_data:
                if item["type"] == "Movie":
                    m = Movie(item["title"], item["genre"], item["duration"])
                else:
                    m = Series(item["title"], item["genre"], item["seasons"])
                m.watched = item["watched"]
                watchlist.append(m)

def save_data():
    data = []
    for item in watchlist:
        obj = {
            "type": "Movie" if isinstance(item, Movie) else "Series",
            "title": item.title,
            "genre": item.genre,
            "watched": item.watched
        }
        if isinstance(item, Movie):
            obj["duration"] = item.duration
        else:
            obj["seasons"] = item.seasons
        data.append(obj)
    with open("data/watchlist.json", "w") as f:
        json.dump(data, f, indent=4)

def tampilkan_daftar():
    if not watchlist:
        print("Belum ada daftar tontonan.")
        return
    for idx, item in enumerate(watchlist, start=1):
        print(f"{idx}. ", end="")
        item.display_info()

def tandai_selesai():
    tampilkan_daftar()
    pilih = int(input("Pilih nomor yang selesai ditonton: ")) - 1
    if 0 <= pilih < len(watchlist):
        watchlist[pilih].mark_as_watched()
        save_data()
        print("Berhasil ditandai sebagai sudah ditonton.")
    else:
        print("Pilihan tidak valid.")

def tambah_item():
    jenis = input("Jenis (movie/series): ").lower()
    title = input("Judul: ")
    genre = input("Genre: ")

    if jenis == "movie":
        dur = int(input("Durasi (menit): "))
        watchlist.append(Movie(title, genre, dur))
    elif jenis == "series":
        seas = int(input("Jumlah season: "))
        watchlist.append(Series(title, genre, seas))
    else:
        print("Jenis tidak dikenali.")
        return
    save_data()
    print("Tontonan berhasil ditambahkan!")

def main():
    load_data()
    while True:
        print("\n===== WatchListKu =====")
        print("1. Tambah Tontonan")
        print("2. Tampilkan Daftar")
        print("3. Tandai Sudah Ditonton")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_item()
        elif pilihan == "2":
            tampilkan_daftar()
        elif pilihan == "3":
            tandai_selesai()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
