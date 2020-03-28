# 프린터 큐
test_case = int(input())
result = []
for _ in range(test_case):
    N, M = map(int, input().split())
    input_data = list(map(int, input().split()))
    array = [(i, prio) for i, prio in enumerate(input_data)]
    order_array = [i[1] for i in array]
    order_array.sort(reverse=True)
    count = 1
    while array:
        if array[0][1] < order_array[0]:
            array.append(array.pop(0))
        elif array[0][1] == order_array[0]:
            if array[0][0] == M:
                result.append(count)
                break
            else:
                array.pop(0)
                order_array.pop(0)
                count += 1

for i in result:
    print(i)
