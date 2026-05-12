def masukan_bilangan():
    n = int(input("Masukkan nilai n: "))
    m= int(input("Masukkan pangkat: "))

    if n < 0:
        print("Masukkan bilangan positif.")
        return masukan_bilangan()
    elif n == 0:
        print("Masukkan bilangan lebih besar dari nol.")
        return masukan_bilangan()
    elif n != int(n):
        print("Masukkan bilangan bulat.")
        return masukan_bilangan()
    elif m != int(m):
        print("Masukkan pangkat bilangan bulat.")
        return masukan_bilangan()
    return n,m