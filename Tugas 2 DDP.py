diksi = {}
print("***** SELAMAT DATANG DI NF BANK *****")
print("Menu: ")
print("[1] Buka Rekening Bank\n[2] Setoran Tunai\n[3] Tarik Tunai\n[4] Transfer\n[5] Lihat Daftar Transfer\n[6] Keluar")
while True:
    pilih = input("Masukkan menu pilihan anda: ")
    if pilih == '1':
        nama = input("Masukkan nama anda: ")
        setoran = eval(input("Masukkan Setoran Awal: "))
        import random, string
        norek =  "REK" + ''.join(random.choice(string.digits) for _ in range(3))
        print("Pembukaan dengan nomor rekening", norek, "atas nama", nama, "berhasil.")
    elif pilih == '2':
        print("*** SETORAN TUNAI ***")
        rek = input("Masukkan nomor rekening: ")
        nom = eval(input("Masukkan nominal yang akan disetor: "))
        if rek in diksi:
            print("Setoran tunai sebesar", nom, "ke rekening", rek, "berhasil.")
        else:
            print("Nomor rekening tidak terdaftar. Setoran tunai gagal.")
    elif pilih == '3':
        print("*** TARIK TUNAI ***")
        rek = input("Masukkan nomor rekening: ")
        nom = eval(input("Masukkan nominal yang akan disetor: "))
        if rek in diksi:
            if nom < diksi[rek]:
                print("Tarik tunai sebesar", nom, "dari rekening", rek, "berhasil.")
            else:
                print("Saldo Tidak mencukupi")
        else:
            print("Nomor rekening tidak terdaftar. Tarik tunai gagal.")
    elif pilih == '4':
        print("*** TARIK TUNAI ***")
        rek = input("Masukkan nomor rekening sumber: ")
        rek_tuj = input("Masukkan nomor rekening tujuan: ")
        nom = eval(input("Masukkan nominal yang akan disetor: "))
        if rek in diksi:
            if rek_tuj in diksi:
                if nom < diksi[rek]:
                    print("Tarik tunai sebesar", nom, "dari rekening", rek, "berhasil.")
                else:
                    print("Saldo Tidak mencukupi")
            else:
                print("Nomor rekening tujuan tidak terdaftar. Transfer gagal")
        else:
            print("Nomor rekening sumber tidak terdaftar. Transfer gagal.")
    elif pilih == '5':
        print("*** LIHAT DATA TRANSFER ***")
        nom = input("Masukkan nomor rekening sumber transfer: ")
        if nom in diksi:
            if keys in diksi[nom]:
                print("")
            else:
                print("Tidak ada data yang ditampilkan.")
        else:
            print("Nomor rekening sumber tidak terdaftar.")

    elif pilih == '6':
        print("Terima kasih atas kunjungan anda")
        break
    else:
        print("Pilihan anda salah. Ulangi.")
