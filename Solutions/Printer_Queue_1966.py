test_case = int(input())

for i in range(test_case):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    sorted_data = list(data)
    sorted_data.sort(reverse=True)

    count = 1
    for i in range(N):
        while data[0] != sorted_data[0]:
            if M == 0:
                M = len(data) - 1
            else:
                M -= 1
            temp = data.pop(0)
            data.append(temp)

        if M == 0:
            print(count)
            break

        data.pop(0)
        count += 1
        M -= 1
        sorted_data.pop(0)
