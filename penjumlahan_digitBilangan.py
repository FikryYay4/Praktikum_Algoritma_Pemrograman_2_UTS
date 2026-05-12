def jumlah_digit_bilangan(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + jumlah_digit_bilangan(n // 10)