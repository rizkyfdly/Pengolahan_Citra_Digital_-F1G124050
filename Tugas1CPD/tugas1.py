def isi_array_3d(nama_array, jumlah_matriks):
    print(f"\n--- Mengisi {nama_array} ---")
    print("Contoh input matriks 3x3: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
    
    array_3d = [] 
    
    for indeks in range(jumlah_matriks):
        teks = input(f"Masukkan Matriks ke-{indeks + 1}: ")
        matriks_2d = eval(teks) 
        array_3d.append(matriks_2d) 
        
    return array_3d

def kalikan_array_3d(array_a, array_b):
    jumlah_matriks = len(array_a)
    array_hasil = []

    for indeks in range(jumlah_matriks):
        matriks_a = array_a[indeks]
        matriks_b = array_b[indeks]

        baris_a = len(matriks_a)
        kolom_a = len(matriks_a[0])
        kolom_b = len(matriks_b[0])

        matriks_hasil = []
        for i in range(baris_a):
            baris_kosong = [0] * kolom_b
            matriks_hasil.append(baris_kosong)

        for i in range(baris_a):         
            for j in range(kolom_b):     
                for k in range(kolom_a): 
                    matriks_hasil[i][j] += matriks_a[i][k] * matriks_b[k][j]

        array_hasil.append(matriks_hasil)

    return array_hasil

def tampilkan_layar(judul, data_3d):
    print(f"\n=== {judul} ===")
    for indeks in range(len(data_3d)):
        print(f"Matriks ke-{indeks + 1}:")
        for baris in data_3d[indeks]:
            print("  ", baris)

def main():
    print("------------------------------------------")
    print(" PROGRAM PERKALIAN ARRAY 3 DIMENSI")
    print("------------------------------------------")
    
    jumlah = int(input("Masukkan jumlah matriks yang diinginkan: "))

    data_a = isi_array_3d("Data Array A", jumlah)
    data_b = isi_array_3d("Data Array B", jumlah)

    hasil_akhir = kalikan_array_3d(data_a, data_b)

    tampilkan_layar("Bentuk Array A", data_a)
    tampilkan_layar("Bentuk Array B", data_b)
    tampilkan_layar("HASIL PERKALIAN (A x B)", hasil_akhir)

if __name__ == "__main__":
    main()