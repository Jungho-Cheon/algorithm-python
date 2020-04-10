N = int(input())
result = []
for _ in range(N):
    arr = sorted([*map(int, input().split())])
    count = [0] * 7

    for i in arr:
        count[i] += 1

    check = False
    for i in range(7):
        if count[i] == 4:
            result.append(50000 + 5000 * i)
            check = True
            break
        elif count[i] == 3:
            result.append(10000 + 1000 * i)
            check = True
            break
        elif count[i] == 2:
            if i == 6:
                result.append(1600)
                check = True
                break
            else:
                for j in range(i + 1, 7):
                    if count[j] == 2:
                        result.append(2000 + 500 * (i + j))
                        check = True
                        break
                result.append(1000 + 100 * i)
                check = True
                break

    if not check:
        result.append(100 * max(arr))

print(max(result))
