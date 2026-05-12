#pangkat m bilangan n
def pangkat_bilangan(n, m):
    if m == 0:
        return 1
    elif m < 0:
        return 1 / pangkat_bilangan(n, -m)
    else:
        return n * pangkat_bilangan(n, m - 1)
    
#Pola perpangkatan
"""
Algoritma perpangkatan bilangan menggunakan pendekatan rekursif bekerja dengan cara
memecah operasi perkalian berulang menjadi langkah-langkah yang lebih kecil dan
dikerjakan satu per satu. Perhatikan contoh berikut: 2^4 pada dasarnya adalah
2 x 2 x 2 x 2, yang jika dikelompokkan dapat ditulis sebagai 2 x (2 x 2 x 2),
atau dengan kata lain 2 x 2^3. Dari sini terlihat bahwa sebuah perpangkatan selalu
dapat dinyatakan sebagai hasil kali basis dengan perpangkatan yang eksponennya
berkurang satu, sehingga terbentuk pola yang berulang dan cocok diselesaikan
menggunakan rekursi.
 
Pola tersebut dapat diamati secara lebih lengkap sebagai berikut: 2^4 = 2 x 2^3,
kemudian 2^3 = 2 x 2^2, lalu 2^2 = 2 x 2^1, lalu 2^1 = 2 x 2^0, dan akhirnya
2^0 = 1 berdasarkan kaidah matematika yang berlaku untuk semua bilangan. Dari pola
ini dapat disimpulkan bahwa n^m = n x n^(m-1), karena setiap langkah hanya mengambil
satu faktor perkalian n dan menyerahkan sisa perhitungan kepada pemanggilan fungsi
berikutnya dengan eksponen yang sudah berkurang satu. Proses ini terus berulang hingga
eksponen mencapai nol, yang menjadi basis dari rekursi dan langsung mengembalikan
nilai 1 tanpa perlu melakukan perhitungan lebih lanjut.
 
Apabila nilai eksponen m merupakan bilangan negatif, maka perhitungan tidak dapat
dilakukan secara langsung menggunakan pola di atas, karena eksponen yang negatif tidak
akan pernah mencapai basis m sama dengan nol jika dikurangi satu setiap pemanggilan.
Untuk menangani kondisi ini, digunakan sifat matematika yang menyatakan bahwa n^m
dengan m negatif sama dengan 1 dibagi n^(-m), atau dapat ditulis sebagai
n^(-m) = 1 / n^m. Dengan kata lain, perpangkatan dengan eksponen negatif merupakan
kebalikan dari perpangkatan dengan eksponen positif yang setara. Penerapannya dalam
fungsi rekursif adalah dengan membalik tanda eksponen terlebih dahulu menjadi positif,
kemudian memanggil fungsi yang sama dengan eksponen positif tersebut, dan terakhir
membagi 1 dengan hasilnya. Sebagai contoh, 2^(-3) diselesaikan dengan menghitung
1 dibagi pangkat_bilangan(2, 3), yang menghasilkan 1 dibagi 8 sama dengan 0.125.

misal 2^4 = 2x2x2x2
2^4 = 2(2x2x2)
2^4 = 2x2^3

Pola perpangkatan bisa juga ditulis sebagai berikut:
2^4 = 2x2^3
2^3 = 2x2^2
2^2 = 2x2^1
2^1 = 2x2^0
2^0 = 1 (rumus matematika)

dari sini kita dapat menyimpulkan bahwa n^m = n x n^(m-1) karena pangkat
m dikurangi 1 setiap kali kita mengalikan n dengan hasil perpangkatan sebelumnya.
Atau jika m itu bilangan negatif, maka n^m = 1 / n^(-m) karena kita membalikkan hasil perpangkatan untuk mendapatkan nilai yang benar.
"""