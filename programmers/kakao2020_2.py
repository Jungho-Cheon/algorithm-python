def divbracket(s):
    ck1 = ck2 = 0

    for i in range(len(s)):
        if s[i] == '(':
            ck1 += 1
        elif s[i] == ')':
            ck2 += 1
        if ck1 == ck2:
            return i+1


def check(s):
    v = []
    for b in s:
        if b == "(":
            v.append(b)
        else:
            if not v:
                return False
            v.pop()
    return True


def solution(p):
    if not p:
        return p

    i = divbracket(p)
    u = p[:i]
    v = p[i:]
    if check(u):
        u += solution(v)
        return u
    else:
        tmp = '(' + solution(v) + ')'
        for b in u[1:-1]:
            if b == '(':
                tmp += ')'
            else:
                tmp += '('
        return tmp


inputs = ["(()())()",
          ")(",
          "()))((()"]

[print(solution(i)) for i in inputs]
