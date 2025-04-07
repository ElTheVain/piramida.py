def simulasi_penginapan(saldo, biaya_per_malam_awal):
    # Inisialisasi variabel
    malam = 0
    harga_penginapan = biaya_per_malam_awal
    kerja_hari_berturut_turut = 0

    while True:
        malam += 1
        print(f"Malam ke-{malam}:")
        print(f"- Saldo sebelum bayar: {saldo:.2f}")
        print(f"- Harga penginapan malam ini: {harga_penginapan:.2f}")

        # Cek apakah saldo cukup untuk membayar penginapan
        if saldo >= harga_penginapan:
            saldo -= harga_penginapan
            print(f"- Bayar penginapan. Sisa saldo: {saldo:.2f}")
            kerja_hari_berturut_turut = 0  # Reset hari kerja berturut-turut
        else:
            print("- Saldo tidak cukup! X harus bekerja.")
            jam_kerja = 0
            while saldo < harga_penginapan and jam_kerja < 3:
                jam_kerja += 1
                saldo += 3
                print(f"Kerja {jam_kerja} jam, saldo sekarang {saldo:.2f}")

         
            if saldo < harga_penginapan or kerja_hari_berturut_turut == 1:
                print("Setelah bekerja, saldo tetap tidak cukup atau X sudah kerja 2 hari berturut-turut. X harus pulang.")
                break
            
            print("Cukup uang setelah bekerja!")
            saldo -= harga_penginapan
            print(f"- Bayar penginapan. Sisa saldo: {saldo:.2f}")
        if malam % 3 == 0:
            harga_penginapan = biaya_per_malam_awal
            print(f"Mulai siklus baru. Harga per malam: {harga_penginapan:.2f}")
        else:
            harga_penginapan *= 0.95  # Diskon 5%
        if jam_kerja > 0:
            kerja_hari_berturut_turut += 1
        else:
            kerja_hari_berturut_turut = 0

    print(f"X menginap selama {malam - 1} malam sebelum kehabisan uang.")

# Contoh penggunaan
simulasi_penginapan(saldo=100, biaya_per_malam_awal=13)
print()  # Untuk memberikan jarak antara output
simulasi_penginapan(saldo=50, biaya_per_malam_awal=13)
