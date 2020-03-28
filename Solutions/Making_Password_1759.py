# 모든 조합을 찾기위해 itertools 라이브러리의 combinations를 사용한다.
from itertools import combinations

# 모음
vowels = ('a', 'e', 'i', 'o', 'u')

L, C = map(int, input().split())
array = list(input().split())
array.sort()

for password in combinations(array, L):
    count = 0
    for i in password:
        if i in vowels:
            count += 1

    if count >= 1 and count <= L - 2:
        print(''.join(password))
