N = int(input())
input_data = set(map(int, input().split()))
M = int(input())
check_data = list(map(int, input().split()))
for i in check_data:
    if i in input_data:
        print(1)
    else:
        print(0)
