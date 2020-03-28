# 걸그룹 마스터 준석이

N, M = map(int, input().split())
data = {}
result = []
for _ in range(N):
    group_name = input()
    data[group_name] = [input() for _ in range(int(input()))]

group_names = [*data.keys()]
# print(group_names)

for _ in range(M):
    answer = input()
    question = int(input())
    if question == 1:
        for i in group_names:
            if answer in data[i]:
                result.append(i)
    else:
        [result.append(name) for name in sorted(data[answer])]

print("\n".join(result))
