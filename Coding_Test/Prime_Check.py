# 소수 체크와 소인수 분해

# 소수 체크 기본


def prime_check(N):
    for i in range(2, N):
        if N % i == 0:
            return False
        if i * i > N:
            break
    return True

# 소인수분해 기본


def prime_factorization(N):
    p, fac = 2, []
    while p**2 <= N:
        if N % p == 0:
            N //= p
            fac.append(p)
        else:
            p += 1
    if N > 1:
        fac.append(N)
    return fac


print(prime_factorization(14))

# 소수 리스트를 미리 만들기
# 에라토스테네스의 체


def era_prime(N):
    ck, p = [0] * (N + 1), []
    for i in range(2, N):
        if ck[i] == 1:
            continue
        else:
            p.append(i)
        for j in range(2 * i, N, i):
            ck[j] = 1
    return p


print(era_prime(100))

# 활용 1 : 소인수의 개수


def era_factor_count(N):
    A = [0] * (N + 1)
    for i in range(1, N):
        for j in range(i, N, i):
            A[j] += 1
    return A


# 에라토스테네스의 체를 변형하여 소인수 분해를 할 수 있다.
def era_factorization(N):
    A = [0] * (N + 1)
    for i in range(2, N):
        if A[i]:
            continue
        for j in range(i, N, i):
            A[j] = i
    return A


# 함수 사용법
# 100까지 자신을 나누어 떨어질 수 있는 소수 중 가장 큰 값을 구한다
A = era_factorization(100)
# 84를 소인수 분해 한다
N = 84
while A[N] != 0:
    print(A[N])
    # N을 소수로 나눠 다음 수에 대해 소인수를 구한다.
    N //= A[N]




# 빠른 거듭제곱과 모듈러
# C/C++ Style
def pow_advanced(a, b, mod):
    ret = 1
    while b > 0:
        if b % 2:
            ret = ret * a % mod
        a, b = a * a % mod, b // 2
    return ret


print('pow_advanced :', pow_advanced(2, 3, 1000))
print('pow :', pow(2, 3))
