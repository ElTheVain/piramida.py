def piramida_ke_kanan(n):
    for i in range(n):
        # Mencetak spasi
        print(' ' * (n - i - 1), end='')
        # Mencetak bintang
        print('* ' * (i + 1))

# Contoh penggunaan
piramida_ke_kanan(5)

def piramida_ke_kiri(n):
    for i in range(n):
        # Mencetak bintang
        print('* ' * (i + 1))

# Contoh penggunaan
piramida_ke_kiri(5)
