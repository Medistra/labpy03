print("Program Mencari Bilangan Terbesar Dari 3 Bilangan")

a = int(input("Masukkan Bilangan Pertama: "))
b = int(input("Masukkan Bilangan Kedua: "))
c = int(input("Masukkan Bilangan Ketiga: "))

if a > b > c:
    print("Bilangan Pertama Adalah Bilangan Terbesar = %s" % a)
elif b> c:
    print("Bilangan Kedua Adalah Bilangan Terbesar = %s" % b)
else:
    print("Bilangan Ketiga Adalah Bilangan Terbesar = %s" % c)