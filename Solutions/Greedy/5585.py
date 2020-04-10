N = 1000 - int(input())
result = 0
for e in [500, 100, 50, 10, 5, 1]:
    result += N // e
    N %= e
print(result)
