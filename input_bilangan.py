def input_bilangan():
    n = int(input("Masukkan nilai bilangan: "))
    if n < 0:
        print("Masukkan bilangan positif.")
        return input_bilangan()
    elif n == 0:
        print("Masukkan bilangan lebih besar dari nol.")
        return input_bilangan()
    elif n != int(n):
        print("Masukkan bilangan bulat.")
        return input_bilangan()
    return n