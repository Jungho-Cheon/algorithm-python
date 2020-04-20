from copy import deepcopy


def isValid(lock):
    for row in lock:
        for i in row:
            if i != 1:
                return False
    return True


def rotate(key):
    ret = [[0]*len(key) for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            ret[i][j] = key[j][len(key) - i - 1]
    return ret


def solution(key, lock):
    a = 0
    b = 0
    for r in key:
        for c in r:
            if c == 1:
                a += 1

    for r in lock:
        for c in r:
            if c == 0:
                b += 1

    if a < b:
        return False

    len_lock = len(lock)
    len_key = len(key)

    # 시작점을 기준으로 검사..
    for row in range(-len_key + 1, len_lock):
        for col in range(-len_key + 1, len_lock):
            # key를 회전해서 비교한다.
            for _ in range(4):
                copy_lock = deepcopy(lock)
                breaker = False
                for i in range(len_key):
                    for j in range(len_key):
                        cx, cy = row + i, col + j

                        if cx < 0 or len_lock <= cx or cy < 0 or len_lock <= cy:
                            continue

                        # key와 lock이 다를 경우에만 성립한다.
                        # key = 1, lock = 0 (key가 맞음)
                        # key = 0, lock = 1 (key가 필요없음)
                        if copy_lock[cx][cy] ^ key[i][j]:
                            copy_lock[cx][cy] = 1
                        else:
                            breaker = True
                            break

                        if isValid(copy_lock):
                            return True
                    if breaker:
                        break
                key = rotate(key)
            key = rotate(key)

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
value = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, value))
