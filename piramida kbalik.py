def print_star_pattern(n):
    for i in range(n):
        # Mencetak spasi
        print(' ' * (2 * i), end='')
        # Mencetak bintang
        print('* ' * (n - i))

# Jumlah baris pola
n = 7
print_star_pattern(n)
