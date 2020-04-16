def solution(s):
    if len(s) == 1:
        return 1
    answer = 1000
    ret = ""
    for l in range(1, len(s)//2+1):
        pattern = s[:l]
        tmp = ""

        cnt = 1
        idx = 0

        while True:
            if pattern == s[idx + l:idx + l * 2]:
                cnt += 1
                idx += l

            else:
                if cnt > 1:
                    tmp += pattern
                    tmp += str(cnt)
                else:
                    tmp += s[idx:idx+l]
                idx += l
                pattern = s[idx:idx+l]
                cnt = 1

            if idx + l > len(s):
                tmp += pattern
                if cnt > 1:
                    tmp += str(cnt)
                break

        if answer > len(tmp):
            answer = len(tmp)
            ret = tmp

    return answer, ret


inputs = ["aabbaccc",
          "ababcdcdababcdcd",
          "abcabcdede",
          "abcabcabcabcdededededede",
          "xababcdcdababcdcd"]

[print(solution(i)) for i in inputs]
