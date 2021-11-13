a = int(input("Masukan bilangan A: "))
b = int(input("Masukan bilangan B: "))
c = int(input("Masukan bilangan C: "))

if a+b == c or b+c == a or c+a == b:
    print("Benar")
else:
    print("Salah")