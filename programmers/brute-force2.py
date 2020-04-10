res = 0
v = list()
seq = set()
ck = [False] * 8


def isPrime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True


def countPrime(cnt, numbers):
    s = ""
    for i in v:
        s += i
    if len(s):
        if isPrime(int(s)):
            seq.add(int(s))

    if cnt == len(numbers):
        return

    for i in range(0, len(numbers)):
        if ck[i]:
            continue
        ck[i] = True
        v.append(numbers[i])
        countPrime(cnt+1, numbers)
        v.pop()
        ck[i] = False


def solution(numbers):

    numbers = list(numbers)
    countPrime(0, numbers)

    return len(seq)


print(solution("17"))
