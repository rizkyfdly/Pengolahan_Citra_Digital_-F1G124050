import cv2
import os
import matplotlib.pyplot as plt

os.makedirs("hasil", exist_ok=True)

for i in range(1, 10):

    nama_file = f"rgb{i}.jpeg"

    gambar = cv2.imread(nama_file)

    if gambar is None:
        print(f"Gambar {nama_file} tidak ditemukan!")
        continue

    grayscale = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)

    nama_hasil = f"hasil/grayscale{i}.jpg"
    cv2.imwrite(nama_hasil, grayscale)

    plt.figure(figsize=(6, 4))
    plt.imshow(grayscale, cmap="gray")
    plt.title(f"Grayscale - RGB {i}")
    plt.axis("off")
    plt.show()

    print(f"Berhasil: {nama_hasil}")