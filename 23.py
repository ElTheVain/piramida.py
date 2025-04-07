X adalah seorang perantau yang ingin tinggal di Kota A dengan budget terbatas. Untuk bertahan di sana, X harus membayar biaya penginapan per malam. Namun, harga penginapan dan aturan menginap di Kota A cukup kompleks, sehingga X memutuskan untuk membuat simulasi agar bisa mengetahui berapa lama ia dapat bertahan sebelum kehabisan uang.

Aturan Simulasi
Harga awal penginapan sudah ditentukan sebelum perjalanan dimulai.
Setiap malam, harga penginapan mendapat diskon 5% dari malam sebelumnya.
Setiap 3 malam, harga penginapan reset ke harga awal.
Jika saldo tidak cukup untuk membayar penginapan malam berikutnya, X dapat bekerja:
Setiap jam kerja, X mendapatkan uang sebanyak 3.
X dapat bekerja maksimal 3 jam dalam satu malam.
Jika setelah bekerja saldo masih tidak cukup, X harus pulang.
Jika X bekerja selama 2 hari berturut-turut, ia akan kelelahan dan harus pulang.
Program harus mencetak progres tiap malam, termasuk:
Saldo sebelum membayar.
Harga penginapan malam itu.
Proses kerja jika saldo tidak cukup.
Sisa saldo setelah membayar.
Parameter Fungsi
Fungsi ini memiliki dua parameter:

saldo (Integer) → jumlah uang yang dimiliki X saat memulai perjalanan.
biaya_per_malam_awal (Integer) → harga penginapan per malam sebelum diskon berlaku.
Aturan Output
Program akan menampilkan progres setiap malam dengan format berikut:

Malam ke-N:
Saldo sebelum bayar
Harga penginapan malam itu
Jika saldo kurang:
Jumlah jam kerja yang dilakukan
Saldo setelah bekerja
Jika setelah bekerja saldo masih kurang, X harus pulang
Jika X bekerja selama 2 hari berturut-turut, ia harus pulang
Jika berhasil menginap, sisa saldo setelah membayar
For example:

