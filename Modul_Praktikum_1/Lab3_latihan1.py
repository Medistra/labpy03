print("Program dengan perulangan bertingkat (nested)")

angka = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
baris = 10

for jumlah in range(baris):
    
    print(*angka, sep="\t")
    for coloum in range(10):
        angka[coloum] = angka[coloum]+1