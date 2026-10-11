# OCR dan Perbandingan Filter Citra

Program `ocr.py` menerapkan beberapa metode pengolahan citra pada gambar ijazah, menjalankan OCR pada gambar asli dan hasil pengolahan, lalu membandingkan hasil pembacaan teksnya. Hasil pemrosesan gambar, visualisasi perbandingan, dan rekapitulasi OCR disimpan di folder `hasil`.

## Author

- **Nama:** Rizky Julfadli
- **NIM:** F1G124050

## Struktur Folder

```text
Tugas5CPD/
├── ocr.py
├── CitraIjazah/                 # Gambar masukan (.jpg, .jpeg, .png, atau .bmp)
└── hasil/
    ├── mean_filter/             # Gambar hasil mean filter
    ├── median_filter/           # Gambar hasil median filter
    ├── gaussian_filter/         # Gambar hasil Gaussian filter
    ├── sharpening/              # Gambar hasil sharpening
    ├── perbandingan/            # Visualisasi gambar asli dan hasil pemrosesan
    └── laporan/
        └── rekapitulasi_ocr.csv # Rekap teks OCR dan akurasi
```

Folder-folder di dalam `hasil` dibuat otomatis saat program dijalankan. Folder `CitraIjazah` harus tersedia dan berisi gambar yang akan diproses.

## Penjelasan Program

Program menggunakan OpenCV untuk membaca dan mengolah citra, NumPy untuk membuat kernel sharpening, Matplotlib untuk membuat visualisasi, `pytesseract` sebagai penghubung ke mesin Tesseract OCR, serta modul `csv` dan `pathlib` untuk menyimpan laporan dan mengelola path.

Tahapan utama program:

1. Mengatur lokasi executable Tesseract dan konfigurasi OCR (`--oem 3 --psm 6`).
2. Menyiapkan folder keluaran dan mencari gambar dengan ekstensi JPG, JPEG, PNG, atau BMP di `CitraIjazah`.
3. Membaca setiap gambar, lalu mengubahnya menjadi citra grayscale untuk pengolahan dan OCR. Versi asli berwarna dipertahankan untuk visualisasi.
4. Membuat empat varian citra:
   - **Mean filter:** merata-ratakan piksel dalam kernel 3×3 untuk menghaluskan citra.
   - **Median filter:** mengganti piksel dengan nilai median tetangganya menggunakan kernel 3×3, yang dapat membantu mengurangi noise.
   - **Gaussian filter:** menghaluskan citra dengan Gaussian blur berukuran 3×3.
   - **Sharpening:** mempertajam detail menggunakan kernel konvolusi.
5. Menjalankan OCR pada gambar asli grayscale dan keempat hasil pengolahan. Teks OCR dirapikan dengan mengganti baris baru menjadi spasi.
6. Membandingkan teks OCR dengan ground truth menggunakan jarak Levenshtein tanpa memperhitungkan spasi. Nilai karakter benar dihitung dari panjang teks acuan dikurangi jarak tersebut, dengan nilai minimum nol; akurasi dihitung sebagai persentase karakter benar dari panjang teks acuan.
7. Menampilkan hasil dan akurasi di terminal, menyimpan gambar hasil filter, membuat satu gambar visualisasi perbandingan untuk setiap input, dan menulis seluruh hasil ke CSV.

`GROUND_TRUTH` di dalam `ocr.py` saat ini berupa dictionary kosong. Jika ingin evaluasi berdasarkan teks acuan yang ditentukan, isi dictionary tersebut dengan nama file tanpa ekstensi sebagai key dan teks acuan sebagai value. Jika teks acuan untuk sebuah gambar tidak tersedia, program menggunakan hasil OCR dari sharpening atau gambar asli—mana yang teksnya lebih panjang—sebagai acuan sementara.

## Persiapan

1. Pasang Python 3.
2. Pasang dependensi Python:

   ```powershell
   py -m pip install opencv-python numpy matplotlib pytesseract
   ```

3. Pasang aplikasi **Tesseract OCR** di Windows. Program saat ini mengharapkan executable pada:

   ```text
   C:\Program Files\Tesseract-OCR\tesseract.exe
   ```

   Jika Tesseract terpasang di lokasi lain, sesuaikan nilai `pytesseract.pytesseract.tesseract_cmd` di bagian konfigurasi `ocr.py`.
4. Letakkan gambar masukan di folder `CitraIjazah`.

## Cara Menjalankan

Buka PowerShell di folder proyek, kemudian jalankan:

```powershell
py ocr.py
```

Pastikan folder kerja saat menjalankan perintah adalah folder proyek, karena lokasi input dan output pada program menggunakan path relatif. Setelah proses selesai, rekap OCR tersedia di `hasil/laporan/rekapitulasi_ocr.csv`, sedangkan gambar dan visualisasi tersimpan di subfolder `hasil` masing-masing.

Jika folder `CitraIjazah` tidak berisi gambar dengan ekstensi yang didukung, program menampilkan pesan bahwa gambar tidak ditemukan dan berhenti.
