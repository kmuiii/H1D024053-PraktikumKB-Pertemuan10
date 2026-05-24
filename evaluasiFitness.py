def hitung_fitness(kromosom, barang, max_gudang):
    total_keuntungan = 0
    total_bobot = 0
    for i in range(len(kromosom)):
        if kromosom[i] == 1:
            total_keuntungan += barang[i][1]
        total_bobot += barang[i][2]
        if total_bobot > max_gudang:
            return 0 # Penalti jika melebihi kapasitas
        else:
            return total_keuntungan