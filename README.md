# PENGOLAHAN CITRA DIGITAL

Kumpulan program Python untuk tugas dan eksperimen mata kuliah Pengolahan Citra
Digital. Setiap folder berisi program yang berbeda; jalankan program dari folder
tugas masing-masing agar path masukan dan keluaran relatif dapat ditemukan.

## Author

- **Nama:** Rizky Julfadli
- **NIM:** F1G124050

## Daftar Isi

- [Tugas1CPD - Perkalian Array 3 Dimensi](#tugas1cpd---perkalian-array-3-dimensi)
- [Tugas3CPD - Grayscale dan Histogram](#tugas3cpd---grayscale-dan-histogram)
- [Tugas4CPD - Enhancement dan OCR](#tugas4cpd---enhancement-dan-ocr)
- [Tugas5CPD - Filtering dan OCR](#tugas5cpd---filtering-dan-ocr)
- [Tugas6CPD - Deteksi Tanda Tangan](#tugas6cpd---deteksi-tanda-tangan)
- [Tugas7CPD - OCR Nomor Ijazah dan Deteksi Tanda Tangan](#tugas7cpd---ocr-nomor-ijazah-dan-deteksi-tanda-tangan)
- [Dependensi dan konfigurasi OCR](#dependensi-dan-konfigurasi-ocr)

## Tugas1CPD - Perkalian Array 3 Dimensi

**Berkas utama:** `Tugas1CPD/tugas1.py`

Program terminal ini meminta sejumlah pasangan matriks, menyimpan matriks
tersebut sebagai kumpulan (array) 3 dimensi, lalu mengalikan setiap pasangan
menggunakan perkalian matriks standar. Fungsi `isi_array_3d` menerima matriks,
`kalikan_array_3d` menghitung hasil, dan `tampilkan_layar` menampilkan input
serta hasil perkalian.

Masukkan matriks sebagai list Python. Untuk perkalian yang valid, jumlah kolom
matriks A harus sama dengan jumlah baris matriks B. Program ini merupakan
latihan operasi array/matriks dan tidak memproses citra.

Jalankan dari folder proyek:

```powershell
cd Tugas1CPD
py tugas1.py
```

## Tugas3CPD - Grayscale dan Histogram

**Berkas program:** `Tugas3CPD/grayscale.py` dan `Tugas3CPD/histogram.py`

Kedua skrip memproses sembilan citra bernama `rgb1.jpeg` sampai `rgb9.jpeg`,
yang harus berada di folder `Tugas3CPD` bersama skrip.

- **`grayscale.py`** membaca citra dengan OpenCV, mengubah BGR menjadi grayscale,
  menyimpan `hasil/grayscale1.jpg` sampai `hasil/grayscale9.jpg`, dan
  menampilkan pratinjau setiap hasil. Jika citra tidak tersedia atau gagal
  dibaca, program mencetak pesan dan melanjutkan ke citra berikutnya.
- **`histogram.py`** membuat histogram kanal merah, hijau, dan biru citra asli,
  serta histogram intensitas citra grayscale. Setiap grafik menggunakan 256
  bin dengan rentang intensitas 0–255 dan disimpan sebagai
  `hasil/histogram/histogram1.png` sampai `histogram9.png`.

Folder hasil dibuat otomatis. Jalankan skrip dari folder `Tugas3CPD`:

```powershell
cd Tugas3CPD
py grayscale.py
py histogram.py
```

## Tugas4CPD - Enhancement dan OCR

**Berkas program:** `Tugas4CPD/enhancement.py`, `Tugas4CPD/grafik.py`, dan
`Tugas4CPD/tes_ocr.py`

Letakkan citra yang akan diolah (JPG, JPEG, PNG, atau BMP) di
`Tugas4CPD/CitraIjazah`. Program mengasumsikan citra di folder tersebut sudah
di-crop ke area yang ingin dianalisis.

- **`enhancement.py`** mengubah setiap citra menjadi grayscale, lalu
  membandingkan tiga metode: penambahan kecerahan (nilai bawaan `20`),
  contrast stretching, dan histogram equalization. Hasil setiap metode
  disimpan di `hasil/brightness`, `hasil/contrast_stretching`, dan
  `hasil/histogram_equalization`. Gambar perbandingan empat panel disimpan di
  `hasil/perbandingan`. Program juga menampilkan statistik mean dan standar
  deviasi intensitas.
- **`grafik.py`** membuat histogram citra asli dan hasil dari ketiga metode
  enhancement. Jalankan setelah `enhancement.py`, karena skrip ini membaca
  berkas hasil yang dibuat oleh program tersebut. Grafik disimpan di
  `hasil/histogram`.
- **`tes_ocr.py`** menjalankan Tesseract OCR pada citra asli dan pada hasil
  brightness, contrast stretching, serta histogram equalization, kemudian
  menampilkan teks yang dikenali di terminal untuk dibandingkan. Skrip ini
  juga memerlukan hasil dari `enhancement.py`.

Urutan penggunaan yang disarankan:

```powershell
cd Tugas4CPD
py enhancement.py
py grafik.py
py tes_ocr.py
```

## Tugas5CPD - Filtering dan OCR

**Berkas utama:** `Tugas5CPD/ocr.py`

Letakkan citra masukan JPG, JPEG, PNG, atau BMP di `Tugas5CPD/CitraIjazah`.
Program mengubah citra menjadi grayscale untuk pemrosesan, lalu menerapkan:

- **Mean filter** untuk merata-ratakan nilai piksel di sekitar setiap piksel.
- **Median filter** untuk mengurangi noise dengan nilai median tetangga.
- **Gaussian filter** untuk penghalusan berbobot Gaussian.
- **Sharpening** dengan kernel konvolusi untuk menegaskan detail.

Tesseract OCR dijalankan pada citra asli grayscale dan keempat hasil tersebut.
Teks OCR ditampilkan di terminal dan dibandingkan menggunakan jarak
Levenshtein, tanpa menghitung spasi. Bila `GROUND_TRUTH` belum diisi untuk
suatu citra, program memakai teks terpanjang dari hasil OCR asli atau
sharpening sebagai acuan sementara; nilai akurasi tersebut bukan evaluasi
terhadap ground truth eksternal.

Gambar hasil filter disimpan di subfolder `hasil/mean_filter`,
`hasil/median_filter`, `hasil/gaussian_filter`, dan `hasil/sharpening`.
Visualisasi perbandingan berada di `hasil/perbandingan`, sementara rekap teks
dan akurasi ditulis ke `hasil/laporan/rekapitulasi_ocr.csv`.

Jalankan dari folder tugas:

```powershell
cd Tugas5CPD
py ocr.py
```

## Tugas6CPD - Deteksi Tanda Tangan

**Berkas utama:** `Tugas6CPD/main.py`

Letakkan citra tanda tangan atau dokumen yang akan dianalisis di
`Tugas6CPD/citraTTD`. Program memproses citra dengan dua jalur segmentasi:

1. Citra diubah menjadi grayscale.
2. Jalur pertama menggunakan inverse global threshold dengan nilai ambang 127;
   jalur kedua menggunakan inverse Otsu threshold untuk menentukan ambang
   secara otomatis.
3. Kedua jalur menjalankan operasi morfologi opening lalu closing dengan
   kernel persegi 3×3.
4. Program menghitung jumlah dan rasio piksel foreground. Keputusan
   `SIGNATURE PRESENT` atau `SIGNATURE ABSENT` menggunakan rasio hasil Otsu
   dengan batas bawaan 2%, disertai pemeriksaan tambahan pada hasil global
   threshold dan nilai ambang Otsu.

Hasil citra asli, grayscale, threshold, operasi morfologi, serta visualisasi
perbandingan disimpan pada subfolder `hasil/1_citra_asli` sampai
`hasil/9_perbandingan`. Rekap nilai ambang, piksel foreground, rasio, dan
status ditampilkan di terminal.

```powershell
cd Tugas6CPD
py main.py
```

## Tugas7CPD - OCR Nomor Ijazah dan Deteksi Tanda Tangan

**Berkas utama:** `Tugas7CPD/main.py`

Program membaca citra JPG, JPEG, dan PNG dari `Tugas7CPD/citraijazah`. Nama
berkas menentukan kategori pemrosesan: berkas yang diawali `0` diperlakukan
sebagai citra nomor ijazah, sedangkan berkas yang diawali `gambar_` diproses
sebagai citra tanda tangan.

Untuk setiap citra, program menyimpan citra asli, grayscale, hasil global
threshold, hasil Otsu threshold, operasi opening dan closing, serta grid
perbandingan di folder `output/nomor_ijazah` atau `output/ttd` sesuai
kategorinya. Untuk OCR nomor ijazah, program membandingkan contrast stretching,
CLAHE, dan gamma correction, menerapkan Otsu threshold pada hasil enhancement,
lalu menjalankan Tesseract untuk mengenali nomor. Nomor hasil OCR dievaluasi
terhadap nilai `GROUND_TRUTH` yang ditetapkan di kode menggunakan Character
Error Rate (CER); metode dengan CER terendah dipilih dan direkap di terminal.
Untuk citra bertanda nama `gambar_`, program menentukan status tanda tangan
dari jumlah piksel foreground pada hasil inverse Otsu threshold.

Contoh konvensi nama berkas:

```text
01_HighQuality.jpg
02_LowContrast.jpg
gambar_1.jpg
gambar_2.jpg
```

Jalankan dari folder tugas:

```powershell
cd Tugas7CPD
py main.py
```

## Dependensi dan konfigurasi OCR

Program pengolahan citra menggunakan Python 3. Paket yang diperlukan bergantung
pada tugas:

- Tugas1: tidak memerlukan paket tambahan di luar Python.
- Tugas3: `opencv-python` dan `matplotlib`.
- Tugas4: `opencv-python`, `numpy`, `matplotlib`, dan `pytesseract`.
- Tugas5: `opencv-python`, `numpy`, `matplotlib`, dan `pytesseract`.
- Tugas6: `opencv-python`, `numpy`, dan `matplotlib`.
- Tugas7: `opencv-python`, `numpy`, dan `pytesseract`.

Contoh memasang seluruh paket Python yang digunakan:

```powershell
py -m pip install opencv-python numpy matplotlib pytesseract
```

Tugas4, Tugas5, dan Tugas7 juga memerlukan aplikasi **Tesseract OCR** terpasang
di sistem. Tugas4 dan Tugas5 mengatur path executable langsung ke
`C:\Program Files\Tesseract-OCR\tesseract.exe`. Tugas7 mencoba mendeteksi
Tesseract pada folder `Program Files` dan `Program Files (x86)`. Jika
Tesseract dipasang di lokasi lain, sesuaikan konfigurasi path di skrip terkait.
