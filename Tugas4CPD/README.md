# Enhancement Citra dan Pengujian OCR Nomor Ijazah

Program ini membandingkan beberapa metode peningkatan kualitas citra grayscale untuk gambar nomor ijazah, menampilkan distribusi intensitas pikselnya, dan membandingkan teks yang dibaca oleh OCR.

## Author

- **Nama:** Rizky Julfadli
- **NIM:** F1G124050

## Struktur Folder

```text
Tugas4CPD/
├── CitraIjazah/                     # Gambar masukan (hasil crop)
├── hasil/
│   ├── brightness/                  # Hasil brightness adjustment
│   ├── contrast_stretching/         # Hasil contrast stretching
│   ├── histogram_equalization/      # Hasil histogram equalization
│   ├── perbandingan/                # Gambar perbandingan hasil enhancement
│   └── histogram/                  # Grafik histogram
├── enhancement.py                   # Enhancement dan perbandingan citra
├── grafik.py                        # Pembuatan grafik histogram
├── tes_ocr.py                       # Pengujian pembacaan teks OCR
└── README.md
```

> Nama file pada folder ini adalah `enhancement.py` (bukan `enhacement.py`).

Gambar masukan yang didukung adalah `.jpg`, `.jpeg`, `.png`, dan `.bmp`. Letakkan gambar yang sudah di-crop ke folder `CitraIjazah/`.

## Penjelasan Program

### `enhancement.py`

Program utama untuk memproses gambar:

1. Membaca gambar dari folder `CitraIjazah/` dan mengubahnya menjadi grayscale.
2. Menghasilkan tiga versi citra:
   - **Brightness adjustment:** menambah nilai kecerahan dengan parameter `BRIGHTNESS_VALUE` (nilai bawaan `20`).
   - **Contrast stretching:** memetakan rentang intensitas minimum–maksimum citra ke rentang 0–255.
   - **Histogram equalization:** meratakan distribusi intensitas menggunakan `cv2.equalizeHist`.
3. Menyimpan hasil tiap metode sebagai file JPG ke subfolder masing-masing di `hasil/`.
4. Menyimpan gambar perbandingan empat panel (citra asli dan tiga hasil enhancement) sebagai PNG di `hasil/perbandingan/`.
5. Menampilkan statistik mean dan standar deviasi intensitas untuk citra asli dan hasil brightness.

Folder keluaran dibuat otomatis jika belum ada. Jika folder `CitraIjazah/` tidak berisi gambar yang didukung, program menampilkan pesan dan berhenti.

### `grafik.py`

Membaca citra asli dan hasil enhancement yang dibuat oleh `enhancement.py`, lalu membuat satu grafik berisi histogram citra asli, brightness, contrast stretching, dan histogram equalization. Sumbu horizontal menunjukkan intensitas piksel (0–255), sedangkan sumbu vertikal menunjukkan jumlah piksel. Grafik disimpan sebagai PNG di `hasil/histogram/`.

Jalankan `enhancement.py` terlebih dahulu agar file hasil yang dibutuhkan tersedia.

### `tes_ocr.py`

Menggunakan OpenCV untuk membaca citra grayscale dan `pytesseract` untuk mengekstrak teks dari citra asli dan ketiga hasil enhancement. Teks yang terbaca ditampilkan di terminal untuk setiap gambar.

Skrip ini membandingkan hasil teks OCR secara berdampingan; skrip **tidak menghitung skor akurasi numerik**. Jalankan `enhancement.py` terlebih dahulu agar semua citra hasil enhancement tersedia.

## Persiapan

Gunakan Python 3 dan pasang pustaka Python yang diperlukan:

```powershell
python -m pip install opencv-python numpy matplotlib pytesseract
```

`tes_ocr.py` juga memerlukan aplikasi **Tesseract OCR** yang terpasang di Windows. Kode saat ini menunjuk ke lokasi:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

Jika Tesseract terpasang di lokasi lain, sesuaikan nilai `pytesseract.pytesseract.tesseract_cmd` di `tes_ocr.py` dengan lokasi `tesseract.exe` pada komputer Anda.

Pastikan gambar masukan sudah tersedia di `CitraIjazah/`, kemudian jalankan perintah dari direktori proyek (folder yang berisi file-file Python tersebut).

## Cara Menjalankan

Jalankan setiap skrip dari direktori proyek menggunakan PowerShell:

```powershell
python enhancement.py
python grafik.py
python tes_ocr.py
```

Urutan yang disarankan:

1. Jalankan `enhancement.py` untuk menghasilkan citra enhancement dan gambar perbandingan.
2. Jalankan `grafik.py` untuk menghasilkan grafik histogram.
3. Jalankan `tes_ocr.py` untuk melihat teks yang dikenali dari gambar asli dan setiap hasil enhancement.

Hasil disimpan di dalam folder `hasil/`, sedangkan hasil OCR ditampilkan di terminal.
