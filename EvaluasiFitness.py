# Data barang (nama, harga, bobot)
barang = [
("Barang1", 60, 10),
("Barang2", 100, 20),
("Barang3", 120, 30),
("Barang4", 90, 25),
("Barang5", 70, 15)
]
kapasitas_tas = 50 # Kapasitas maksimum tas
# Fungsi untuk menghitung nilai fitness
def hitung_fitness(kromosom, barang, kapasitas_tas):
    total_harga = 0
    total_bobot = 0
    for i in range(len(kromosom)):
        if kromosom[i] == 1: # Jika barang dipilih
            total_harga += barang[i][1] # Tambahkan harga
            total_bobot += barang[i][2] # Tambahkan bobot
    if total_bobot > kapasitas_tas: # Jika melebihi kapasitas, fitness = 0
        return 0  # Penalti jika melebihi kapasitas
    else:
        return total_harga # Fitness adalah total harga

# PERBAIKAN: Wrap contoh kode dengan if __name__ == "__main__"
# ALASAN: Saat import, kode di bawah tidak perlu dijalankan, hanya fungsi yang dibutuhkan
if __name__ == "__main__":
    # Definisi contoh populasi awal
    populasi_awal = [
        [1, 0, 1, 0, 1], # Contoh kromosom individu
        [0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1],
        # Tambahkan lebih banyak individu sesuai kebutuhan
    ]
    # Contoh penggunaan
    fitness_populasi = [hitung_fitness(individu, barang,
    kapasitas_tas) for individu in populasi_awal]

    # Menampilkan nilai fitness
    print("\nNilai Fitness:")
    for idx, fitness in enumerate(fitness_populasi):
        print(f"Individu {idx+1}: Fitness = {fitness}")
