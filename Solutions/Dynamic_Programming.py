# * 동적 계획법 (Dynamic Programming)
#   -> Memoization : 중간 결과값을 저장하여 최종 결과값을 도출하는데 사용함.
#   -> 계산 중복을 피해 시간을 단축할 수 있다.
#   -> 중간 결과값 저장을 위해 저장공간이 필요하다.
#   -> 점화식을 구해서 다음 인덱스의 값을 찾는다.

# 분할정복과 동적계획법은 둘 다 큰 문제를 해결하기 위해 작은 문제로 나누는 기법으로 공통점을 갖는다.

# 1) Recursive한 구현은 스택에 쌓여져서 같은값을 여러번 구하게된다.
def fibo_1(num):
    if num <= 1:
        return num
    return fibo_1(num - 1) + fibo_1(num - 2)


# 2) Memoization을 하기위해 리스트를 사용
def DP_fibo(num):
    DP = list([0 for a in range(num + 1)]) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    DP[1] = 1

    for idx in range(2, num + 1):
        DP[idx] = DP[idx - 1] + DP[idx - 2]

    return DP[num]


DP = DP_fibo(7)
print(DP)
