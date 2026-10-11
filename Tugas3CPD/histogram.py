import cv2
import matplotlib.pyplot as plt
import os

os.makedirs("hasil/histogram", exist_ok=True)

for i in range(1, 10):

    nama_file = f"rgb{i}.jpeg"

    gambar = cv2.imread(nama_file)

    if gambar is None:
        print(f"Gambar {nama_file} tidak ditemukan!")
        continue

    gambar_rgb = cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB)

    grayscale = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 1, 1)

    plt.hist(
        gambar_rgb[:, :, 0].ravel(),
        bins=256,
        range=(0, 256),
        alpha=0.5,
        label="Red"
    )

    plt.hist(
        gambar_rgb[:, :, 1].ravel(),
        bins=256,
        range=(0, 256),
        alpha=0.5,
        label="Green"
    )

    plt.hist(
        gambar_rgb[:, :, 2].ravel(),
        bins=256,
        range=(0, 256),
        alpha=0.5,
        label="Blue"
    )

    plt.title(f"Histogram Citra Asli (RGB) - RGB {i}")
    plt.xlabel("Intensitas Piksel")
    plt.ylabel("Jumlah Piksel")
    plt.legend()
    plt.xlim(0, 255)

    plt.subplot(2, 1, 2)

    plt.hist(
        grayscale.ravel(),
        bins=256,
        range=(0, 256)
    )

    plt.title(f"Histogram Grayscale - RGB {i}")
    plt.xlabel("Intensitas Piksel")
    plt.ylabel("Jumlah Piksel")
    plt.xlim(0, 255)

    plt.tight_layout()

    nama_hasil = f"hasil/histogram/histogram{i}.png"
    plt.savefig(nama_hasil, dpi=300)

    plt.close()

    print(f"Berhasil membuat: {nama_hasil}")

print("\nSemua histogram selesai dibuat!")