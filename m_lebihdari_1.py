import matplotlib.pyplot as plt # Mengimpor library matplotlib.pyplot yang digunakan untuk membuat visualisasi grafik

# Deklarasikan definisi fungsi buat nerima 4 parameter : koordinat titik awal (x1,y1) dan titik akhir (x2,y2)
def koordinat_titik(x1, y1, x2, y2):
    points = [] # Membuat list kosong, buat nampung koordinat titik yang akan dihitung
    iterasi = 1
    
    # Mengecek jika ada nilai x1 > x2 atau y1 > y2 untuk ditukar
    if y1 > y2:
        print("Nilai x1 lebih besar dari x2, maka akan dilakukan penukaran posisi") # Memberikan keterangan
        y1, y2 = y2, y1 # Menukar y1 dan y2
        x1, x2 = x2, x1 # Menukar x1 dan x2


    # Hitung perbedaan x dan y
    a = x2 - x1 # Menghitung selisih antara koordinat x2 dengan x1 dan disimpan dalam var a
    b = y2 - y1 # Menghitung selisih antara koordinat y2 dengan y1 dan disimpan dalam var b

    # Hitung kemiringan
    m = a / b
    
    # Menginisialisasi titik awal dengan nilai x1 dan y1
    x = x1
    y = y1
    # Menambahkan koordinat titik tersebut ke dalam list points
    points.append((x, y))
    
    # Menggunakan Loop While untuk iterasi
    while y < y2: # Kondisi ketika nilai y < y2, maka selanjutnya
        y += 1 # Menambahkan nilai y sebesar 1 setiap iterasi
        x = round(x1 + m * (y - y1)) # Menghitung nilai x menggunakan rumus pers garis x = x1 + m(y-y1) di dalam fungsi round() untuk memperoleh hasil nilai x yang dibulatkan
        points.append((x, y)) # Menambahkan koordinat (x,y) ke dalam list points
        iterasi += 1 # Menambahkan iterasi
    
    # Loop While ini akan terus berjalan sampai nilai y mencapai y2
    print(f"Jumlah Iterasi : {iterasi}") # Pakai f atau format untuk memanggil variabel dalam print
    return points

# Deklarasikan definisi fungsi untuk menggambar grafik dengan 4 parameter yang sama
def brute_force(x1, y1, x2, y2):
    # Memanggil fungsi koordinat_titik untuk mendapatkan list koordinat titik dari 4 paramaternya
    koordinatTitik = koordinat_titik(x1, y1, x2, y2)
    
    # Memisahkan koordinat x dan y dari list koordinatTitik menggunakan list comprehension
    x_coords = [point[0] for point in koordinatTitik] # Buat list baru berisi nilai point[0] untuk setiap point yang ada di dalam var- koordinatTitik
    y_coords = [point[1] for point in koordinatTitik] # Buat list baru berisi nilai point[1] untuk setiap point yang ada di dalam var koordinatTitik
    
    # Membuat grafiknya
    plt.figure(figsize=(10, 8)) # Ukuran kanvas grafiknya
    # Membuat grafik dengan titik berbentuk lingkaran, garis warna biru, ukuran titiknya 5, garisnya tipe solid, dan ketebalan garis = 1
    plt.plot(x_coords, y_coords, marker='o', color='blue', markersize=5, linestyle='-', linewidth=1)
    plt.title("Plot Titik Koordinat Algoritma Brute-Force") # Menambahkan judul grafik
    plt.xlabel("X") # Menambahkan label sumbu X
    plt.ylabel("Y") # Menambahkan label sumbu Y
    plt.grid(True) # Menampilkan grid pada grafik
    plt.gca().set_aspect('equal', adjustable='box') # Mengatur aspek ratio grafik agar skala X dan Y sama
    plt.show() # Menampilkan grafik

# Meminta User Untuk Memasukkan Input Koordinat
x1 = int(input("Masukkan nilai x1: ")) # Mengkonversi Input Data menjadi Tipe Data Integer
y1 = int(input("Masukkan nilai y1: ")) # Mengkonversi Input Data menjadi Tipe Data Integer
x2 = int(input("Masukkan nilai x2: ")) # Mengkonversi Input Data menjadi Tipe Data Integer
y2 = int(input("Masukkan nilai y2: ")) # Mengkonversi Input Data menjadi Tipe Data Integer

# Memanggil fungsi koordinat_titik
algo_bf = koordinat_titik(x1, y1, x2, y2)

# Mencetak semua koordinat yang dihasilkan
print("Koordinat Titik: ")
for point in algo_bf:
    print(point)

# Memanggil fungsi brute_force untuk menampilkan visualisasi grafik
brute_force(x1, y1, x2, y2)
