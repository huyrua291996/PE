import math


def proper_divisors(n):
    pro_div = []
    pro_div.append(1)
    for num in range(2, math.sqrt(n) + 1):
        if n % num == 0:
            pro_div.append(num)
            pro_div.append(n / num)
    return set(pro_div)


divisors = []
for i in range(0, 10000):
    divisors.append(sum(proper_divisors(i)))
total = 0
for i in range(0, 10000):
    a = divisors[i]
    if a < 10000:
        b = divisors[a]
        if i == b and a != b:
            print ('%d and %d are amicable' % (a, b))
            total += a
print(total)