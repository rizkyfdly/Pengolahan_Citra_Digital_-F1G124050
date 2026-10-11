# Pengolahan Citra: Grayscale dan Histogram

Program ini berisi dua skrip Python untuk mengolah sembilan citra masukan: mengubah citra menjadi grayscale dan membuat histogram intensitas warna.

## Struktur folder

```text
Tugas3CPD/
├── grayscale.py
├── histogram.py
├── rgb1.jpeg
├── rgb2.jpeg
├── ...
├── rgb9.jpeg
└── hasil/                  # Dibuat otomatis saat program dijalankan
    ├── grayscale1.jpg
    ├── ...
    ├── grayscale9.jpg
    └── histogram/
        ├── histogram1.png
        ├── ...
        └── histogram9.png
```

Letakkan semua citra masukan (`rgb1.jpeg` hingga `rgb9.jpeg`) di folder yang sama dengan kedua skrip. Nama berkas harus sesuai agar dapat ditemukan oleh program.

## Penjelasan kode

### `grayscale.py`

1. Mengimpor OpenCV untuk membaca dan mengolah citra, `os` untuk membuat folder keluaran, dan Matplotlib untuk menampilkan citra.
2. Membuat folder `hasil` jika belum tersedia.
3. Mengulang nomor 1 sampai 9 dan membaca berkas `rgb{i}.jpeg`.
4. Jika citra gagal dibaca atau tidak ditemukan, program mencetak pesan dan melanjutkan ke citra berikutnya.
5. Mengubah citra dari format BGR yang digunakan OpenCV ke grayscale dengan `cv2.cvtColor`.
6. Menyimpan hasil sebagai `hasil/grayscale{i}.jpg`, menampilkan pratinjau grayscale, dan mencetak nama berkas hasil.

### `histogram.py`

1. Mengimpor OpenCV, Matplotlib, dan `os`, kemudian membuat folder `hasil/histogram` jika belum tersedia.
2. Membaca citra `rgb{i}.jpeg` untuk nomor 1 sampai 9. Citra yang tidak dapat dibaca dilewati dengan pesan.
3. Mengubah citra BGR menjadi RGB untuk mendapatkan kanal warna dengan urutan yang benar, serta membuat versi grayscale.
4. Membuat dua grafik dalam satu gambar:
   - Histogram kanal merah, hijau, dan biru dari citra asli.
   - Histogram intensitas dari citra grayscale.
5. Histogram menggunakan 256 bin pada rentang intensitas 0–255. Grafik disimpan sebagai `hasil/histogram/histogram{i}.png`, lalu ditutup agar tidak menumpuk selama pemrosesan.
6. Setelah seluruh citra diproses, program mencetak pesan bahwa proses histogram selesai.

## Persiapan

Pastikan Python sudah terpasang. Dari terminal atau PowerShell, pindah ke folder proyek, lalu pasang dependensi:

```powershell
py -m pip install opencv-python matplotlib
```

## Menjalankan program

Jalankan perintah berikut dari folder proyek, tempat skrip dan berkas `rgb1.jpeg` hingga `rgb9.jpeg` berada:

```powershell
py grayscale.py
```

Skrip grayscale menampilkan hasil setiap citra. Tutup jendela gambar yang sedang ditampilkan untuk melanjutkan ke citra berikutnya.

Untuk membuat histogram, jalankan:

```powershell
py histogram.py
```

Hasil grayscale berada di folder `hasil`. Berkas gambar histogram berada di `hasil/histogram`. Folder keluaran akan dibuat otomatis jika belum ada.

## Author

**Nama: Rizky Julfadli**
**NIM: F1G124050**