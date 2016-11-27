import math


import math


def proper_divisors(n):
    pro_div = []
    pro_div.append(1)
    for num in range(2, int(math.sqrt(n)) + 1):
        if n % num == 0:
            pro_div.append(num)
            pro_div.append(n / num)
    return set(pro_div)


def generate_abundant(n):
    abundant = []
    for num in range(1, n + 1):
        sum_pds = sum(proper_divisors(num))
        if sum_pds > num:
            abundant.append(num)
    return abundant


ab = generate_abundant(28124)
sums = set()
for char in range(len(ab)):
    for ch in range(char, len(ab)):
        res = ab[char] + ab[ch]
        if res < 28124:
            sums.add(res)
print(sum(set(range(28124)).difference(sums)))