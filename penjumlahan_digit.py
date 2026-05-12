def penjumlahan_digit_bilangan(n):
    if n == 0:
        return 0
    else:
        digit = n % 10
        return digit + penjumlahan_digit_bilangan(n // 10)
    
#penjelasan Algoritma
"""
Algoritma penjumlahan digit bilangan menggunakan pendekatan rekursif bekerja dengan cara
memecah sebuah bilangan menjadi digit-digitnya satu per satu, kemudian menjumlahkan
seluruhnya secara bertahap. Proses ini memanfaatkan dua operasi dasar, yaitu modulus
(n % 10) untuk mengambil digit terakhir dari suatu bilangan, dan pembagian bulat
(n // 10) untuk membuang digit terakhir tersebut sehingga tersisa bilangan yang lebih
kecil. Sebagai contoh, bilangan 4821 akan diproses dengan mengambil digit 1 terlebih
dahulu, kemudian menyerahkan sisa bilangan 482 untuk diproses pada pemanggilan
berikutnya, begitu seterusnya hingga tidak ada digit yang tersisa.
 
Seperti semua fungsi rekursif, algoritma ini memiliki dua bagian utama. Pertama adalah
basis (base case), yaitu kondisi berhenti yang ditetapkan ketika nilai n sama dengan 0.
Pada titik ini tidak ada digit yang perlu dijumlahkan lagi sehingga fungsi mengembalikan
nilai 0 secara langsung. Tanpa basis ini, fungsi akan terus memanggil dirinya sendiri
tanpa henti dan menyebabkan program berhenti dengan error. Kedua adalah rekurens
(recursive case), yaitu kondisi ketika n tidak sama dengan 0. Pada kondisi ini, fungsi
mengambil digit terakhir dari n menggunakan operasi n % 10, lalu menjumlahkannya dengan
hasil pemanggilan fungsi itu sendiri menggunakan sisa bilangan n // 10. Rumus lengkapnya
dapat ditulis sebagai: jumlah_digit(n) = (n % 10) + jumlah_digit(n // 10).
 
Proses rekursi ini pasti akan berhenti karena setiap pemanggilan selalu menghasilkan
nilai n // 10 yang lebih kecil dari n sebelumnya. Bilangan bulat positif yang terus
dibagi 10 pasti akan mencapai 0 dalam jumlah langkah yang terbatas, yaitu sebanyak
jumlah digit yang dimiliki bilangan tersebut. Sebagai ilustrasi, bilangan 4821 memiliki
4 digit sehingga fungsi akan dipanggil sebanyak 4 kali sebelum akhirnya mencapai basis
dan mengembalikan nilai 0. Hasil akhir kemudian terbentuk secara bertahap saat nilai
dikembalikan dari dalam ke luar, yaitu 0, lalu 4, lalu 12, lalu 14, dan akhirnya 15
sebagai jumlah keseluruhan digit 4 + 8 + 2 + 1.
"""