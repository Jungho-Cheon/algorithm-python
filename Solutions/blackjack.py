#cards_num, cards_sum = map(int, input().split())
#data = list(map(int, input().split()))
from itertools import combinations

cards_num, cards_sum = 5, 21
data = [5, 6, 7, 8, 9]


def blackjack_1(data, cards_num, cards_sum):
    past = 0
    for i in range(0, cards_num):
        for j in range(i + 1, cards_num):
            for k in range(j + 1, cards_num):
                current = data[i] + data[j] + data[k]
                if current <= cards_sum and past < current:
                    past = current
    return past


def blackjack_2(data, cards_num, cards_sum):
    all_list = list(combinations(data, 3))
    result = 0
    for i in range(len(all_list)):
        current = 0
        for j in range(3):
            current += all_list[i][j]

        if current <= cards_sum and current > result:
            result = current

    return result


print(blackjack_1(data, cards_num, cards_sum))
print(blackjack_2(data, cards_num, cards_sum))
