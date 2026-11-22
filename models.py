class LaporanSampah:
    def __init__(self, id_laporan, lokasi, jenis_sampah, deskripsi):
        self.id_laporan = id_laporan
        self.lokasi = lokasi
        self.jenis_sampah = jenis_sampah
        self.deskripsi = deskripsi
        self.status = "Menunggu Penanganan"

    def tampilkan_data(self):
        print("ID Laporan: ", self.id_laporan)
        print("Lokasi: ", self.lokasi)
        print("Jenis Sampah: ", self.jenis_sampah)
        print("Deskripsi: ", self.deskripsi)
        print("Status: ", self.status)