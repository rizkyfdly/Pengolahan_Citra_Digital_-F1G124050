# Deteksi Nomor Ijazah dan Tanda Tangan

## Author

* **Nama:** Rizky Julfadli
* **NIM:** F1G124050
* **Mata Kuliah:** Pengolahan Citra Digital
* **Universitas:** Universitas Halu Oleo

Proyek ini bertujuan untuk memproses gambar ijazah dan melakukan deteksi serta evaluasi terhadap:

- nomor ijazah
- keberadaan tanda tangan pada dokumen
- hasil OCR dengan beberapa teknik enhancement image
- perbandingan hasil preprocessing untuk memilih metode terbaik

Kode utama berada di file `main.py`.

## Deskripsi Program

Program membaca semua file gambar yang berada di folder `citraijazah/`, lalu melakukan pipeline berikut:

1. Mengubah citra menjadi grayscale
2. Menerapkan thresholding global dan Otsu
3. Melakukan operasi morfologi (opening/closing)
4. Menyimpan hasil proses ke folder output sesuai kategori
5. Melakukan OCR pada nomor ijazah menggunakan beberapa teknik enhancement:
   - Contrast Stretching
   - CLAHE
   - Gamma Correction
6. Memilih hasil terbaik berdasarkan nilai CER (Character Error Rate)
7. Mengidentifikasi apakah tanda tangan ada atau tidak pada gambar yang memiliki nama file berawalan `gambar_`

## Struktur Folder

```text
Tugas7CPD/
├── main.py
├── README.md
├── citraijazah/
│   ├── 01_HighQuality.jpg
│   ├── 02_LowContrast.jpg
│   ├── gambar_1.jpg
│   └── ...
├── output/
│   ├── nomor_ijazah/
│   │   ├── 1_citra_asli/
│   │   ├── 2_grayscale/
│   │   ├── 3_global_thresh/
│   │   ├── 4_global_opening/
│   │   ├── 5_global_closing/
│   │   ├── 6_otsu_thresh/
│   │   ├── 7_otsu_opening/
│   │   ├── 8_otsu_closing/
│   │   └── 9_perbandingan/
│   └── ttd/
│       ├── 1_citra_asli/
│       ├── 2_grayscale/
│       ├── 3_global_thresh/
│       ├── 4_global_opening/
│       ├── 5_global_closing/
│       ├── 6_otsu_thresh/
│       ├── 7_otsu_opening/
│       ├── 8_otsu_closing/
│       └── 9_perbandingan/
└── ...
```

## Persyaratan

Sebelum menjalankan program, pastikan perangkat Anda sudah memiliki:

- Python 3.8+
- OpenCV (`opencv-python`)
- NumPy
- Tesseract OCR
- `pytesseract`

## Instalasi

### 1. Clone atau unduh proyek

```bash
git clone <url-repository>
cd Tugas7CPD
```

### 2. Buat environment virtual (opsional, tetapi disarankan)

```bash
python -m venv venv
```

Pada Windows:

```bash
venv\Scripts\activate
```

Pada Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Install dependency

```bash
pip install opencv-python numpy pytesseract
```

### 4. Instal Tesseract OCR

Karena program menggunakan `pytesseract`, Tesseract OCR harus terinstal pada sistem operasi.

#### Windows

- Unduh installer Tesseract dari situs resmi atau package manager yang tersedia.
- Pastikan path Tesseract terdeteksi otomatis.
- Jika tidak terdeteksi, sesuaikan konfigurasi path di file `main.py`:

```python
TESSERACT_PATHS = [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
]
```

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install tesseract-ocr
```

## Menjalankan Program

Pastikan folder `citraijazah/` sudah berisi file gambar yang akan diproses.

Kemudian jalankan:

```bash
python main.py
```

Program akan otomatis:

- membaca semua file gambar dari `citraijazah/`
- memproses citra
- menyimpan hasil preprocessing ke `output/`
- menampilkan tabel hasil OCR di terminal

## Konvensi Nama File

Program membedakan jenis gambar berdasarkan nama file:

- `0...` atau file yang diawali dengan angka, misalnya `01_HighQuality.jpg` → diproses sebagai gambar nomor ijazah
- `gambar_...` → diproses sebagai gambar tanda tangan

Contoh:

```text
01_HighQuality.jpg
02_LowContrast.jpg
gambar_1.jpg
gambar_2.jpg
```

## Output yang Dihasilkan

### 1. Folder nomor ijazah

Semua hasil preprocessing nomor ijazah disimpan di:

```text
output/nomor_ijazah/
```

Subfolder yang dihasilkan:

- `1_citra_asli`
- `2_grayscale`
- `3_global_thresh`
- `4_global_opening`
- `5_global_closing`
- `6_otsu_thresh`
- `7_otsu_opening`
- `8_otsu_closing`
- `9_perbandingan`

### 2. Folder tanda tangan

Semua hasil preprocessing tanda tangan disimpan di:

```text
output/ttd/
```

Pada folder ini, program juga mengecek apakah tanda tangan hadir dengan threshold Otsu.

## Hasil Terminal

Setelah program selesai, hasil akan ditampilkan dalam bentuk tabel terminal seperti berikut:

```text
Nama gambar                               Hasil OCR             CER         Enhancement terbaik      Tanda tangan
==============================================================================================================================
01_HighQuality.jpg                        571012022000056      0.00%       CLAHE                    ABSENT
gambar_1.jpg                              -                    -           -                        PRESENT
```

## Catatan Penting

- Nilai `GROUND_TRUTH` saat ini sudah diatur secara default di dalam file `main.py`.
- Program bekerja paling baik jika citra ijazah memiliki kualitas yang cukup jelas.
- Jika hasil OCR tidak akurat, periksa kualitas gambar, ukuran teks, dan kontras citra.
- Pastikan Tesseract sudah terpasang dengan benar agar `pytesseract` bisa berjalan.

## Troubleshooting

### Error: `pytesseract` tidak ditemukan

```bash
pip install pytesseract
```

### Error: Tesseract tidak terdeteksi

- Periksa apakah Tesseract sudah terinstall
- Cek lokasi `tesseract.exe`
- Ubah path di file `main.py` sesuai lokasi instalasi

### Folder `citraijazah` kosong

Pastikan Anda menaruh file gambar di folder berikut:

```text
citraijazah/
```

### Tidak ada output yang dihasilkan

Pastikan file gambar memiliki format yang didukung, seperti:

- `.jpg`
- `.jpeg`
- `.png`

## Kesimpulan

Program ini berfungsi untuk melakukan preprocessing, OCR, evaluasi nomor ijazah, serta deteksi keberadaan tanda tangan dari citra dokumen. Dengan menjalankan `python main.py`, semua proses akan otomatis berjalan dan hasilnya dapat dilihat melalui terminal serta output yang disimpan di folder `output/`.
