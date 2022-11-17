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