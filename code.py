def segitigaPensiunPersegiGajian(n):
    if type(n) != int or n <= 0:
        print("Ouput Yang Tersedia")
        return

    # Segitiga terbalik
    for i in range(n):
        print("  " * i + "* " * (n - i))

    # Persegi pola bergantian
    for i in range(n):
        for j in range(n):
            if i % 2 == 0 and j % 2 == 0:
                print("#", end=" ")
            elif i % 2 == 0 and j % 2 == 1:
                print("*", end=" ")
            else:
                print("*", end=" ")
        print()
#pilihan k2
def segitigaPensiunPersegiGajian(n):
    if n <= 0 or not isinstance(n, int):
        print("Ouput Yang Tersedia")
        return

    # Cetak segitiga terbalik
    baris = 0
    while baris < n:
        spasi = 0
        while spasi < baris:
            print("  ", end="")
            spasi += 1
        bintang = 0
        while bintang < n - baris:
            print("* ", end="")
            bintang += 1
        print()
        baris += 1

    # Cetak persegi bergantian
    baris = 0
    while baris < n:
        kolom = 0
        while kolom < n:
            if baris % 2 == 0:
                if kolom % 2 == 0:
                    print("#", end=" ")
                else:
                    print("*", end=" ")
            else:
                print("*", end=" ")
            kolom += 1
        print()
        baris += 1
      #pilihan ke 3
def segitigaPensiunPersegiGajian(n):
    if type(n) != int or n <= 0:
        print("Ouput Yang Tersedia")
    else:
        # Pola segitiga terbalik
        for i in range(n):
            for j in range(n):
                if j < i:
                    print("  ", end="")
                else:
                    print("* ", end="")
            print()

        # Pola persegi bergantian
        for i in range(n):
            for j in range(n):
                if i % 2 == 0 and j % 2 == 0:
                    print("#", end=" ")
                elif i % 2 == 0 and j % 2 == 1:
                    print("*", end=" ")
                else:
                    print("*", end=" ")
            print()


            #untuk soal piramida wisnu
def segitigaPensiunPersegiGajian(n):
    # Cek apakah n adalah bilangan bulat positif
    if n <= 0:
        print("Ouput Yang Tersedia")
        return
    
    # Mencetak segitiga terbalik
    for i in range(n):
        print(' ' * i, end='')
        print('* ' * (n - i))
    
    # Mencetak persegi bergantian
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print('*', end=' ')
            else:
                print('#', end=' ')
        print()  

# Contoh penggunaan
segitigaPensiunPersegiGajian(6)
print()  # Untuk memberikan jarak antara output
segitigaPensiunPersegiGajian(7)
print()  # Untuk memberikan jarak antara output
segitigaPensiunPersegiGajian(15)
