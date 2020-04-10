
# N = int(input()) % 8

for M in range(1, 100):
    N = M % 8
    if 1 <= N < 6:
        print(N)
    elif 6 <= N < 8:
        print(10 - N)
    else:
        print(2)
    