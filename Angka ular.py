def ularAngka(bawah, samping):
    num = 1
    for i in range(bawah):
        row = []
        if i % 2 == 0:
            for j in range(samping):
                row.append(num)
                num += 1
        else:
            for j in range(samping):
                row.insert(0, num)
                num += 1

        if i == 0:
            row[0] = "head"

        if i == bawah - 1:
            if bawah % 2 == 0:
                row[-samping] = "tail"
            else:
                row[-1] = "tail"

        print(" ".join(f"{n:02d}" if isinstance(n, int) else f"{n:>4}" for n in row))
