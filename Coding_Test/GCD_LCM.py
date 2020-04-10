# 최소 공배수와 최대 공약수는 유클리드 호제법을 이용한다.

# 최대 공약수
# GCD(a,b) == GCD(b, a%b)
import math


def gcd_native(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def gcd(a, b):
    return gcd(b, a % b) if a % b != 0 else b


def gcd2(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


print(gcd(4, 12), gcd2(4, 12))
print(math.gcd(4, 12))

# 최소 공배수
def lcm(a, b):
    return int(a * b / gcd(a, b))


print(lcm(4, 7))
