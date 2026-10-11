# Program Perkalian Array 3 Dimensi

Program ini meminta pengguna memasukkan beberapa pasangan matriks, mengalikan
setiap pasangan matriks, lalu menampilkan array masukan dan hasilnya. Perkalian
yang dilakukan adalah perkalian matriks standar, bukan perkalian elemen demi
elemen.

## Author

**Nama : Rizky Julfadli**
**NIM : F1G124050**

## Struktur Kode

Semua kode program berada dalam satu file, yaitu [`tugas1.py`](./tugas1.py).
File tersebut terdiri dari fungsi-fungsi berikut:

| Fungsi | Penjelasan |
| --- | --- |
| `isi_array_3d(nama_array, jumlah_matriks)` | Meminta input matriks dari pengguna sebanyak `jumlah_matriks` kali, lalu mengumpulkannya dalam sebuah list. |
| `kalikan_array_3d(array_a, array_b)` | Mengalikan matriks pada indeks yang sama dari `array_a` dan `array_b`, kemudian mengembalikan kumpulan matriks hasil. |
| `tampilkan_layar(judul, data_3d)` | Menampilkan judul dan setiap matriks yang terdapat dalam array 3 dimensi. |
| `main()` | Mengatur alur program: meminta jumlah matriks, membaca array A dan B, menghitung hasil, lalu menampilkan seluruh data. |

Bagian `if __name__ == "__main__":` menjalankan fungsi `main()` saat file
dieksekusi secara langsung.

## Cara Kerja Program

1. Program meminta jumlah pasangan matriks yang akan diproses.
2. Program meminta matriks-matriks untuk array A, lalu array B.
3. Setiap matriks A dikalikan dengan matriks B pada urutan yang sama.
4. Program menampilkan array A, array B, dan hasil perkaliannya.

Perkalian matriks menggunakan tiga perulangan: indeks baris hasil (`i`), indeks
kolom hasil (`j`), dan indeks penjumlahan (`k`). Setiap elemen hasil dihitung
dengan rumus:

```text
hasil[i][j] = jumlah dari A[i][k] * B[k][j]
```

## Cara Menjalankan Program

Pastikan Python 3 sudah terpasang. Buka terminal atau PowerShell di folder
proyek, lalu jalankan:

```powershell
python tugas1.py
```

Jika perintah `python` tidak tersedia, pada Windows Anda dapat mencoba:

```powershell
py tugas1.py
```

Masukkan jumlah matriks, kemudian masukkan setiap matriks sebagai list Python.
Contoh matriks 3 × 3:

```text
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

Contoh sesi input untuk satu pasangan matriks:

```text
Masukkan jumlah matriks yang diinginkan: 1
Masukkan Matriks ke-1: [[1, 2], [3, 4]]
Masukkan Matriks ke-1: [[5, 6], [7, 8]]
```

Matriks-matriks yang dipasangkan harus memiliki ukuran yang sesuai untuk
perkalian matriks: jumlah kolom matriks A harus sama dengan jumlah baris matriks
B. Untuk setiap pasangan, bentuk hasilnya adalah jumlah baris A × jumlah kolom B.

> **Catatan:** Program saat ini menggunakan `eval()` untuk membaca masukan
> matriks. Gunakan hanya masukan yang tepercaya dan berbentuk list angka Python.
