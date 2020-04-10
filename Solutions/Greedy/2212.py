# 센서
import sys

N = int(input())
K = int(input())

if K >= N:
    print(0)
    sys.exit()

sensors = {*map(int, input().split())}
sensors = list(sensors)
sensors.sort()

dist = []
for i in range(len(sensors) - 1):
    dist.append(sensors[i + 1] - sensors[i])
dist.sort(reverse=True)
result = 0
for i in dist[K - 1:]:
    result += i
print(result)
