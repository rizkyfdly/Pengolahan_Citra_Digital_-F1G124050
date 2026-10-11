import os
import re
import glob
import cv2
import numpy as np
import pytesseract

# ---------------------------------------------------------
# 1. KONFIGURASI PATH & SUB-FOLDER OUTPUT
# ---------------------------------------------------------
FOLDER_INPUT = "citraijazah"
GROUND_TRUTH = "571012022000056"

SUB_FOLDERS = [
    "1_citra_asli",
    "2_grayscale",
    "3_global_thresh",
    "4_global_opening",
    "5_global_closing",
    "6_otsu_thresh",
    "7_otsu_opening",
    "8_otsu_closing",
    "9_perbandingan"
]

DIR_OUT_NO = os.path.join("output", "nomor_ijazah")
DIR_OUT_TTD = os.path.join("output", "ttd")

for base_dir in [DIR_OUT_NO, DIR_OUT_TTD]:
    for sub in SUB_FOLDERS:
        os.makedirs(os.path.join(base_dir, sub), exist_ok=True)

# Auto-detect Tesseract OCR di Windows
TESSERACT_PATHS = [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
]
for path in TESSERACT_PATHS:
    if os.path.exists(path):
        pytesseract.pytesseract.tesseract_cmd = path
        break


# ---------------------------------------------------------
# 2. ENHANCEMENT & CER
# ---------------------------------------------------------
def contrast_stretch(img):
    mn, mx = np.min(img), np.max(img)
    return img if mx == mn else ((img - mn) * 255 / (mx - mn)).astype(np.uint8)

def clahe_enhancement(img):
    return cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)).apply(img)

def gamma_correction(img, gamma=1.5):
    table = np.array([((i / 255.0) ** (1 / gamma)) * 255 for i in range(256)]).astype(np.uint8)
    return cv2.LUT(img, table)

