# 순열 구하기

arr = [2, 5, 7]
v = []
ck = [False] * len(arr)


def sequence(num):
    if num == 0:
        print(v)
        return

    for i in range(len(arr)):
        if ck[i]:
            continue
        ck[i] = True
        v.append(arr[i])
        sequence(num - 1)
        v.pop()
        ck[i] = False


sequence(3)
