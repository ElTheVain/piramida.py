def hitung_jarak_tempuh(kecepatan_awal, waktu_awal, faktor_cuaca, faktor_jalan, faktor_bbm, faktor_lampu_merah, faktor_beban, faktor_kondisi_ban):
    kecepatan = kecepatan_awal
    waktu = waktu_awal
    total_jarak = 0

    bulan = 1
    while bulan <= 5:
        # Perubahan bulanan
        if bulan % 2 == 1:  # Bulan ganjil: 1, 3, 5 → turun 5%
            kecepatan = kecepatan * 0.95
            waktu = waktu * 0.95
        elif bulan == 2:  # Bulan ke-2 → naik 10% dari bulan ke-1
            kecepatan = kecepatan * 1.10
            waktu = waktu * 1.10
        elif bulan == 4:  # Bulan ke-4 → naik 15% dari bulan ke-3
            kecepatan = kecepatan * 1.15
            waktu = waktu * 1.15

        # Koreksi dengan faktor eksternal
        kecepatan_koreksi = kecepatan * faktor_cuaca * faktor_bbm * faktor_kondisi_ban
        waktu_koreksi = waktu * faktor_jalan * faktor_lampu_merah * faktor_beban

        # Hitung jarak bulan ini
        jarak = kecepatan_koreksi * waktu_koreksi
        total_jarak += jarak

        print(f"Jarak tempuh bulan {bulan}: {jarak:.2f} km")

        bulan += 1

    print(f"Total jarak tempuh selama 5 bulan: {total_jarak:.2f} km")
          
