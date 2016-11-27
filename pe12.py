import math


def get_factors(n):
    factors = []
    factors.append(1)
    for num in range(2, math.sqrt(n) + 1):
        if n % num == 0:
            factors.append(num)
            factors.append(n / num)
    factors.append(n)
    return set(factors)


def main():
    i = n = 0
    factors = []

    while len(factors) < 500:
        i += 1
        n += i
        factors = get_factors(n)

    print(n)


if __name__ == "main":
    main() 