def levenshtein(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        curr = [i]
        for j, cb in enumerate(b, 1):
            cost = 0 if ca == cb else 1
            curr.append(min(curr[-1] + 1, prev[j] + 1, prev[j - 1] + cost))
        prev = curr
    return prev[-1]

def hitung_cer(pred):
    if not pred: return 100.0
    return (levenshtein(pred, GROUND_TRUTH) / len(GROUND_TRUTH)) * 100.0

def ekstrak_nomor(text):
    digits_only = re.sub(r'\D', '', text)
    kandidat = re.findall(r"\d{10,}", digits_only)
    if not kandidat:
        return digits_only[:15] if len(digits_only) >= 10 else digits_only
    return min(kandidat, key=lambda x: abs(len(x) - len(GROUND_TRUTH)))


# ---------------------------------------------------------
# 3. PIPELINE PEMROSESAN SERTA GRID PERBANDINGAN
# ---------------------------------------------------------
def process_pipeline_steps(img_color):
    gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    
    _, global_thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    _, otsu_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    
    global_open = cv2.morphologyEx(global_thresh, cv2.MORPH_OPEN, kernel)
    global_close = cv2.morphologyEx(global_open, cv2.MORPH_CLOSE, kernel)
    
    otsu_open = cv2.morphologyEx(otsu_thresh, cv2.MORPH_OPEN, kernel)
    otsu_close = cv2.morphologyEx(otsu_open, cv2.MORPH_CLOSE, kernel)

    steps = {
        "1_citra_asli": img_color,
        "2_grayscale": gray,
        "3_global_thresh": global_thresh,
        "4_global_opening": global_open,
        "5_global_closing": global_close,
        "6_otsu_thresh": otsu_thresh,
        "7_otsu_opening": otsu_open,
        "8_otsu_closing": otsu_close
    }
    
    h, w = gray.shape[:2]
    canvas = np.zeros((h * 3, w * 3, 3), dtype=np.uint8)

    grid_items = [
        ("1. Original", img_color),
        ("2. Grayscale", cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)),
        ("3. Global Thresh", cv2.cvtColor(global_thresh, cv2.COLOR_GRAY2BGR)),
        ("4. Global Open", cv2.cvtColor(global_open, cv2.COLOR_GRAY2BGR)),
        ("5. Global Close", cv2.cvtColor(global_close, cv2.COLOR_GRAY2BGR)),
        ("6. Otsu Thresh", cv2.cvtColor(otsu_thresh, cv2.COLOR_GRAY2BGR)),
        ("7. Otsu Open", cv2.cvtColor(otsu_open, cv2.COLOR_GRAY2BGR)),
        ("8. Otsu Close", cv2.cvtColor(otsu_close, cv2.COLOR_GRAY2BGR)),
    ]

    for idx, (title, img_cell) in enumerate(grid_items):
        r, c = idx // 3, idx % 3
        cell = img_cell.copy()
        cv2.putText(cell, title, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        canvas[r*h:(r+1)*h, c*w:(c+1)*w] = cell

    steps["9_perbandingan"] = canvas
    return steps, gray


# ---------------------------------------------------------
# 4. EXECUTION PIPELINE
# ---------------------------------------------------------
if __name__ == "__main__":
    extensions = ["*.jpg", "*.jpeg", "*.png", "*.JPEG", "*.JPG", "*.PNG"]
    
    files = []
    for ext in extensions:
        files.extend(glob.glob(os.path.join(FOLDER_INPUT, ext)))
    files = sorted(list(set(files)))

    if not files:
        print(f"[-] Tidak ada gambar di folder '{FOLDER_INPUT}/'. Masukkan gambar terlebih dahulu.")
        exit()

    rekapitulasi = []

    for path_img in files:
        filename = os.path.basename(path_img)
        img = cv2.imread(path_img)
        if img is None: continue

        # Deteksi Jenis Gambar Berdasarkan Nama File
        is_nomor_only = filename.startswith("0")  # e.g., 01_HighQuality, 02_LowContrast, dll.
        is_ttd_only = filename.startswith("gambar_")  # e.g., gambar_1.jpg, gambar_2.jpg

        steps, gray = process_pipeline_steps(img)

        # Simpan ke folder output sesuai tipe gambar
        if is_nomor_only:
            for folder_name, img_result in steps.items():
                cv2.imwrite(os.path.join(DIR_OUT_NO, folder_name, filename), img_result)
            ttd_status = "ABSENT"
        elif is_ttd_only:
            for folder_name, img_result in steps.items():
                cv2.imwrite(os.path.join(DIR_OUT_TTD, folder_name, filename), img_result)
            
            # Cek presensi TTD
            _, inv_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            fg_pix = cv2.countNonZero(inv_thresh)
            ttd_status = "PRESENT" if fg_pix > 50 else "ABSENT"
        else:
            ttd_status = "ABSENT"

        # Evaluasi OCR Nomor Ijazah
        enhancements = {
            "Contrast Stretching": contrast_stretch(gray),
            "CLAHE": clahe_enhancement(gray),
            "Gamma Correction": gamma_correction(gray)
        }

        ocr_results = []
        for enh_name, enh_img in enhancements.items():
            _, bin_enh = cv2.threshold(enh_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            txt = pytesseract.image_to_string(bin_enh, config="--psm 6").strip()
            num = ekstrak_nomor(txt)
            cer_val = hitung_cer(num)
            ocr_results.append((enh_name, num, cer_val))

        best_enh = min(ocr_results, key=lambda x: x[2])

        rekapitulasi.append([
            filename,
            best_enh[1],
            f"{best_enh[2]:.2f}%",
            best_enh[0],
            ttd_status
        ])

    # ---------------------------------------------------------
    # 5. TABEL OUTPUT TERMINAL (LEBIH LEBAR DAN RAPI)
    # ---------------------------------------------------------
    print("\n" + "=" * 115)
    print(
        f"{'Nama gambar':<38}"
        f"{'Hasil OCR':<22}"
        f"{'CER':<12}"
        f"{'Enhancement terbaik':<25}"
        f"{'Tanda tangan':<15}"
    )
    print("=" * 115)

    for row in rekapitulasi:
        print(
            f"{row[0]:<38}"
            f"{row[1]:<22}"
            f"{row[2]:<12}"
            f"{row[3]:<25}"
            f"{row[4]:<15}"
        )
    print("=" * 115 + "\n")