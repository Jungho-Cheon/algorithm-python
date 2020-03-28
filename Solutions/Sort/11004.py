# k번째 수

N, K = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
print(array[K - 1])
