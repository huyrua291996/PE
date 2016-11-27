import time


def seq(n):
    if n % 2 == 0:
        return n / 2
    else:
        return (3 * n) + 1


num = maximum = 0

start = time.time()

cache = {1: 1}

for i in range(1, 1000000, 2):
    result = i
    num_terms = 0
    while result != 1:
        if result in cache:
            num_terms += cache[result]
            break
        else:
            num_terms += 1
            result = seq(result)
    cache[i] = num_terms
    if num_terms > maximum:
        num = i
        maximum = num_terms

print(num)

end = time.time()
print(end - start)