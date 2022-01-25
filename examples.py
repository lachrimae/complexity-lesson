def my_max(l):
    for entry1 in l:
        bigger_than_all = True
        for entry2 in l:
            if entry1 < entry2:
                bigger_than_all = False
        if bigger_than_all:
            return entry1

def best_max(l):
    result = l[0]
    for entry in l:
        if entry > result:
            result = entry
    return result

def fib_arithmetic(n):
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = 1 - phi
    numerator = math.pow(phi, n) - math.pow(psi, n)
    fraction = numerator / sqrt_5
    return round(fraction)

def fib_exp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_exp(n-1) + fib_exp(n-2)

def fib_lin(n):
    res = [0, 1]
    if n <= 1:
        return res[n]
    for i in range(2, n + 1):
        res.append(res[i-1] + res[i-2])
    return res[-1]