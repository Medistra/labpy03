print ("Program mengurutkan data berdasarkan input")

data = []
for i in range (10):
    x = int(input("Masukan bilangan: "))
    data.append(x)
print ("data sebelum diurutkan: ",data)
list.sort(data)
print("data setelah diurutkan: ",data)