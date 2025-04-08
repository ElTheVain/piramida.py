def hitung_jarak_tempuh(kecepatan_awal, waktu_awal, faktor_cuaca, faktor_jalan,
                         faktor_bbm, faktor_lampu_merah, faktor_beban, faktor_kondisi_ban):
    
    kecepatan = kecepatan_awal
    waktu = waktu_awal
    total_jarak = 0

    for bulan in range(1, 6):  # dari bulan 1 sampai 5
        # Penyesuaian kecepatan & waktu berdasarkan bulan
        if bulan % 2 == 1:  # bulan ganjil: 1, 3, 5
            kecepatan *= 0.95
            waktu *= 0.95
        elif bulan == 2:
            kecepatan *= 1.10
            waktu *= 1.10
        elif bulan == 4:
            kecepatan *= 1.15
            waktu *= 1.15

        # Pengaruh faktor eksternal terhadap kecepatan & waktu
        kecepatan_dipengaruhi = kecepatan * faktor_cuaca * faktor_bbm * faktor_kondisi_ban
        waktu_dipengaruhi = waktu * faktor_jalan * faktor_lampu_merah * faktor_beban

        # Hitung jarak
        jarak = kecepatan_dipengaruhi * waktu_dipengaruhi
        total_jarak += jarak

        print(f"Jarak tempuh bulan {bulan}: {jarak:.2f} km")

    print(f"Total jarak tempuh selama 5 bulan: {total_jarak:.2f} km")
