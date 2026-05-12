#main(gabugan kode modular)
from display import tampilkan_display
from input_bilangan import input_bilangan
from penjumlahan_digit import penjumlahan_digit_bilangan
from input_perpangkatan import masukan_bilangan
from pangkat_bilangan import pangkat_bilangan
import os

def main():
    while True:
        tampilkan_display()
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            n = input_bilangan()
            hasil = penjumlahan_digit_bilangan(n)
            print(f"Jumlah digit dari {n} adalah: {hasil}")
        elif pilihan == '2':
            n, m = masukan_bilangan()
            hasil = pangkat_bilangan(n, m)
            print(f"{n} pangkat {m} adalah: {hasil}")
        elif pilihan == '3':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        input("Tekan Enter untuk melanjutkan...")
        os.system('cls' if os.name == 'nt' else 'clear')
if __name__ == "__main__":
    main()