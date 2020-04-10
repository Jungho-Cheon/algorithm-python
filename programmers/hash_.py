# 위장ㄴ

# 의상의 종류 별로 분류하여 몇개의 의상이 있는지 count한다.
# 이후 의상의 종류별로 입지 않는 경우의 수를 추가하기 위해 +1 한다.
# 모든 조합을 구하기 위해 모두 곱한다.
# 이후 모두 입지 않는 경우의 수를 빼기위해 -1한다.


def solution(clothes):
    if len(clothes) == 0:
        return 0

    hash = dict()
    for c, label in clothes:
        if label in hash:
            hash[label] += 1
        else:
            hash[label] = 1

    counts = list([*hash.values()])

    answer = 1
    for c in counts:
        answer *= c + 1

    return answer - 1


clothes = [['yellow_hat', 'headgear'], [
    'blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
print(solution(clothes))
