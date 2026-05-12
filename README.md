# Praktikum_Algoritma_Pemrograman_2_UTS
# 🔁 Recursive Arithmetic Python Project

> README ini sudah dikonversi full Markdown dan siap langsung di-copy ke file `README.md` pada GitHub.

<div align="center">

# 📘 UTS Struktur Data & Algoritma

### Program Rekursif Penjumlahan Digit dan Perpangkatan Bilangan

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Algorithm](https://img.shields.io/badge/Algorithm-Recursive-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey?style=for-the-badge)

</div>

---

# 📌 Deskripsi Project

Project ini merupakan implementasi algoritma rekursif menggunakan bahasa Python untuk menyelesaikan dua operasi matematika dasar:

1. 🔢 Penjumlahan digit bilangan
2. ⚡ Perpangkatan bilangan

Program dibuat dengan konsep modular programming sehingga setiap fitur dipisahkan ke dalam file berbeda agar lebih rapi, mudah dipahami, dan mudah dikembangkan.

---

# 🎯 Tujuan Project

Project ini dibuat untuk:

* Memahami konsep dasar rekursi
* Melatih logika algoritma
* Memahami base case dan recursive case
* Mengimplementasikan modular programming
* Menerapkan operasi matematika menggunakan fungsi rekursif

---

# 🧠 Konsep Rekursi

Rekursi adalah teknik pemrograman di mana sebuah fungsi memanggil dirinya sendiri untuk menyelesaikan masalah yang lebih kecil hingga mencapai kondisi berhenti.

## Struktur Dasar Rekursi

```python
fungsi(data):
    if kondisi_berhenti:
        return hasil
    else:
        return proses + fungsi(data_yang_lebih_kecil)
```

### Rekursi selalu memiliki:

| Komponen       | Fungsi                                                |
| -------------- | ----------------------------------------------------- |
| Base Case      | Kondisi berhenti agar fungsi tidak berjalan selamanya |
| Recursive Case | Pemanggilan fungsi terhadap masalah yang lebih kecil  |

---

# 📂 Struktur Project

```bash
uts_301250004_MochammadFikryNugraha/
│
├── main.py
├── display.py
├── input_bilangan.py
├── input_perpangkatan.py
├── penjumlahan_digit.py
├── penjumlahan_digitBilangan.py
├── pangkat_bilangan.py
└── __pycache__/
```

---

# ⚙️ Penjelasan File

## 📄 main.py

File utama program.

Fungsi:

* Menjalankan menu
* Mengatur alur program
* Memanggil fungsi dari module lain

---

## 📄 display.py

Berisi tampilan menu program.

```python
def tampilkan_display():
    print("=== Aritmatika === ")
```

---

## 📄 input_bilangan.py

Digunakan untuk validasi input bilangan.

Validasi:

* Tidak boleh negatif
* Tidak boleh nol
* Harus bilangan bulat

---

## 📄 input_perpangkatan.py

Digunakan untuk input:

* Basis bilangan
* Pangkat bilangan

---

## 📄 penjumlahan_digit.py

Berisi algoritma rekursif untuk menjumlahkan digit.

```python
def penjumlahan_digit_bilangan(n):
    if n == 0:
        return 0
    else:
        digit = n % 10
        return digit + penjumlahan_digit_bilangan(n // 10)
```

---

## 📄 pangkat_bilangan.py

Berisi algoritma rekursif perpangkatan.

```python
def pangkat_bilangan(n, m):
    if m == 0:
        return 1
    elif m < 0:
        return 1 / pangkat_bilangan(n, -m)
    else:
        return n * pangkat_bilangan(n, m - 1)
```

---

# 🔍 Algoritma Penjumlahan Digit

## 📖 Logika Dasar

Penjumlahan digit dilakukan dengan:

1. Mengambil digit terakhir menggunakan `% 10`
2. Menghapus digit terakhir menggunakan `// 10`
3. Memanggil fungsi kembali hingga angka menjadi `0`

---

## 🧩 Mengapa Rekursi Bisa Digunakan?

Karena masalah besar dapat dipecah menjadi masalah lebih kecil.

Contoh:

```text
4821
= 1 + jumlah_digit(482)
= 1 + 2 + jumlah_digit(48)
= 1 + 2 + 8 + jumlah_digit(4)
= 1 + 2 + 8 + 4 + jumlah_digit(0)
= 15
```

---

## 🧠 Pola Rekursif

```text
jumlah_digit(n)
= digit_terakhir + jumlah_digit(sisa_digit)
```

atau:

```text
jumlah_digit(n)
= (n % 10) + jumlah_digit(n // 10)
```

---

## 🔄 Simulasi Rekursi

### Input:

```text
1234
```

### Proses:

| Pemanggilan Fungsi | Nilai      |
| ------------------ | ---------- |
| f(1234)            | 4 + f(123) |
| f(123)             | 3 + f(12)  |
| f(12)              | 2 + f(1)   |
| f(1)               | 1 + f(0)   |
| f(0)               | 0          |

### Hasil:

```text
4 + 3 + 2 + 1 = 10
```

---

# ⚡ Algoritma Perpangkatan

## 📖 Logika Dasar

Perpangkatan sebenarnya adalah perkalian berulang.

Contoh:

```text
2^4 = 2 × 2 × 2 × 2
```

Jika diperhatikan:

```text
2^4 = 2 × 2^3
2^3 = 2 × 2^2
2^2 = 2 × 2^1
2^1 = 2 × 2^0
2^0 = 1
```

---

# 🧠 Mengapa Bisa Menjadi Rekursif?

Karena pola perpangkatan memiliki hubungan terhadap dirinya sendiri.

```text
n^m = n × n^(m-1)
```

Setiap langkah:

* Pangkat berkurang 1
* Fungsi memanggil dirinya sendiri
* Berhenti saat pangkat = 0

---

## 🔄 Simulasi Rekursi

### Input:

```text
2^4
```

### Proses:

| Pemanggilan Fungsi | Hasil      |
| ------------------ | ---------- |
| f(2,4)             | 2 × f(2,3) |
| f(2,3)             | 2 × f(2,2) |
| f(2,2)             | 2 × f(2,1) |
| f(2,1)             | 2 × f(2,0) |
| f(2,0)             | 1          |

### Perhitungan Balik:

```text
2 × 2 × 2 × 2 × 1 = 16
```

---

# 📉 Kompleksitas Algoritma

| Algoritma             | Time Complexity | Space Complexity |
| --------------------- | --------------- | ---------------- |
| Penjumlahan Digit     | O(n)            | O(n)             |
| Perpangkatan Rekursif | O(m)            | O(m)             |

Keterangan:

* `n` = jumlah digit
* `m` = nilai pangkat

---

# ▶️ Cara Menjalankan Program

## 1️⃣ Clone Repository

```bash
git clone https://github.com/username/repository.git
```

---

## 2️⃣ Masuk ke Folder Project

```bash
cd uts_301250004_MochammadFikryNugraha
```

---

## 3️⃣ Jalankan Program

```bash
python main.py
```

atau

```bash
python3 main.py
```

---

# 🖥️ Tampilan Program

```text
=== Aritmatika ===
1. Penjumlahan digit Bilangan
2. Menghitung perpangkatan Bilangan
3. Keluar
```

---

# 📌 Contoh Output

## 🔢 Penjumlahan Digit

### Input:

```text
1234
```

### Output:

```text
Jumlah digit dari 1234 adalah: 10
```

---

## ⚡ Perpangkatan Bilangan

### Input:

```text
2
4
```

### Output:

```text
2 pangkat 4 adalah: 16
```

---

# 🚨 Validasi Input

Program memiliki validasi:

✅ Bilangan tidak boleh negatif

✅ Bilangan tidak boleh nol

✅ Input harus integer

---

# 🧪 Edge Case

| Input           | Hasil                   |
| --------------- | ----------------------- |
| 0 digit         | 0                       |
| Pangkat 0       | 1                       |
| Pangkat negatif | 1 / n^m                 |
| Bilangan besar  | Tetap diproses rekursif |

---

# 📚 Teknologi yang Digunakan

| Teknologi           | Fungsi                 |
| ------------------- | ---------------------- |
| Python              | Bahasa pemrograman     |
| Rekursi             | Penyelesaian algoritma |
| Modular Programming | Struktur project       |

---

# ✨ Keunggulan Project

✅ Menggunakan konsep rekursi murni

✅ Struktur modular dan rapi

✅ Mudah dipahami pemula

✅ Memiliki validasi input

✅ Dilengkapi penjelasan algoritma

✅ Cocok untuk pembelajaran dasar struktur data dan algoritma

---

# 📖 Kesimpulan

Project ini menunjukkan bahwa:

* Rekursi mampu menyelesaikan masalah kompleks dengan cara sederhana
* Masalah matematika dapat dipecah menjadi submasalah lebih kecil
* Base case sangat penting agar rekursi berhenti
* Rekursi sangat cocok untuk pola yang berulang

Implementasi penjumlahan digit dan perpangkatan menjadi contoh nyata bagaimana algoritma rekursif bekerja secara bertahap hingga menghasilkan solusi akhir.

---

# 👨‍💻 Author

### Mochammad Fikry Nugraha

📚 Teknik Informatika

🎓 Project UTS Struktur Data & Algoritma

---

# ⭐ Support

Jika project ini membantu:

🌟 Berikan star pada repository

🍴 Fork repository ini

📢 Bagikan ke teman

---
