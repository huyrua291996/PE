def fac(n):
    if n > 1:
        return n * fac(n - 1)
    else:
        return 1


print(fac(40) / (fac(20) ** 2))