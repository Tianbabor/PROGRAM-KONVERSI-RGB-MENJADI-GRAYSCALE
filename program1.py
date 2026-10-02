# ==========================================
# TUGAS PENGOLAHAN CITRA DIGITAL
# KONVERSI RGB MENJADI GRAYSCALE
# ==========================================

# 1. Import library
import cv2
import matplotlib.pyplot as plt

# 2. Membaca citra
gambar = cv2.imread("foto_saya.jpeg")

# Mengecek gambar
if gambar is None:
    print("Foto tidak ditemukan!")
else:

    # 3. Menampilkan citra asli
    gambar_rgb = cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB)

    # 4. Proses pengolahan citra
    grayscale = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)

    # 5. Menampilkan citra asli dan hasil grayscale
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(gambar_rgb)
    plt.title("Citra Asli")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(grayscale, cmap="gray")
    plt.title("Citra Grayscale")
    plt.axis("off")

    plt.show()

    # 6. Menyimpan hasil
    cv2.imwrite("hasil_grayscale.jpg", grayscale)

    print("Hasil berhasil disimpan sebagai hasil_grayscale.jpg")