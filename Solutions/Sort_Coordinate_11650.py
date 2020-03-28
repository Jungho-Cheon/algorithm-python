num_coordinate = int(input())

data = list()
for _ in range(num_coordinate):
    x, y = map(int, input().split())
    data.append((x, y))

# python의 기본 정렬 라이브러리는 굳이 key를 사용하지 않아도 첫번째요소~마지막요소 순서로 정렬한다..
data.sort(key=lambda x: (x[0], x[1]))

for i in range(len(data)):
    print(data[i][0], data[i][1])
