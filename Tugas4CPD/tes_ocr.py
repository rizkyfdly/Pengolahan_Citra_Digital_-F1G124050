import cv2
import pytesseract
from pathlib import Path

# ==========================================================
# KONFIGURASI TESSERACT OCR
# ==========================================================
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Konfigurasi mode OCR (OEM 3 = Default Engine, PSM 6 = Menganggap gambar sebagai 1 baris teks)
CUSTOM_CONFIG = r'--oem 3 --psm 6'


# ==========================================================
# KONFIGURASI FOLDER
# ==========================================================
folder_asli = Path("CitraIjazah")
folder_brightness = Path("hasil/brightness")
folder_contrast = Path("hasil/contrast_stretching")
folder_equalization = Path("hasil/histogram_equalization")


# ==========================================================
# FUNGSI BACA TEKS DENGAN OCR
# ==========================================================
def baca_ocr(path_gambar):
    gambar = cv2.imread(str(path_gambar), cv2.IMREAD_GRAYSCALE)
    if gambar is None:
        return "Gagal Membaca Gambar"
    
    # Ekstraksi teks menggunakan pytesseract
    teks = pytesseract.image_to_string(gambar, config=CUSTOM_CONFIG)
    return teks.strip()


# ==========================================================
# MENCARI GAMBAR ASLI
# ==========================================================
daftar_gambar = sorted(
    list(folder_asli.glob("*.jpg")) + 
    list(folder_asli.glob("*.jpeg")) + 
    list(folder_asli.glob("*.png")) + 
    list(folder_asli.glob("*.bmp"))
)

if not daftar_gambar:
    print("Tidak ditemukan gambar di folder CitraIjazah.")
    exit()


# ==========================================================
# PENGUJAN OCR PADA TIAP METODE
# ==========================================================
print("=" * 85)
print("PENGUJIAN AKURASI OCR PADA HASIL ENHANCEMENT")
print("=" * 85)

for file_asli in daftar_gambar:
    nama = file_asli.stem
    
    # Path masing-masing gambar hasil enhancement
    file_brightness = folder_brightness / f"{nama}_brightness.jpg"
    file_contrast = folder_contrast / f"{nama}_contrast.jpg"
    file_equalization = folder_equalization / f"{nama}_equalization.jpg"
    
    # Ekstraksi Teks
    teks_asli = baca_ocr(file_asli)
    teks_brightness = baca_ocr(file_brightness)
    teks_contrast = baca_ocr(file_contrast)
    teks_equalization = baca_ocr(file_equalization)
    
    # Tampilkan Hasil
    print(f"\n[Gambar: {file_asli.name}]")
    print("-" * 85)
    print(f"1. Gambar Asli          : '{teks_asli}'")
    print(f"2. Brightness           : '{teks_brightness}'")
    print(f"3. Contrast Stretching  : '{teks_contrast}'")
    print(f"4. Histogram Eq.        : '{teks_equalization}'")
    print("-" * 85)

print("\n" + "=" * 85)
print("PENGUJIAN SELESAI")
print("=" * 85)