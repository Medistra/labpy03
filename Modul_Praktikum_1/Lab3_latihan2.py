print ("program menampilkan n (bilangan acak) yang lebih dari 0.5")

jumlah = int(input("Masukan jumlah n : "))
import random
for i in range (jumlah):
    print("data ke", i+1,"=",(random.uniform(0.1,0.5)))
