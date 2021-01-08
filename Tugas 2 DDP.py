data_a = open("transfer.txt")
data_x = open("nasabah.txt")
data_y = []
data_z = []
data_nama = []
data_rekening = []
data_saldo = []
data_mentah = []
data_transfer = []
data_g = []
for h in data_a:
    data_mentah.append(h.strip())
for i in data_mentah:
    data_transfer.append(i.split(","))
for g in range(len(data_transfer)):
  if data_transfer[g][1] not in data_g:
    data_g.append(data_transfer[g][1])
for p in data_x:
    data_y.append(p.strip())
for c in data_y:
    data_z.append(c.split(","))
for a in range(len(data_z)):
    data_rekening.append(data_z[a][0])
    data_nama.append(data_z[a][1])
    data_saldo.append(eval(data_z[a][2]))
data_tunai = dict(zip(data_rekening, data_saldo))
data_nasabah = dict(zip(data_rekening, data_nama))
def menu():
    print("Menu: ")
    print("[1] Buka Rekening Bank\n[2] Setoran Tunai\n[3] Tarik Tunai\n[4] Transfer\n[5] Lihat Daftar Transfer\n[6] Keluar")
print("***** SELAMAT DATANG DI NF BANK *****")
menu()
while True: 
    pilih = input("Masukkan menu pilihan anda: ")
    if pilih == '1':
        nama = input("Masukkan nama anda: ")
        setoran = eval(input("Masukkan Setoran Awal: "))
        import random, string
        norek =  "REK" + ''.join(random.choice(string.digits) for _ in range(3))
        print("Pembukaan dengan nomor rekening", norek, "atas nama", nama, "berhasil.\n")
        data_nama.append(nama)
        data_saldo.append(setoran)
        data_rekening.append(norek)
        data_tunai[norek] = setoran
        data_nasabah[norek] = nama
        menu()
    elif pilih == '2':
        print("*** SETORAN TUNAI ***")
        rek = input("Masukkan nomor rekening: ")
        nom = eval(input("Masukkan nominal yang akan disetor: "))
        if rek.upper() in data_rekening:
            print("Setoran tunai sebesar", nom, "ke rekening", rek, "berhasil.\n")
            tambah = data_tunai[rek.upper()] + nom
            data_tunai[rek.upper()] = tambah
        else:
            print("Nomor rekening tidak terdaftar. Setoran tunai gagal.\n")
        menu()
    elif pilih == '3':
        print("*** TARIK TUNAI ***")
        rek = input("Masukkan nomor rekening: ")
        nom = eval(input("Masukkan nominal yang akan disetor: "))
        if rek.upper() in data_rekening:
            if nom < data_tunai[rek.upper()]:
                kurang = data_tunai[rek.upper()]-nom
                data_tunai[rek.upper] = kurang
                print("Tarik tunai sebesar", nom, "dari rekening", rek, "berhasil.\n")
                data_tunai[rek.upper()] = kurang
            else:
                print("Saldo Tidak mencukupi.\n")
        else:
            print("Nomor rekening tidak terdaftar. Tarik tunai gagal.\n")
        menu()
    elif pilih == '4':
        print("*** TRANSFER ***")
        rek = input("Masukkan nomor rekening sumber: ")
        rek_tuj = input("Masukkan nomor rekening tujuan: ")
        nom = eval(input("Masukkan nominal yang akan disetor: "))
        if rek.upper() in data_rekening:
            if rek_tuj.upper() in data_rekening:
                if nom <= data_tunai[rek.upper()]:
                    tambah = data_tunai[rek_tuj.upper()]+nom
                    kurang = data_tunai[rek.upper()]-nom
                    data_tunai[rek.upper()] = kurang
                    data_tunai[rek_tuj.upper()] = tambah
                    print("Transfer sebesar", nom, "dari rekening", rek, "ke rekening" , rek_tuj,"berhasil.\n")
                    import random, string
                    trans = "TRF" + ''.join(random.choice(string.digits) for _ in range(3))
                    data_transfer.append([trans, rek.upper(), rek_tuj.upper(), nom])
                    data_g.append(rek.upper())
                else:
                    print("Saldo Tidak mencukupi. \n")
            else:
                print("Nomor rekening tujuan tidak terdaftar. Transfer gagal.\n")
        else:
            print("Nomor rekening sumber tidak terdaftar. Transfer gagal.\n")
        menu()
    elif pilih == '5':
        print("*** LIHAT DATA TRANSFER ***")
        rek = input("Masukkan nomor rekening sumber transfer: ")
        if rek.upper() in data_rekening:
          if rek.upper() in data_g:
                for wow in range(len(data_transfer)):
                    if rek.upper() == data_transfer[wow][1]:
                        print(data_transfer[wow][0], data_transfer[wow][1], data_transfer[wow][2], data_transfer[wow][3])
                print("\n")
          else:
            print("Tidak ada data yang ditampilkan.\n")
        else:
            print("Nomor rekening sumber tidak terdaftar.\n")
        menu()
    elif    pilih == '6':
        print("Terima kasih atas kunjungan anda")
        nasabah = open("nasabah.txt", "+w")
        for hapus in range(len(data_rekening)):
          nasabah.write(str(data_rekening[hapus])+ "," + str(data_nama[hapus]) + "," + str(data_tunai[data_rekening[hapus]])+ "\n")
        nasabah = open("transfer.txt", "+w")
        for hapus in range(len(data_transfer)):
            nasabah.write(str(data_transfer[hapus][0])+","+str(data_transfer[hapus][1])+","+str(data_transfer[hapus][2])+","+str(data_transfer[hapus][3])+"\n")
        nasabah.close()
        data_a.close()
        data_x.close()
        break
    else:
        print("Pilihan anda salah. Ulangi.")
