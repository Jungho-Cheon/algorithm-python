def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


a, b = 4, 8
print(gcd(a, b), lcm(a, b))
