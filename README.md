# Praktikum5
Anggita Risqi Nur Clarita (312210450)

## DAFTAR ISI <br>
| No | Description | Link |
|-----|------|-----|
|1|Latihan|[Click Here](#latihan)|
|2|Praktikum 5|[Click Here](#praktikum-5)|
|3|Flowchart Praktikum 5|[Click Here](#flowchart-praktikum-5)|

## Latihan
Buat sebuah list sebanyak 5 elemen dengan nilai bebas
akses list:
• tampilkan elemen ke 3
• ambil nilai elemen ke 2 sampai elemen ke 4
• ambil elemen terakhir
ubah elemen list:
• ubah elemen ke 4 dengan nilai lainnya
• ubah elemen ke 4 sampai dengan elemen terakhir
tambah elemen list:
• ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
• tambah list B dengan nilai string
• tambah list B dengan 3 nilai
• gabungkan list B dengan list A

### Rumusnya
```python
# Latihan
print("Nama : Anggita Risqi Nur Clarita")
print("NIM  : 312210450")

print("Membuat List sebanyak 5 elemen dengan nilai bebas")
# akses list
a = [20, 40, 50, 60, 100]
print(a) #Menampilkan semua elemen
print(a[2]) #Menampilkan elemen ke 3
print(a[1:3]) #Menampilkan elemen ke 2 sampai dengan ke 4
print(a[4]) #Menampilkan elemen terakhir

print("------------------------------------------")
# ubah elemen list
a[3] = 80 # Mengubah elemen ke 4 dengan nilai lainnya
print(a[3]) # Menampilkan elemen ke 4 yang sudah diubah nilainya
a[3:4] = 80, 90 # Mengubah elemen ke 4 sampai dengan elemen terakhir
print(a[3:5]) # menampilkan elemen ke 4 sampai dengan elemen terakhir

print("------------------------------------------")
# tambah elemen list
b = a[0:2] # Mengambil 2 bagian dari list pertama (a) dan jadikan list kedua (b)
print(b)
b.append(45) # Menambah list dengan nilai string
print(b)
b.extend([85, 90, 95]) # Menambah list b dengan 3 nilai
print(b)
c = a+b # Menggabungkan list b dengan list a
print(c)
```

### Programnya
![image](https://github.com/AnggitaRisqiNC/Praktikum5/blob/main/screenshot/Latihan%201.png)
![image](https://github.com/AnggitaRisqiNC/Praktikum5/blob/main/screenshot/Latihan%201-.png)

### Hasil dari Programnya (RUN)
![image](https://github.com/AnggitaRisqiNC/Praktikum5/blob/main/screenshot/Run%20Latihan%201.png)


## Praktikum 5
Buat program sederhana untuk menambahkan data kedalam sebuah list dengan rincian sebagai berikut:
• Program meminta memasukkan data sebanyak-banyaknya (gunakan perulangan)
• Tampilkan pertanyaan untuk menambah data (ya/tidak?), apabila jawaban "tidak", maka program akan menampilkan daftar datanya.
• Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%)
• Buat flowchart dan penjelasan programnya pada README.md.
• Commit dan push repository ke github.

### Rumusnya
```python
# Membuat Tugas Praktikum
data =[]
while True :
    nama       = input    ("Nama        : ")
    nim        = input    ("NIM         : ")
    tugas      = int(input("Nilai Tugas : "))
    uts        = int(input("Nilai UTS   : "))
    uas        = int(input("Nilai UAS   : "))
    nilaiakhir = float(tugas)*30/100+(uts)*35/100+(uas)*35/100
    data.append([nama,nim,tugas,uts,uas,nilaiakhir])
    lagi= input("Tambah data (ya/tidak)? ")
    if lagi.lower() =="tidak":
        break


print("=====================================================================================");
print("|  No  |     Nama     |     NIM     |   Tugas   |   UTS   |   UAS   |  Nilai Akhir  |");
print("=====================================================================================");
i=0
for x in data:
    i+=1
    print("|  {6:2}  |  {0:10}  |  {1:9}  |  {2:7}  |  {3:5}  | {4:6}  |  {5:11.2f}  |"\
          .format (x[0][:9] , x[1][:9],x[2],x[3],x[4],x[5], i))
print("=====================================================================================");
```

### Programnya
![image](https://github.com/AnggitaRisqiNC/Praktikum5/blob/main/screenshot/Praktikum%205.png)

### Hasil dari Programnya (RUN)
![image](https://github.com/AnggitaRisqiNC/Praktikum5/blob/main/screenshot/Run%20Praktikum%205.png)

### Penjelasan Programnya
1. Buatlah list berupa Nama, NIM, Nilai Tugas, Nilai UTS, Nilai UAS.
2. Lalu inputlah Nama, NIM, Nilai Tugas, Nilai UTS, Nilai UAS.
3. Lalu mencari nilai akhir dengan perhitungan nilai tugas 30%, nilai uts 35% dan uas 35% , dengan perintah float
4. Gunakan perintah append pada Nama, NIM, Nilai tugas, Nilai UTS, Nilai UAS untuk menambahkan 1 item ke elemen terakhir.
5. Jika ingin menambah list data ketik "ya" dan jika tidak ingin menambahkan list data ketik "tidak". Dengan perintah while jawab =="ya" dan if jawab =="tidak". Jawab input("Tambah data (ya/tidak)").
6. Gunakanlah perulangan for, dengan perintah for i in range(len(Nama)):. Fungsi "len" ialah untuk mengembalikan panjang (jumlah anggota) dari suatu objek.
7. Lalu cetak dengan perintah print
8. Selesai

### Flowchart Praktikum 5
![image](https://github.com/AnggitaRisqiNC/Praktikum5/blob/main/screenshot/Flowchart%20Praktikum%205.jpg)

## Finish