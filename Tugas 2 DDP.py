print("***** SELAMAT DATANG DI NF BANK *****")
print("Menu: ")
print("[1] Buka Rekening Bank\n[2] Setoran Tunai\n[3] Tarik Tunai\n[4] Transfer\n[5] Lihat Daftar Transfer\n[6] Keluar")
while True:
    pilih = eval(input("Masukkan menu pilihan anda: "))
    if pilih == 1:
        nama = input("Masukkan nama anda: ")
        setoran = eval(input("Masukkan Setoran Awal: "))
        import random, string
        norek =  "REK" + ''.join(random.choice(string.digits) for _ in range(3))
        print("Pembukaan dengan nomor rekening", norek, "atas nama", nama, "berhasil.")
            
    elif pilih == 6:
        print("Terima kasih atas kunjungan anda")
        break
    else:
        print("Pilihan anda salah. Ulangi.")
