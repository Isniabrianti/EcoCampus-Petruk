import csv
from pathlib import Path
from models import LaporanSampah

FILE_DATA = Path(__file__).parent / "data" / "laporan.csv"

def simpan_laporan(daftar_laporan):
    FILE_DATA.parent.mkdir(parents=True, exist_ok=True)

    with open(FILE_DATA, "w", newline="", encoding="utf-8") as file:
        kolom = [
            "id_laporan",
            "lokasi",
            "jenis_sampah",
            "deskripsi",
            "status"
        ]

        penulis = csv.DictWriter(file, fieldnames=kolom)
        penulis.writeheader()

        for laporan in daftar_laporan:
            penulis.writerow({
                "id_laporan": laporan.id_laporan,
                "lokasi": laporan.lokasi,
                "jenis_sampah": laporan.jenis_sampah,
                "deskripsi": laporan.deskripsi,
                "status": laporan.status
            })

def muat_laporan():
    daftar_laporan = []
    try:
        with open(FILE_DATA, "r", newline="", encoding="utf-8") as file:
            pembaca = csv.DictReader(file)

            for baris in pembaca:
                laporan = LaporanSampah(
                    int(baris["id_laporan"]),
                    baris["lokasi"],
                    baris["jenis_sampah"],
                    baris["deskripsi"]
                )
                laporan.status = baris["status"]
                daftar_laporan.append(laporan)

    except FileNotFoundError:
        print("File laporan belum tersedia")
        
    return daftar_laporan