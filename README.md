# Tugas Praktikum 4 

## Program Data Nilai Mahasiswa 
Pada praktikum 4 ini kita akan membuat program sederhana untuk menginput data nilai mahasiswa. Berikut syntaxnya:
```
nilai = []                                                                    

ulangi = True                                                                 

while ulangi:                                                                 
    nama = input("Masukan Nama: ")                                            
    nim = input("Masukan NIM: ")                                              
    tugas = int(input("Masukan Nilai Tugas: "))                               
    uts = int(input("Masukan Nilai UTS: "))                                   
    uas = int(input("Masukan Nilai UAS: "))                                   
    akhir = (tugas * 30/100) + (uts * 35/100) + (uas * 35/100)                

    nilai.append([nama, nim, int(tugas), int(uts), int(uas), int(akhir)])     
    if (input("tambah data lagi (y/t)?") == 't'):                             
        ulangi = False                                                        

print("\nDaftar Nilai Mahasiswa: ")                                            
print("====================================================================")
print("| NO |     Nama     |    NIM    |  Tugas  |  UTS  |  UAS  |  Akhir |")
print("====================================================================")
i=0
for item in nilai:                                                        
    i+=1
    print("| {no:2d} | {nama:12s} | {nim:9s} | {tugas:7d} | {uts:5d} | {uas:5d} | {akhir:6.2f} |"
          .format(no=i, nama=item[0], nim=item[1], tugas=item[2], uts=item[3], uas=item[4], akhir=item[5]))
print("====================================================================")
```

## Penjelasan 
1. Pertama kita membuat variable list kosong yang nantinya akan di inpukan dengan data yang diinginkan. Dan ```ulang = True``` digunakan untuk mengontrol pengulangan 
   ```
   nilai = []                                                                    # Berfungsi sebagai integer list

   ulangi = True                                                                 # Statement true jika pengulangan kondisi bernilai benar
   ```
2. Setelah itu, kita membuat kondisi perulangan dan statement yang akan dijalankan ketika perulangan terjadi. Dan fungsi 'append' disini digunakan untuk menambahkan item di akhir list. 
   ```
   while ulangi:                                                                 # Statement while untuk pengulangan
       nama = input("Masukan Nama: ")                                            # Menginputkan nama
       nim = input("Masukan NIM: ")                                              # Menginputkan NIM
       tugas = int(input("Masukan Nilai Tugas: "))                               # Menginputkan nilai tugas
       uts = int(input("Masukan Nilai UTS: "))                                   # Menginputkan nilai UTS
       uas = int(input("Masukan Nilai UAS: "))                                   # Menginputkan nilai UAS
       akhir = (tugas * 30/100) + (uts * 35/100) + (uas * 35/100)                # Penjumlahan nilai Akhir

       nilai.append([nama, nim, int(tugas), int(uts), int(uas), int(akhir)])     # Gunakan fungsi append untuk menambahkan item di akhir list dan list menjadi rapih
   ```
3. Berikutnya, setelah membuat perulangan, kita membuat statement untuk memberhentikan perulangan, dengan cara menginputkan 't' apabila diminta saat program dijalankan. 't' akan membuat variable ```ulang = True``` menjadi ```ulang = False``` yang akan menghentikan pengulangan.
   ```
       if (input("tambah data lagi (y/t)?") == 't'):                             # Kondisi untuk menambahkan data atau tidak
           ulangi = False                                                        # Statement false untuk menghentikan pengulangan
   ```
4. Terakhir kita membuat perintah untuk mencetak hasil dari yang di buat.
   ```
   print("\nDaftar Nilai Mahasiswa: ")                                           # Format untuk mengetahui outputnya
   print("====================================================================")
   print("| NO |     Nama     |    NIM    |  Tugas  |  UTS  |  UAS  |  Akhir |")
   print("====================================================================")
   i=0
   for item in nilai:                                                            # Dimasukan kondisi/status untuk daftar nilai
       i+=1                                                                      # Untuk mengisi di bagian  Nomor                          
       print("| {no:2d} | {nama:12s} | {nim:9s} | {tugas:7d} | {uts:5d} | {uas:5d} | {akhir:6.2f} |"
             .format(no=i, nama=item[0], nim=item[1], tugas=item[2], uts=item[3], uas=item[4], akhir=item[5]))
   print("====================================================================")
   ```