Test	Result
simulasi_penginapan(saldo=100, biaya_per_malam_awal=13)
Mulai siklus baru. Harga per malam: 13.00
Malam ke-1:
- Saldo sebelum bayar: 100.00
- Harga penginapan malam ini: 13.00
- Bayar penginapan. Sisa saldo: 87.00
Malam ke-2:
- Saldo sebelum bayar: 87.00
- Harga penginapan malam ini: 12.35
- Bayar penginapan. Sisa saldo: 74.65
Malam ke-3:
- Saldo sebelum bayar: 74.65
- Harga penginapan malam ini: 11.73
- Bayar penginapan. Sisa saldo: 62.92
Mulai siklus baru. Harga per malam: 13.00
Malam ke-4:
- Saldo sebelum bayar: 62.92
- Harga penginapan malam ini: 13.00
- Bayar penginapan. Sisa saldo: 49.92
Malam ke-5:
- Saldo sebelum bayar: 49.92
- Harga penginapan malam ini: 12.35
- Bayar penginapan. Sisa saldo: 37.57
Malam ke-6:
- Saldo sebelum bayar: 37.57
- Harga penginapan malam ini: 11.73
- Bayar penginapan. Sisa saldo: 25.84
Mulai siklus baru. Harga per malam: 13.00
Malam ke-7:
- Saldo sebelum bayar: 25.84
- Harga penginapan malam ini: 13.00
- Bayar penginapan. Sisa saldo: 12.84
Malam ke-8:
- Saldo sebelum bayar: 12.84
- Harga penginapan malam ini: 12.35
- Bayar penginapan. Sisa saldo: 0.49
Malam ke-9:
- Saldo sebelum bayar: 0.49
- Harga penginapan malam ini: 11.73
- Saldo tidak cukup! X harus bekerja.
Kerja 1 jam, saldo sekarang 3.49
Kerja 2 jam, saldo sekarang 6.49
Kerja 3 jam, saldo sekarang 9.49
Setelah bekerja, saldo tetap tidak cukup atau X sudah kerja 2 hari berturut-turut. X harus pulang.
X menginap selama 8 malam sebelum kehabisan uang.
simulasi_penginapan(saldo=50, biaya_per_malam_awal=13)
Mulai siklus baru. Harga per malam: 13.00
Malam ke-1:
- Saldo sebelum bayar: 50.00
- Harga penginapan malam ini: 13.00
- Bayar penginapan. Sisa saldo: 37.00
Malam ke-2:
- Saldo sebelum bayar: 37.00
- Harga penginapan malam ini: 12.35
- Bayar penginapan. Sisa saldo: 24.65
Malam ke-3:
- Saldo sebelum bayar: 24.65
- Harga penginapan malam ini: 11.73
- Bayar penginapan. Sisa saldo: 12.92
Mulai siklus baru. Harga per malam: 13.00
Malam ke-4:
- Saldo sebelum bayar: 12.92
- Harga penginapan malam ini: 13.00
- Saldo tidak cukup! X harus bekerja.
Kerja 1 jam, saldo sekarang 15.92
Cukup uang setelah bekerja!
- Bayar penginapan. Sisa saldo: 2.92
Malam ke-5:
- Saldo sebelum bayar: 2.92
- Harga penginapan malam ini: 12.35
- Saldo tidak cukup! X harus bekerja.
Kerja 1 jam, saldo sekarang 5.92
Kerja 2 jam, saldo sekarang 8.92
Kerja 3 jam, saldo sekarang 11.92
Setelah bekerja, saldo tetap tidak cukup atau X sudah kerja 2 hari berturut-turut. X harus pulang.
X menginap selama 4 malam sebelum kehabisan uang.


def simulasi_penginapan(saldo, biaya_per_malam_awal):
    malam_ke = 1
    hari_kerja_berturut = 0
    harga_malam = biaya_per_malam_awal
    malam_siklus = 1  # Untuk melacak kapan harus reset ke harga awal

    while True:
        if malam_siklus == 1:
            print(f"Mulai siklus baru. Harga per malam: {biaya_per_malam_awal:.2f}")

        print(f"Malam ke-{malam_ke}:")
        print(f"- Saldo sebelum bayar: {saldo:.2f}")
        print(f"- Harga penginapan malam ini: {harga_malam:.2f}")

        if saldo >= harga_malam:
            saldo -= harga_malam
            print(f"- Bayar penginapan. Sisa saldo: {saldo:.2f}")
            hari_kerja_berturut = 0
        else:
            print("- Saldo tidak cukup! X harus bekerja.")
            jam_kerja = 0

            while saldo < harga_malam and jam_kerja < 3:
                saldo += 3
                jam_kerja += 1
                print(f"Kerja {jam_kerja} jam, saldo sekarang {saldo:.2f}")

            if saldo >= harga_malam:
                hari_kerja_berturut += 1
                if hari_kerja_berturut >= 2:
                    print("Setelah bekerja, saldo cukup, tapi X sudah kerja 2 hari berturut-turut. X harus pulang.")
                    break
                print("Cukup uang setelah bekerja!")
                saldo -= harga_malam
                print(f"- Bayar penginapan. Sisa saldo: {saldo:.2f}")
            else:
                print("Setelah bekerja, saldo tetap tidak cukup atau X sudah kerja 2 hari berturut-turut. X harus pulang.")
                break

        # Update malam ke dan siklus
        malam_ke += 1
        malam_siklus += 1

        if malam_siklus > 3:
            malam_siklus = 1
            harga_malam = biaya_per_malam_awal
        else:
            harga_malam *= 0.95

    print(f"X menginap selama {malam_ke - 1} malam sebelum kehabisan uang.")

