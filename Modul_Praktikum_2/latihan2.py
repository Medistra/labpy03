gaji = int(input("Masukann gaji:"))
berkeluarga = (False, True)[input("Sudah berkeluarga? (Y/T)") == "Y"]
punya_rumah = (False, True)[input("Punya rumah? (Y/T)") == "Y"]

if gaji > 3000000:
    print ("Gaji sudah diatass UMR")
    if berkeluarga:
     print ("- Wajib ikutan asuransi dan menabung untuk pensiun")
    else:
        print ("- Tidak perlu ikutan asuransi")
    if punya_rumah:
        print ("- Wajib bayar pajakk rummah")
    else:
        print ("- Tidak wajib bayar pajak rumah")
else:
    print ("gaji belum UMR")