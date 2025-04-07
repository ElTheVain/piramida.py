def simulasi_penginapan(saldo, biaya_per_malam_awal):
    malam = 0
    harga_penginapan = biaya_per_malam_awal
    hari_kerja = 0

    while True:
        if malam % 3 == 0:
            print(f"Mulai siklus baru. Harga per malam: {biaya_per_malam_awal:.2f}")
            harga_penginapan = biaya_per_malam_awal

        jam_kerja = 0  # reset setiap malam
        print(f"Malam ke-{malam + 1}:")
        print(f"- Saldo sebelum bayar: {saldo:.2f}")
        print(f"- Harga penginapan malam ini: {harga_penginapan:.2f}")

        if saldo >= harga_penginapan:
            saldo -= harga_penginapan
            malam += 1
            print(f"- Bayar penginapan. Sisa saldo: {saldo:.2f}")
            hari_kerja = 0
        else:
            print("- Saldo tidak cukup! X harus bekerja.")
            while saldo < harga_penginapan and jam_kerja < 3:
                jam_kerja += 1
                saldo += 3
                print(f"Kerja {jam_kerja} jam, saldo sekarang {saldo:.2f}")

            if saldo < harga_penginapan:
                print("Setelah bekerja, saldo tetap tidak cukup atau X sudah kerja 2 hari berturut-turut. X harus pulang.")
                break
            else:
                print("Cukup uang setelah bekerja!")
                saldo -= harga_penginapan
                malam += 1
                print(f"- Bayar penginapan. Sisa saldo: {saldo:.2f}")
                hari_kerja += 1
                if hari_kerja >= 2:
                    print("X sudah kerja 2 hari berturut-turut. X harus pulang.")
                    break

        # Diskon 5% jika belum reset
        if malam % 3 != 0:
            harga_penginapan *= 0.95

    print(f"X menginap selama {malam} malam sebelum kehabisan uang.")
