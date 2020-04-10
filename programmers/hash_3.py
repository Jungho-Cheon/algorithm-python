# 베스트 앨범


def solution(genres, plays):
    answer = []

    hash1 = dict()
    hash2 = dict()
    for idx, g in enumerate(genres):
        if g in hash1:
            hash1[g] += plays[idx]
        else:
            hash1[g] = plays[idx]

        if g in hash2:
            hash2[g].append((plays[idx], idx))
        else:
            hash2[g] = [(plays[idx], idx)]

    # 장르별 총 재생 수 -> 어떤 장르가 총 재생 수가 많은지 알아야낸다.
    tmp = list(zip(hash1.keys(), hash1.values()))
    tmp.sort(key=lambda x: -x[1])

    for genre, _ in tmp:
        lst = list()
        for play, idx in hash2[genre]:
            lst.append((play, idx))
        lst.sort(key=lambda x: -x[0])

        # 최대 2개까지 베스트 앨범에 담는다.
        for _, idx in lst[:min(len(lst), 2)]:
            answer.append(idx)

    return answer


print(solution(['classic', 'pop', 'classic',
                'classic', 'pop'], [500, 600, 150, 800, 2500]))
