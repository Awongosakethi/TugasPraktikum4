nilai = []                                                                    # Berfungsi sebagai integer list

ulangi = True                                                                 # Statement true jika pengulangan kondisi bernilai benar

while ulangi:                                                                 # Statement while untuk pengulangan
    nama = input("Masukan Nama: ")                                            # Menginputkan nama
    nim = input("Masukan NIM: ")                                              # Menginputkan NIM
    tugas = int(input("Masukan Nilai Tugas: "))                               # Menginputkan nilai tugas
    uts = int(input("Masukan Nilai UTS: "))                                   # Menginputkan nilai UTS
    uas = int(input("Masukan Nilai UAS: "))                                   # Menginputkan nilai UAS
    akhir = (tugas * 30/100) + (uts * 35/100) + (uas * 35/100)                # Penjumlahan nilai Akhir

    nilai.append([nama, nim, int(tugas), int(uts), int(uas), int(akhir)])     # Gunakan fungsi append untuk menambahkan item di akhir list dan list menjadi rapih
    if (input("tambah data lagi (y/t)?") == 't'):                             # Kondisi untuk menambahkan data atau tidak
        ulangi = False                                                        # Statement false untuk menghentikan pengulangan

print("\nDaftar Nilai Mahasiswa: ")                                           # Format untuk mengetahui outputnya
print("====================================================================")
print("| NO |     Nama     |    NIM    |  Tugas  |  UTS  |  UAS  |  Akhir |")
print("====================================================================")
i=0
for item in nilai:                                                           # Dimasukan kondisi/status untuk daftar nilai
    i+=1                                                                     # Untuk mengisi di bagian  Nomor
    print("| {no:2d} | {nama:12s} | {nim:9s} | {tugas:7d} | {uts:5d} | {uas:5d} | {akhir:6.2f} |"
          .format(no=i, nama=item[0], nim=item[1], tugas=item[2], uts=item[3], uas=item[4], akhir=item[5]))
print("====================================================================")
